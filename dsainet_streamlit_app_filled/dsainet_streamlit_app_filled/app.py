from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

pages = [
    st.Page("pages/1_Home.py", title="Home"),
    st.Page("pages/2_Background.py", title="Background"),
    st.Page("pages/3_Demo.py", title="Demo"),
    st.Page("pages/4_Methods_Results.py", title="Methods & Results"),
    st.Page("pages/5_Details.py", title="Details"),
    st.Page("pages/6_Team.py", title="Team"),
]

st.navigation(pages).run()
