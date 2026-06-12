import streamlit as st
import pandas as pd
from pathlib import Path
import sys

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from utils import inject_css, init_lang_state, sidebar_language_switcher, tr, section_badge, highlight_dsai
from data_content import DATASETS, TABLE_II, TABLE_III, TABLE_IV, FIGURE_TITLES

st.set_page_config(page_title="Methods & Results | DSAINet", layout="wide")
inject_css()
init_lang_state()

asset_dir = Path(__file__).resolve().parents[1] / "assets"

with st.sidebar:
    sidebar_language_switcher()

section_badge("Benchmark & protocol", "测试结果与协议")
st.title(tr("Testing Method and Results", "测试方法与结果"))

st.markdown(
    f"""
    <div class="soft-note">
        {tr("This page presents comprehensive benchmark results across 10 public datasets and 5 EEG paradigms, along with detailed evaluation protocols and hyperparameter settings.", "本页呈现了跨 10 个公开数据集和 5 个 EEG 范式的综合基准结果，以及详细的评估协议和超参数设置。")}
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2, tab3 = st.tabs([
    tr("Main Results", "主要结果"),
    tr("Evaluation Setup", "评估设置"),
    tr("Supplementary Figures", "补充图"),
])

with tab1:
    st.markdown(f"### {tr('Table III — Motor imagery benchmarks', '表 III — 运动想象 benchmark')}")
    st.caption(tr(
        "Performance comparison on five motor imagery datasets using ACC (%) and weighted F1-score (%), reported as mean ± std.",
        "五个运动想象数据集上的性能比较，指标为 ACC (%) 与 weighted F1-score (%)，结果报告为 mean ± std。"
    ))
    col_names_3 = [
        "Method",
        "BCIC-IV-2a ACC","BCIC-IV-2a F1",
        "BCIC-IV-2b ACC","BCIC-IV-2b F1",
        "Zhou2016 ACC","Zhou2016 F1",
        "OpenBMI ACC","OpenBMI F1",
        "PhysioNet-MI ACC","PhysioNet-MI F1",
    ]
    df3 = pd.DataFrame(TABLE_III, columns=col_names_3)
    st.dataframe(df3.style.apply(highlight_dsai, axis=1), use_container_width=True, hide_index=True)

    st.write("")
    st.markdown(f"### {tr('Table IV — Other downstream EEG tasks', '表 IV — 其他下游 EEG 任务')}")
    st.caption(tr(
        "Performance comparison on five downstream EEG datasets using ACC (%) and weighted F1-score (%), reported as mean ± std.",
        "五个下游 EEG 数据集上的性能比较，指标为 ACC (%) 与 weighted F1-score (%)，结果报告为 mean ± std。"
    ))
    col_names_4 = [
        "Method",
        "Mumtaz2017 ACC","Mumtaz2017 F1",
        "ADFTD ACC","ADFTD F1",
        "Rockhill2021 ACC","Rockhill2021 F1",
        "EEGMat ACC","EEGMat F1",
        "Shin2018 ACC","Shin2018 F1",
    ]
    df4 = pd.DataFrame(TABLE_IV, columns=col_names_4)
    st.dataframe(df4.style.apply(highlight_dsai, axis=1), use_container_width=True, hide_index=True)

    st.write("")
    st.markdown(f"### {tr('Accuracy-efficiency comparison', '准确率-效率对比')}")
    st.image(str(asset_dir / "macs_param_physionet.png"), use_container_width=True)
    st.caption(
        tr(
            "ACC comparison with model complexity metrics on PhysioNet-MI.",
            "PhysioNet-MI 数据集上的 ACC 与模型复杂度指标对比。",
        )
    )

    st.write("")
    st.image(str(asset_dir / "tables_page.png"), use_container_width=True)
    st.caption(tr("Scanned page containing Table III and Table IV from the paper.", "论文中包含表 III 与表 IV 的原始页面。"))

with tab2:
    st.markdown(f"### {tr('Dataset summary (Table I content)', '数据集汇总（表 I 内容）')}")
    ds_df = pd.DataFrame(DATASETS)
    show_df = ds_df.drop(columns=["Link"])
    st.dataframe(show_df, use_container_width=True, hide_index=True)

    st.write("")
    st.markdown(f"### {tr('Dataset download links', '数据集下载链接')}")
    for row in DATASETS:
        with st.expander(f'{row["Dataset"]} — {row["Paradigm"]}'):
            st.markdown(f"**{tr('Task types', '任务类型')}**: {row['Task Types']}")
            st.link_button(tr("Open dataset page", "打开数据集页面"), row["Link"])

    st.write("")
    left, right = st.columns([1, 1], gap="large")
    with left:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-title">{tr("Evaluation protocol", "评估协议")}</div>
                <div class="section-body">
                    • {tr("Subject-independent evaluation only", "仅采用跨受试者评估")}<br/>
                    • {tr("LOSO for BCIC-IV-2a / BCIC-IV-2b / Zhou2016", "BCIC-IV-2a / BCIC-IV-2b / Zhou2016 使用 LOSO")}<br/>
                    • {tr("Subject-level k-fold cross-validation for the remaining datasets", "其余数据集使用受试者级 k 折交叉验证")}<br/>
                    • {tr("For each run, the checkpoint with the best validation performance is used for final testing", "每次实验都用验证集表现最好的 checkpoint 在测试集上评估")}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-title">{tr("Training configurations (Table II)", "训练配置（表 II）")}</div>
                <div class="section-body">
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        df2 = pd.DataFrame(TABLE_II, columns=[tr("Dataset","数据集"), "Batch", "LR", tr("Epochs","轮数"), tr("Protocol","协议")])
        st.dataframe(df2, use_container_width=True, hide_index=True)

with tab3:
    st.markdown(f"### {tr('Figure titles from the paper', '论文中的图标题')}")
    for fig_no, title in FIGURE_TITLES:
        st.markdown(f"**{fig_no}** — {title}")

    st.write("")
    st.markdown(f"### {tr('Figures 3–5', '图 3–5')}")
    st.image(str(asset_dir / "fig3_45_page.png"), use_container_width=True)
    st.caption(tr(
        "This cropped paper page contains Fig. 3 (hyperparameter sensitivity), Fig. 4 (segment length), and Fig. 5 (accuracy–efficiency trade-off).",
        "这张裁剪后的论文图片包含图 3（超参数敏感性）、图 4（segment length）和图 5（精度-效率权衡）。"
    ))

    st.write("")
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.image(str(asset_dir / "fig6_saliency.png"), use_container_width=True)
        st.caption("Fig. 6 — Mean saliency maps.")
    with c2:
        st.image(str(asset_dir / "fig7_attention.png"), use_container_width=True)
        st.caption("Fig. 7 — Learned attention patterns.")
