import streamlit as st
import pandas as pd

def render_thesis_tracker():
    st.header("📚 Thesis Tracker")

    if "thesis" not in st.session_state:
        st.session_state.thesis = pd.DataFrame(
            columns=["Milestone","Target Words","Completed Words"]
        )

    with st.form("add_milestone"):
        name = st.text_input("Milestone")
        target = st.number_input("Target Words",0,50000,2000)
        completed = st.number_input("Completed Words",0,50000,0)
        submitted = st.form_submit_button("Add")

        if submitted:
            new = pd.DataFrame([[name,target,completed]],
                               columns=st.session_state.thesis.columns)
            st.session_state.thesis = pd.concat(
                [st.session_state.thesis,new], ignore_index=True
            )

    if not st.session_state.thesis.empty:
        st.dataframe(st.session_state.thesis)
        total_target = st.session_state.thesis["Target Words"].sum()
        total_completed = st.session_state.thesis["Completed Words"].sum()
        progress = total_completed / total_target if total_target > 0 else 0
        st.progress(progress)
