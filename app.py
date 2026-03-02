import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import date

# 1. Configurazione della Pagina
st.set_page_config(page_title="CEO ROADMAP 2026", layout="wide", page_icon="📈")

# 2. Stile Dark Mode "Bloomberg/McKinsey"
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stProgress > div > div > div > div { background-color: #00d4ff; }
    h1, h2, h3 { color: #00d4ff; font-family: 'Helvetica Neue', sans-serif; }
    .card { background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 CEO Roadmap 2026: Executive Dashboard")
st.write(f"**Data Odierna:** {date.today().strftime('%d %B %Y')} | **Status:** High Performance Mode")

# --- SIDEBAR: KPI RAPIDI ---
st.sidebar.header("📊 Key Performance Indicators")
st.sidebar.metric("GPA (Media)", "29.2/30")
st.sidebar.metric("GMAT Target", "645", "Current: 575")
st.sidebar.metric("Esami Mancanti", "3")

# --- LAYOUT PRINCIPALE ---
col1, col2 = st.columns([1.2, 1])

with col1:
    # SEZIONE GMAT
    st.subheader("📉 GMAT Focus Edition: Path to 645")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=['Cold Test', 'Target'], y=[575, 645],
                        mode='lines+markers', name='Progress',
                        line=dict(color='#00d4ff', width=4)))
    fig.update_layout(template="plotly_dark", height=300, margin=dict(l=20, r=20, t=20, b=20), yaxis=dict(range=[550, 670]))
    st.plotly_chart(fig, use_container_width=True)
    st.info("🎯 Focus: Potenziare la sezione **Verbal** (gap attuale: 47%)")

    # SEZIONE PIANIFICAZIONE SETTIMANALE
    st.subheader("📅 Weekly Executive Schedule")
    sched_data = {
        "Giorno": ["Lun", "Mar", "Mer", "Gio", "Ven", "Weekend"],
        "Focus": ["Deep Work (Tesi)", "Uni (Service)", "Uni (Full Day)", "Uni + Gym", "Lab + Gym", "GMAT Prep"],
        "Logistica": ["🏠 Home", "🚗 Audio-Learning", "🚗 Audio-Learning", "🚗 Audio-Learning", "🚗 Audio-Learning", "🏠 Home"],
        "Sport": ["🏋️ 18:00", "-", "-", "🏋️ 18:30", "🏋️ 18:30", "-"]
    }
    st.table(pd.DataFrame(sched_data))

with col2:
    # SEZIONE MASTER DEADLINES
    st.subheader("🎯 Master Application Funnel")
    masters = {
        "HEC Paris (MiM)": "09/04",
        "ESCP Business School": "07/05",
        "CEIBS Shanghai": "12/05",
        "Mannheim (MMM)": "15/05"
    }
    for m, d in masters.items():
        st.write(f"**{m}**")
        st.caption(f"Scadenza: {d}")
        st.progress(0.1) # Stato iniziale

    st.divider()

    # SEZIONE ACCADEMICA
    st.subheader("📚 Academic Milestones")
    st.write("Analisi & Scrittura Tesi")
    st.progress(0.4)
    
    st.checkbox("Strategic Management (Esame)")
    st.checkbox("Service Management (Esame)")
    st.checkbox("Laboratorio (Esame)")

# --- FOOTER ---
st.divider()
st.markdown("<center><i>'The best way to predict the future is to create it.'</i></center>", unsafe_allow_html=True)
