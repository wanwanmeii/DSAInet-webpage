from __future__ import annotations

import re

import streamlit as st

EN = "English"
ZH = "中文"


def init_lang_state() -> None:
    if "lang" not in st.session_state:
        st.session_state["lang"] = EN


def tr(en: str, zh: str) -> str:
    return zh if st.session_state.get("lang", EN) == ZH else en


def sidebar_language_switcher() -> None:
    choice = st.radio(
        "Language / 语言",
        [EN, ZH],
        index=0 if st.session_state.get("lang", EN) == EN else 1,
        horizontal=True,
    )
    st.session_state["lang"] = choice


def section_badge(en: str, zh: str) -> None:
    st.markdown(f'<div class="small-badge">{tr(en, zh)}</div>', unsafe_allow_html=True)


def inject_css() -> None:
    st.markdown(
        """
        <style>
        :root{
            --bg:#f6f8fb;
            --card:#ffffff;
            --text:#172026;
            --muted:#5f6b73;
            --primary:#1768ac;
            --primary-soft:#e9f3fb;
            --accent:#16857a;
            --accent-soft:#e9f7f5;
            --warn:#a56b00;
            --border:#dbe3e8;
            --shadow:0 14px 34px rgba(23,32,38,.08);
        }
        .stApp{background:linear-gradient(180deg,#ffffff 0%,var(--bg) 100%);}
        .block-container{padding-top:2rem;padding-bottom:4rem;}
        .hero-card,.section-card,.metric-card,.member-card,.media-card{
            background:var(--card);
            border:1px solid var(--border);
            border-radius:8px;
            box-shadow:var(--shadow);
        }
        .hero-card{padding:1.6rem 1.7rem;background:linear-gradient(135deg,#ffffff 0%,#eef6fb 100%);}
        .section-card,.metric-card,.member-card,.media-card{padding:1rem 1.1rem;}
        .cta-box{padding:1.35rem 1.45rem;border-radius:8px;background:linear-gradient(135deg,#1768ac 0%,#16857a 100%);color:white;box-shadow:var(--shadow);}
        .hero-title{font-size:2.15rem;font-weight:850;color:var(--text);line-height:1.18;margin-bottom:.55rem;}
        .hero-subtitle{font-size:1.04rem;color:var(--muted);line-height:1.72;}
        .metric-title,.section-title{font-size:1.05rem;font-weight:800;color:var(--text);margin-bottom:.4rem;}
        .metric-text,.section-body{font-size:.96rem;color:var(--muted);line-height:1.7;}
        .small-badge{
            display:inline-block;padding:.32rem .72rem;border-radius:999px;background:var(--primary-soft);
            color:var(--primary);font-weight:800;font-size:.88rem;margin-bottom:.7rem;
        }
        .soft-note{
            font-size:.94rem;color:#56636d;background:#fbfdff;border:1px solid var(--border);
            border-radius:8px;padding:.9rem 1rem;line-height:1.65;
        }
        .chip{
            display:inline-block;padding:.34rem .68rem;border-radius:999px;background:var(--accent-soft);
            color:#126b62;font-size:.86rem;font-weight:700;margin-right:.34rem;margin-bottom:.34rem;
        }
        .metric-big{font-size:1.7rem;font-weight:850;color:var(--primary);line-height:1.08;margin-top:.25rem;}
        div[data-testid="stButton"] > button {
            border-radius:6px;border:none;padding:.72rem 1.2rem;font-weight:800;
            background:linear-gradient(135deg,#1768ac 0%,#16857a 100%);color:white;
        }
        div[data-testid="stLinkButton"] > a {border-radius:6px;font-weight:800;}
        .member-name{font-size:1.08rem;font-weight:850;margin-bottom:.15rem;color:var(--text);}
        .member-role{font-size:.92rem;color:var(--primary);font-weight:800;margin-bottom:.45rem;}
        .member-text{color:var(--muted);line-height:1.65;font-size:.94rem;}
        .table-title{font-size:1rem;font-weight:850;color:var(--text);margin:.2rem 0 .5rem 0;}
        .step-box{border:1px solid var(--border);border-radius:8px;padding:.75rem;background:#fbfdff;margin-bottom:.45rem;}
        .step-name{font-weight:850;color:var(--text);}
        .step-shape{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;color:var(--primary);font-size:.84rem;}
        .footer-note{color:var(--muted);font-size:.86rem;line-height:1.6;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def highlight_dsai(row):
    name = str(row.iloc[0]) if len(row) else ""
    if "DSAINet" in name:
        return ["background-color: #e9f7f5; font-weight: 800;" for _ in row]
    return ["" for _ in row]


def parse_metric(value: object) -> float:
    match = re.search(r"\d+(?:\.\d+)?", str(value))
    return float(match.group(0)) if match else float("-inf")


def highlight_best_and_dsai(df):
    best = {
        col: df[col].map(parse_metric).max()
        for col in df.columns
        if col != "Method"
    }

    def style(row):
        styles = []
        is_ours = "DSAINet" in str(row.iloc[0])
        for col, value in row.items():
            item = []
            if is_ours:
                item.append("background-color: #e9f7f5")
                item.append("font-weight: 800")
            if col in best and abs(parse_metric(value) - best[col]) < 1e-9:
                item.append("color: #b24736")
                item.append("font-weight: 900")
            styles.append("; ".join(item))
        return styles

    return df.style.apply(style, axis=1)
