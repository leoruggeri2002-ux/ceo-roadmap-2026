import streamlit as st
import pandas as pd
import plotly.express as px

def render_gmat_engine():
    st.header("📊 GMAT Analytics")

    if "gmat_log" not in st.session_state:
        st.session_state.gmat_log = pd.DataFrame(
            columns=["Date","Verbal","Quant","DI","Total"]
        )

    with st.form("add_score"):
        date = st.date_input("Date")
        v = st.number_input("Verbal",0,90)
        q = st.number_input("Quant",0,90)
        di = st.number_input("DI",0,90)
        submitted = st.form_submit_button("Add Score")

        if submitted:
            total = v+q+di
            new = pd.DataFrame([[date,v,q,di,total]],
                               columns=st.session_state.gmat_log.columns)
            st.session_state.gmat_log = pd.concat(
                [st.session_state.gmat_log,new], ignore_index=True
            )

    if not st.session_state.gmat_log.empty:
        fig = px.line(st.session_state.gmat_log,
                      x="Date", y="Total",
                      markers=True)
        st.plotly_chart(fig)

        avg = st.session_state.gmat_log["Total"].mean()
        st.metric("Average Score", round(avg,1))
