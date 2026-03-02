import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# --- CONFIGURAZIONE MOBILE-FIRST ---
st.set_page_config(page_title="CEO 2026", layout="centered", page_icon="📈")

# CSS per ottimizzazione iPhone & Look McKinsey/Bloomberg
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    [data-testid="stMetricValue"] { font-size: 1.8rem !important; color: #00d4ff !important; }
    .stProgress > div > div > div > div { background-color: #00d4ff; }
    .st-emotion-cache-1kyxreq { justify-content: center; }
    /* Arrotondamento card */
    div.stButton > button { width: 100%; border-radius: 10px; border: 1px solid #00d4ff; background-color: #161b22; color: white; }
    /* Mobile optimization */
    @media (max-width: 640px) {
        .main { padding: 10px !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER STATS ---
st.title("🏦 CEO COMMAND 2026")
col_gpa, col_gmat = st.columns(2)
col_gpa.metric("GPA", "29.2", "Top Tier")
col_gmat.metric("GMAT", "575", "Target: 645")

st.divider()

# --- 1. OPERATIONAL SCHEDULE (MOBILE SELECTOR) ---
st.header("📅 Daily Operations")
day = st.selectbox("Seleziona Giorno", ["LUN (Home)", "MAR (Uni PM)", "MER (Full Uni)", "GIO (Uni AM)", "VEN (Uni PM)", "SAB (GMAT)"])

# Dizionario Orari Dettagliato
schedules = {
    "LUN (Home)": [("08:00", "GMAT Verbal"), ("09:00", "GMAT Verbal"), ("10:00", "TESI: Progetto"), ("11:00", "TESI: Progetto"), ("13:00", "Master Admin"), ("14:00", "Progetto Strat."), ("16:00", "Progetto Lab"), ("18:00", "🏋️ PALESTRA")],
    "MAR (Uni PM)": [("08:00", "GMAT Quant"), ("09:00", "TESI: Scrittura"), ("11:00", "GMAT Quant"), ("12:00", "🚗 Audio-Learning"), ("14:00", "🏛️ SERVICE MANAGEMENT"), ("18:00", "🏠 Viaggio Home")],
    "MER (Full Uni)": [("08:00", "🚗 Audio-Learning"), ("09:00", "🏛️ STRATEGIC MGMT"), ("14:00", "🏛️ LABORATORIO"), ("16:00", "Progetto Lab"), ("18:00", "🏠 Viaggio Home")],
    "GIO (Uni AM)": [("08:00", "GMAT Verbal"), ("09:00", "🚗 Audio-Learning"), ("10:00", "🏛️ SERVICE MANAGEMENT"), ("12:00", "Studio Uni"), ("14:00", "Progetto Service"), ("16:00", "Progetto Strat."), ("18:00", "🏋️ PALESTRA")],
    "VEN (Uni PM)": [("08:00", "GMAT Quant"), ("09:00", "TESI: Scrittura"), ("10:00", "TESI: Progetto"), ("12:00", "🚗 Audio-Learning"), ("14:00", "🏛️ LABORATORIO"), ("16:00", "Progetto Lab"), ("18:00", "🏋️ PALESTRA")],
    "SAB (GMAT)": [("08:00", "📝 SIMULAZIONE"), ("10:00", "🧠 GMAT FOCUS (2h15)"), ("11:00", "🔍 Revisione"), ("13:00", "Master Research"), ("14:00", "Progetto Lab")]
}

for time, task in schedules[day]:
    st.markdown(f"**{time}** | {task}")

st.divider()

# --- 2. THESIS & EXAM MILESTONES (ULTRA-GRANULAR) ---
st.header("🔬 Execution Milestones")

with st.expander("🎓 TESI MAGISTRALE", expanded=True):
    st.write("**Fase 1: Progetto & Analisi Dati**")
    st.progress(45)
    st.write("**Fase 2: Scrittura Capitoli**")
    st.progress(15)
    st.caption("Prossimo Goal: Concludere analisi quantitativa entro fine mese.")

with st.expander("📚 PROGETTI ESAME"):
    st.write("**Strategic Mgmt** (Analisi Competitiva)")
    st.progress(30)
    st.write("**Service Mgmt** (Modellazione Processi)")
    st.progress(60)
    st.write("**Laboratorio** (Sviluppo Prototipo)")
    st.progress(10)

st.divider()

# --- 3. MASTER FUNNEL & DEADLINES ---
st.header("🏛️ Target Business Schools")
targets = [
    {"B": "HEC Paris", "D": "09/04", "P": 25, "Borsa": "Excellence"},
    {"B": "Mannheim", "D": "15/05", "P": 10, "Borsa": "Standard"},
    {"B": "ESCP", "D": "07/05", "P": 15, "Borsa": "Merit"},
]

for t in targets:
    st.markdown(f"**{t['B']}** (Scadenza: {t['D']})")
    st.progress(t['P'])
    st.caption(f"Target Borsa: {t['Borsa']}")

st.divider()

# --- 4. GMAT RADAR (PERFORMANCE ANALYSIS) ---
st.header("🎯 GMAT Analysis")
categories = ['Quant', 'Verbal', 'DI']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=[79, 79, 78], theta=categories, fill='toself', name='Current', line_color='#30363d'))
fig.add_trace(go.Scatterpolar(r=[85, 84, 82], theta=categories, fill='toself', name='Target', line_color='#00d4ff'))
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[70, 90])), template="plotly_dark", height=300, margin=dict(l=40, r=40, t=20, b=20), showlegend=False)
st.plotly_chart(fig, use_container_width=True)

st.markdown("<center><i>CEO ROADMAP v4.0 - PRIVATE SYSTEM</i></center>", unsafe_allow_html=True)
