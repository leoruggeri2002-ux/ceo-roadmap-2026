import streamlit as st

def render_decision_model():
    st.header("🎯 Decision Simulator")

    target_score = st.slider("Your Expected GMAT",500,800,650)
    school_avg = st.slider("School Average GMAT",500,800,680)

    diff = target_score - school_avg

    if diff >= 30:
        st.success("High Competitiveness")
    elif diff >= 0:
        st.warning("Competitive but risky")
    else:
        st.error("Low competitiveness")
