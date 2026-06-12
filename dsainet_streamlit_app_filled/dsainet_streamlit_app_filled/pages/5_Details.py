import streamlit as st
import pandas as pd
from pathlib import Path
import sys

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from utils import inject_css, init_lang_state, sidebar_language_switcher, tr, section_badge, highlight_dsai
from data_content import TABLE_V, KEY_REF_ROWS

st.set_page_config(page_title="Details | DSAINet", layout="wide")
inject_css()
init_lang_state()

with st.sidebar:
    sidebar_language_switcher()

section_badge("More details", "更多细节")
st.title(tr("Supplementary Details", "补充细节"))

st.markdown(
    f"""
    <div class="soft-note">
        {tr("Find detailed hyperparameters, ablation studies, and key references below.", "在下方找到详细的超参数、消融实验和关键参考文献。")}
    </div>
    """,
    unsafe_allow_html=True,
)

tab1, tab2, tab3 = st.tabs([
    tr("Architecture & Hyperparameters", "结构与超参数"),
    tr("Ablation", "消融实验"),
    tr("Key References", "关键参考文献"),
])

with tab1:
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-title">{tr("Architecture-related hyperparameters fixed across datasets", "跨数据集固定的架构相关超参数")}</div>
            <div class="section-body">
                • {tr("Embedding dimension: 40", "嵌入维度：40")}<br/>
                • {tr("Attention heads: 4", "注意力头数：4")}<br/>
                • {tr("Tokenizer f1: 16", "Tokenizer 中的 f1：16")}<br/>
                • {tr("Tokenizer temporal kernel sizes: 64 and 16", "Tokenizer 时间卷积核大小：64 和 16")}<br/>
                • {tr("Depth multiplier D: 2", "深度乘子 D：2")}<br/>
                • {tr("Pooling sizes: 4 and 8", "池化大小：4 和 8")}<br/>
                • {tr("Coarse branch kernel sizes: 11 and 15", "粗粒度分支卷积核：11 和 15")}<br/>
                • {tr("Fine branch kernel sizes: 3 and 7", "细粒度分支卷积核：3 和 7")}<br/>
                • {tr("Convolution expansion ratio: 4", "卷积扩展倍率：4")}<br/>
                • {tr("Feed-forward expansion ratio: 2", "前馈层扩展倍率：2")}<br/>
                • {tr("Dropout: 0.25", "Dropout：0.25")}<br/>
                • {tr("Optimizer: Adam, weight decay = 1×10⁻⁴", "优化器：Adam，weight decay = 1×10⁻⁴")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with tab2:
    st.markdown(f"### {tr('Table V — Ablation study', '表 V — 消融实验')}")
    st.caption(tr(
        "Ablation study of DSAINet on three representative tasks using ACC (%), reported as mean ± std.",
        "在三个代表性任务上的 DSAINet 消融实验，指标为 ACC (%)，结果报告为 mean ± std。"
    ))
    df = pd.DataFrame(TABLE_V, columns=[tr("Model Variant","模型变体"), "BCIC-IV-2a", "BCIC-IV-2b", "ADFTD"])
    st.dataframe(df.style.apply(highlight_dsai, axis=1), use_container_width=True, hide_index=True)

    st.markdown(
        f"""
        <div class="soft-note">
            {tr("The full model performs best, showing that the gains come from component synergy rather than from a single design choice alone.", "完整模型表现最好，说明增益来自各组件协同作用，而不是某一个单独设计带来的。")}
        </div>
        """,
        unsafe_allow_html=True,
    )

with tab3:
    ref_df = pd.DataFrame(KEY_REF_ROWS, columns=[tr("Model / Paper","模型 / 论文"), tr("Citation","引用"), tr("Why it matters","意义")])
    st.dataframe(ref_df, use_container_width=True, hide_index=True)

    st.markdown(
        f"""
        <div class="soft-note">
            {tr("You can still add a full reference list later if you want this page to look more paper-like. Right now it keeps only the most relevant methods around DSAINet.", "如果你希望这一页更像论文附录，后续还可以补全完整参考文献列表。当前版本先保留了与 DSAINet 最相关的方法。")}
        </div>
        """,
        unsafe_allow_html=True,
    )
