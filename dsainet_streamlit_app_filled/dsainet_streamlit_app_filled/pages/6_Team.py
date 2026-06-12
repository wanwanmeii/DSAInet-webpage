from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from data_content import TEAM
from utils import inject_css, init_lang_state, sidebar_language_switcher, tr, section_badge


st.set_page_config(page_title="Team | DSAINet", layout="wide")
inject_css()
init_lang_state()

asset_dir = Path(__file__).resolve().parents[1] / "assets"
teammate_dir = asset_dir / "teammates"

st.markdown(
    """
    <style>
    .team-intro{
        border:1px solid #dbe3e8;
        border-radius:8px;
        padding:1.05rem 1.15rem;
        background:linear-gradient(135deg,#ffffff 0%,#f6fbff 62%,#f5fbf8 100%);
        box-shadow:0 12px 30px rgba(23,32,38,.07);
        margin-bottom:1rem;
    }
    .team-row-title{
        font-size:1.28rem;
        font-weight:900;
        color:#172026;
        line-height:1.25;
        margin:.25rem 0 .25rem 0;
    }
    .team-row-subtitle{
        color:#1768ac;
        font-size:1.02rem;
        font-weight:850;
        margin-bottom:.55rem;
    }
    .team-row-body{
        color:#5f6b73;
        font-size:.98rem;
        line-height:1.65;
    }
    .team-detail-line{
        margin:.12rem 0;
    }
    .team-detail-label{
        color:#31424c;
        font-weight:850;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    sidebar_language_switcher()

section_badge("Team", "团队")
st.title(tr("Our Team", "我们的团队"))

st.markdown(
    f"""
    <div class="team-intro">
        <div class="section-title">{tr("DSAINet Research Team", "DSAINet 研究团队")}</div>
        <div class="section-body">
            {tr(
                "This project represents collaborative research across model design, comprehensive evaluation, visualization, web demo development, and presentation preparation.",
                "本项目汇集了模型设计、综合评估、可视化、网页 demo 制作和展示材料准备等多方面协作。"
            )}
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

photo_ext = {
    "李泽元": "jpg",
    "邱子浩": "jpg",
    "张琬梅": "jpg",
    "王榕": "jpg",
    "杜又郎": "png",
}

for index, member in enumerate(TEAM, start=1):
    zh_name, en_name, zh_role, en_role, *extra = member
    details = extra[0] if extra else []
    detail_html = "".join(
        (
            '<div class="team-detail-line">'
            f'<span class="team-detail-label">{tr(en_label, zh_label)}:</span> '
            f"{tr(en_value, zh_value)}"
            "</div>"
        )
        for zh_label, en_label, zh_value, en_value in details
    )
    if not detail_html:
        detail_html = tr(
            "Contribution area for this DSAINet project.",
            "该成员在 DSAINet 项目中的主要负责方向。"
        )

    with st.container(border=True):
        photo_col, text_col = st.columns([0.22, 0.78], gap="large")
        photo_path = teammate_dir / f"{zh_name}.{photo_ext[zh_name]}"

        with photo_col:
            if photo_path.exists():
                st.image(str(photo_path), use_container_width=True)
            else:
                st.warning(f"Missing photo: {photo_path.name}")

        with text_col:
            st.markdown(f'<div class="team-row-title">{zh_name} / {en_name}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="team-row-subtitle">{tr(en_role, zh_role)}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="team-row-body">{detail_html}</div>', unsafe_allow_html=True)
