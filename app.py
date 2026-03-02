import streamlit as st
from modules.master_dashboard import render_master_dashboard
from modules.gmat_engine import render_gmat_engine
from modules.thesis_tracker import render_thesis_tracker
from modules.weekly_planner import render_weekly_planner
from modules.decision_model import render_decision_model

st.set_page_config(page_title="MASTER EXECUTION SYSTEM", layout="wide")

st.title("🎯 MASTER EXECUTION SYSTEM")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Master Dashboard",
        "GMAT Analytics",
        "Thesis Tracker",
        "Weekly Planner",
        "Decision Simulator"
    ]
)

if menu == "Master Dashboard":
    render_master_dashboard()

elif menu == "GMAT Analytics":
    render_gmat_engine()

elif menu == "Thesis Tracker":
    render_thesis_tracker()

elif menu == "Weekly Planner":
    render_weekly_planner()

elif menu == "Decision Simulator":
    render_decision_model()
