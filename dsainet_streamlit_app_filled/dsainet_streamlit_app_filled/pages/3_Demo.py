from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
DEMO_DIR = REPO_ROOT / "dsainet_demo"

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from utils import inject_css, init_lang_state, sidebar_language_switcher, tr, section_badge


st.set_page_config(page_title="Demo | DSAINet", layout="wide")
inject_css()
init_lang_state()

st.markdown(
    """
    <style>
    .demo-ribbon{
        height:6px;border-radius:999px;margin:.3rem 0 .9rem 0;
        background:linear-gradient(90deg,#1768ac 0%,#16857a 34%,#f2b84b 67%,#b24736 100%);
    }
    .demo-visual-title{
        font-size:1.05rem;font-weight:850;color:#172026;margin:.1rem 0 .45rem 0;
        display:flex;align-items:center;gap:.45rem;
    }
    .demo-dot{width:.72rem;height:.72rem;border-radius:999px;display:inline-block;}
    .demo-card-note{
        color:#5f6b73;font-size:.9rem;line-height:1.55;margin-top:.25rem;
    }
    .demo-highlight{
        border:1px solid #dbe3e8;border-radius:8px;padding:1rem 1.1rem;
        background:linear-gradient(135deg,#ffffff 0%,#f6fbff 55%,#f7fbf8 100%);
        box-shadow:0 12px 30px rgba(23,32,38,.07);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def local_demo_path(raw_path: object) -> Path:
    path_text = str(raw_path).replace("\\", "/")
    marker = "dsainet_demo/"
    if marker in path_text:
        return REPO_ROOT / "dsainet_demo" / path_text.split(marker, 1)[1]
    return DEMO_DIR / path_text


@st.cache_data
def load_trials() -> pd.DataFrame:
    manifest = DEMO_DIR / "demo_trials_manifest.csv"
    df = pd.read_csv(manifest)
    df["trial_label"] = df.apply(
        lambda row: (
            f'{row["class_name"]} | {row["split"]} | '
            f'trial {row["trial_index"]} | conf {float(row["confidence"]):.2%}'
        ),
        axis=1,
    )
    return df


@st.cache_data
def load_forward_shapes(dataset: str) -> pd.DataFrame:
    path = DEMO_DIR / "forward_pass" / f"{dataset}_forward_shapes.csv"
    return pd.read_csv(path)


@st.cache_data
def load_forward_steps(dataset: str) -> list[dict]:
    path = DEMO_DIR / "forward_pass" / f"{dataset}_forward_steps.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f).get("steps", [])


@st.cache_data
def load_label_coverage(dataset: str) -> pd.DataFrame:
    path = DEMO_DIR / "label_coverage" / f"{dataset}_label_coverage.csv"
    return pd.read_csv(path)


def show_visual_card(title: str, path: Path, caption: str, accent: str) -> None:
    st.markdown(
        f"""
        <div class="demo-visual-title">
            <span class="demo-dot" style="background:{accent};"></span>{title}
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        if path.exists():
            st.image(str(path), use_container_width=True)
            st.markdown(f'<div class="demo-card-note">{caption}</div>', unsafe_allow_html=True)
        else:
            st.warning(f"Missing file: {path}")


with st.sidebar:
    sidebar_language_switcher()

section_badge("Real exported demo materials", "真实导出的 demo 材料")
st.title(tr("Interactive DSAINet Demo", "DSAINet 交互式演示"))
st.markdown('<div class="demo-ribbon"></div>', unsafe_allow_html=True)

if not (DEMO_DIR / "demo_trials_manifest.csv").exists():
    st.error(f"Cannot find demo manifest: {DEMO_DIR / 'demo_trials_manifest.csv'}")
    st.stop()

trials = load_trials()

metric_cols = st.columns(4, gap="medium")
metric_cols[0].metric(tr("Datasets", "数据集"), trials["dataset"].nunique())
metric_cols[1].metric(tr("Demo trials", "Demo trial"), len(trials))
metric_cols[2].metric(tr("Trials per label", "每类 trial"), "3")
metric_cols[3].metric(tr("Correct samples", "预测正确样本"), f'{int(trials["is_correct"].sum())}/{len(trials)}')

st.write("")
st.markdown(f"### {tr('Step 1: Choose a Real Trial', '步骤 1：选择真实样本')}")

controls = st.columns([1.1, 1.1, 2.3], gap="medium")
dataset = controls[0].selectbox(
    tr("Dataset", "数据集"),
    sorted(trials["dataset"].unique()),
    key="real_demo_dataset",
)

dataset_trials = trials[trials["dataset"] == dataset].copy()
class_name = controls[1].selectbox(
    tr("True label", "真实标签"),
    sorted(dataset_trials["class_name"].unique()),
    key="real_demo_class",
)

class_trials = dataset_trials[dataset_trials["class_name"] == class_name].copy()
trial_label = controls[2].selectbox(
    tr("Trial", "样本"),
    class_trials["trial_label"].tolist(),
    key="real_demo_trial",
)
selected = class_trials[class_trials["trial_label"] == trial_label].iloc[0]

info_cols = st.columns(5, gap="medium")
info_cols[0].metric(tr("Protocol", "协议"), str(selected["strategy"]))
info_cols[1].metric(tr("Split", "划分"), str(selected["split"]))
info_cols[2].metric(tr("True label", "真实标签"), str(selected["class_name"]))
info_cols[3].metric(tr("Prediction", "预测标签"), str(selected["predicted_name"]))
info_cols[4].metric(tr("Confidence", "置信度"), f'{float(selected["confidence"]):.2%}')

probabilities = json.loads(selected["probabilities_json"])
class_lookup = (
    dataset_trials[["class_index", "class_name"]]
    .drop_duplicates()
    .sort_values("class_index")
    .set_index("class_index")["class_name"]
    .to_dict()
)
prob_df = pd.DataFrame(
    [
        {
            tr("Class", "类别"): class_lookup.get(int(index), f"class {index}"),
            tr("Probability", "概率"): float(value),
        }
        for index, value in probabilities.items()
    ]
)

tab_trial, tab_forward, tab_coverage = st.tabs(
    [
        tr("Trial Visualizations", "样本可视化"),
        tr("Forward Pass", "前向传播"),
        tr("Coverage", "覆盖检查"),
    ]
)

with tab_trial:
    st.markdown(f"### {tr('Step 2: Input, Prediction, and Interpretation', '步骤 2：输入、预测与解释')}")
    st.markdown('<div class="demo-highlight">', unsafe_allow_html=True)
    show_visual_card(
        tr("Input EEG waveform", "输入 EEG 波形"),
        local_demo_path(selected["waveform_png"]),
        tr("Pre-rendered EEG waveform for the selected trial.", "所选 trial 的预渲染 EEG 波形。"),
        "#1768ac",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    image_cols = st.columns(2, gap="large")
    with image_cols[0]:
        show_visual_card(
            tr("Prediction probabilities", "预测概率"),
            local_demo_path(selected["probability_png"]),
            tr("Softmax probability plot; the selected sample is correctly predicted.", "Softmax 概率图；当前样本预测正确。"),
            "#16857a",
        )
    with image_cols[1]:
        show_visual_card(
            tr("Saliency / topomap", "Saliency / topomap"),
            local_demo_path(selected["saliency_png"]),
            tr("Gradient-based channel saliency or topomap visualization.", "基于梯度的通道 saliency 或 topomap 可视化。"),
            "#b24736",
        )

    st.write("")
    left, right = st.columns([1, 1], gap="large")
    with left:
        st.markdown(f"### {tr('Probability values', '概率数值')}")
        st.dataframe(
            prob_df.style.format({tr("Probability", "概率"): "{:.4%}"}),
            use_container_width=True,
            hide_index=True,
        )
    with right:
        st.markdown(f"### {tr('Sample package', '样本文件')}")
        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-body">
                    <b>{tr("NPZ file", "NPZ 文件")}</b><br/>
                    <span class="step-shape">{local_demo_path(selected["npz"])}</span><br/><br/>
                    {tr(
                        "The package contains the raw EEG array, labels, probabilities, channel saliency values, and channel names when available.",
                        "该样本包包含原始 EEG 数组、标签、概率、通道 saliency 数值，以及可用时的通道名称。"
                    )}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab_forward:
    st.markdown(f"### {tr('Step 3: Dataset-Specific Forward Pass', '步骤 3：数据集对应的前向传播')}")
    st.markdown(
        f"""
        <div class="soft-note">
            {tr(
                "Tensor shapes differ across datasets because channel counts and class counts differ. The table below is loaded from the exported forward_pass files.",
                "不同数据集的通道数和类别数不同，因此 tensor shape 也不同。下表直接读取导出的 forward_pass 文件。"
            )}
        </div>
        """,
        unsafe_allow_html=True,
    )
    shapes = load_forward_shapes(dataset)
    st.dataframe(shapes, use_container_width=True, hide_index=True)

    st.write("")
    st.markdown(f"### {tr('Module sequence', '模块顺序')}")
    steps = load_forward_steps(dataset)
    for step in steps:
        st.markdown(
            f"""
            <div class="step-box">
                <div class="step-name">{step["module"]}</div>
                <div class="step-shape">input: {step["input_shape"]} → output: {step["output_shape"]}</div>
                <div class="metric-text">{step["explain"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with tab_coverage:
    st.markdown(f"### {tr('Label Coverage Quality Check', '标签覆盖质量检查')}")
    st.markdown(
        f"""
        <div class="soft-note">
            {tr(
                "The exported materials include three correctly predicted trials for every label of each dataset.",
                "导出的材料为每个数据集的每个 label 都提供了 3 个预测正确的 trial。"
            )}
        </div>
        """,
        unsafe_allow_html=True,
    )
    coverage = load_label_coverage(dataset)
    st.dataframe(coverage, use_container_width=True, hide_index=True)

    st.write("")
    st.markdown(f"### {tr('All trials in this dataset', '该数据集中的全部 demo trial')}")
    display_cols = [
        "split",
        "trial_index",
        "class_name",
        "predicted_name",
        "is_correct",
        "confidence",
    ]
    st.dataframe(
        dataset_trials[display_cols].sort_values(["class_name", "trial_index"]),
        use_container_width=True,
        hide_index=True,
    )
