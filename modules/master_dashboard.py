import streamlit as st
import pandas as pd
from datetime import datetime

def render_master_dashboard():
    st.header("🌍 Master Programs & Deadlines")

    if "programs" not in st.session_state:
        st.session_state.programs = pd.DataFrame(columns=[
            "School","Country","Round",
            "App Deadline","Scholarship Deadline",
            "Avg GMAT","Tuition","Status"
        ])

    with st.form("add_program"):
        school = st.text_input("School")
        country = st.selectbox("Country", ["France","Germany","USA","China","Other"])
        round_ = st.text_input("Round")
        app_dead = st.date_input("Application Deadline")
        schol_dead = st.date_input("Scholarship Deadline")
        avg_gmat = st.number_input("Average GMAT", 500, 800, 650)
        tuition = st.number_input("Tuition (€/$)", 0, 200000, 30000)
        status = st.selectbox("Status", ["Researching","Preparing","Submitted","Admitted"])

        submitted = st.form_submit_button("Add Program")

        if submitted:
            new = pd.DataFrame([[school,country,round_,
                                 app_dead,schol_dead,
                                 avg_gmat,tuition,status]],
                               columns=st.session_state.programs.columns)
            st.session_state.programs = pd.concat(
                [st.session_state.programs,new], ignore_index=True
            )

    if not st.session_state.programs.empty:
        df = st.session_state.programs.copy()
        df["Days to App"] = (pd.to_datetime(df["App Deadline"]) - datetime.now()).dt.days
        df["Days to Scholarship"] = (pd.to_datetime(df["Scholarship Deadline"]) - datetime.now()).dt.days
        st.dataframe(df)
