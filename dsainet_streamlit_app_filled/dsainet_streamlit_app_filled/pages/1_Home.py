import streamlit as st
from pathlib import Path
import sys

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from utils import inject_css, init_lang_state, sidebar_language_switcher, tr, section_badge
from data_content import VALUE_CLAIM_EN, VALUE_CLAIM_ZH, MODEL_SUMMARY_EN, MODEL_SUMMARY_ZH, HOME_METRICS

st.set_page_config(page_title="Home | DSAINet", layout="wide")
inject_css()
init_lang_state()

asset_dir = Path(__file__).resolve().parents[1] / "assets"

with st.sidebar:
    sidebar_language_switcher()

section_badge("Home Page / Project Overview", "首页 / 项目概览")
st.title(tr("General EEG Decoding with DSAINet", "基于 DSAINet 的通用 EEG 解码"))

st.markdown(
    f"""
    <div class="hero-card">
        <div class="hero-title">{tr("A unified, lightweight, cross-subject EEG decoder", "一个统一、轻量、跨受试者的 EEG 解码器")}</div>
        <div class="hero-subtitle">{tr(VALUE_CLAIM_EN, VALUE_CLAIM_ZH)}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
cols = st.columns(4, gap="medium")
for col, (value, en_label, zh_label) in zip(cols, HOME_METRICS):
    with col:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-title">{tr(en_label, zh_label)}</div>
                <div class="metric-big">{value}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
c1, c2, c3 = st.columns(3, gap="large")
with c1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{tr("Problem", "问题")}</div>
            <div class="metric-text">
                {tr("EEG decoding is hard because signals are noisy, vary strongly across subjects, and carry task-relevant information at multiple temporal scales.", "EEG 解码之所以困难，是因为信号噪声大、跨受试者差异显著，而且任务相关信息分布在多个时间尺度上。")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    chips = "".join([f'<span class="chip">{x}</span>' for x in ["Tokenizer","Dual-Scale Conv","Intra-Attn","Inter-Attn","Adaptive Pooling"]])
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{tr("Model", "模型")}</div>
            <div class="metric-text">
                {tr("DSAINet constructs shared spatiotemporal tokens, models fine/coarse temporal patterns in parallel, then refines and integrates them with structured attention.", "DSAINet 先构造共享时空 token，再并行建模细粒度/粗粒度时间模式，并通过结构化注意力完成精炼与整合。")}
                <br/><br/>{chips}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{tr("Results", "结果")}</div>
            <div class="metric-text">
                {tr("Across five paradigms and ten public datasets, DSAINet reports the best ACC and weighted F1-score under subject-independent evaluation, while keeping a favorable accuracy–efficiency trade-off.", "在五类范式、十个公开数据集上，DSAINet 在跨受试者评估中取得了最优 ACC 与 weighted F1，同时保持了较好的精度-效率平衡。")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

st.markdown(f"### {tr('General EEG decoding workflow', '通用 EEG 解码流程')}")
st.image(str(asset_dir / "fig1_overview.png"), use_container_width=True)
st.caption(
    tr(
        "Fig. 1. Overview of the general EEG decoding setting used in this project.",
        "图 1. 本项目中通用 EEG 解码任务设置的整体示意图。",
    )
)

st.write("")

# 突出显示的 Demo 按钮
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; margin: 2rem 0;">
        <div style="
            background: linear-gradient(135deg, #6670d8 0%, #5f88df 100%);
            border-radius: 50px;
            padding: 2rem 3rem;
            box-shadow: 0 20px 50px rgba(102, 112, 216, 0.3);
            text-align: center;
            max-width: 600px;
        ">
            <div style="
                font-size: 2.2rem;
                font-weight: 900;
                color: white;
                margin-bottom: 0.8rem;
                letter-spacing: 0.5px;
            ">{tr("🚀 TRY THE INTERACTIVE DEMO", "🚀 尝试交互式 DEMO")}</div>
            <div style="
                font-size: 1rem;
                color: rgba(255, 255, 255, 0.95);
                line-height: 1.6;
                margin-bottom: 1.5rem;
            ">
                {tr("Explore DSAINet with real-world EEG data. See predictions, saliency maps, and ablation results instantly.", "用真实脑电数据探索 DSAINet。即时查看预测结果、saliency map 和消融实验对比。")}
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button(tr("LAUNCH DEMO", "启动 DEMO"), use_container_width=True, help=tr("Click to explore the interactive demo", "点击进入交互式演示")):
        st.switch_page("pages/3_Demo.py")

st.write("")
left, right = st.columns([1.05, 0.95], gap="large")
with left:
    st.markdown(
        f"""
        <div class="cta-box">
            <div class="metric-title" style="color:white;">{tr("Why Try the Demo?", "为什么试试 Demo？")}</div>
            <div class="section-body" style="color:white;">
                ✓ {tr("See real predictions on multiple datasets", "在多个数据集上查看真实预测")}<br/>
                ✓ {tr("Visualize which brain regions matter most", "可视化最重要的脑区")}<br/>
                ✓ {tr("Compare full model vs. ablated variants", "对比完整模型与消融模型")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">{tr("Model structure summary", "模型结构摘要")}</div>
            <div class="section-body">
                {"<br/>".join([f"• {tr(en, zh)}" for en, zh in zip(MODEL_SUMMARY_EN, MODEL_SUMMARY_ZH)])}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.markdown(f"### {tr('Architecture figure from the paper', '论文中的模型结构图')}")
st.image(str(asset_dir / "fig2_architecture.png"), use_container_width=True)
st.caption(
    tr(
        "Fig. 2. Overall architecture of DSAINet: shared spatiotemporal tokenization → fine/coarse temporal convolution → intra-branch attentive refinement → inter-branch attentive interaction → adaptive token aggregation → classification.",
        "图 2：DSAINet 的整体结构：共享时空 token 化 → 细/粗粒度时间卷积 → 分支内注意力精炼 → 分支间注意力交互 → 自适应 token 聚合 → 分类。",
    )
)
