import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(layout="wide")
st.title("🎯 MiM 2026 Strategic Control Panel")

# ==========================================
# PROFILO
# ==========================================

st.sidebar.header("Profilo")

current_score = st.sidebar.number_input("GMAT attuale", 200, 805, 575)
target_score = st.sidebar.number_input("GMAT target", 200, 805, 720)
weekly_hours_total = st.sidebar.slider("Ore totali studio/settimana", 10, 60, 30)
gmat_ratio = st.sidebar.slider("Percentuale ore su GMAT", 50, 90, 70)

exam_month = st.sidebar.selectbox(
    "Mese tentativo ufficiale",
    ["Aprile 2026", "Maggio 2026"]
)

today = datetime(2026, 3, 3)
exam_dates = {
    "Aprile 2026": datetime(2026, 4, 25),
    "Maggio 2026": datetime(2026, 5, 20),
}
exam_date = exam_dates[exam_month]
weeks_left = max((exam_date - today).days // 7, 0)

gmat_hours = weekly_hours_total * (gmat_ratio / 100)
thesis_hours = weekly_hours_total - gmat_hours

st.sidebar.metric("Settimane disponibili", weeks_left)
st.sidebar.metric("Ore GMAT/settimana", int(gmat_hours))
st.sidebar.metric("Ore Tesi/settimana", int(thesis_hours))

# ==========================================
# MOCK TRACKER
# ==========================================

st.header("📊 Mock Tracker")

if "mock_scores" not in st.session_state:
    st.session_state.mock_scores = []

new_mock = st.number_input("Inserisci punteggio mock", 200, 805, step=5)

if st.button("Aggiungi Mock"):
    st.session_state.mock_scores.append(new_mock)

if st.session_state.mock_scores:
    df_mock = pd.DataFrame({
        "Tentativo": range(1, len(st.session_state.mock_scores) + 1),
        "Punteggio": st.session_state.mock_scores
    })

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_mock["Tentativo"],
        y=df_mock["Punteggio"],
        mode="lines+markers"
    ))
    fig.add_hline(y=target_score)
    st.plotly_chart(fig, use_container_width=True)

    real_growth = df_mock["Punteggio"].iloc[-1] - df_mock["Punteggio"].iloc[0]
    st.metric("Crescita reale", real_growth)

    current_projection = df_mock["Punteggio"].iloc[-1]
else:
    current_projection = current_score

# ==========================================
# SCUOLE TARGET
# ==========================================

st.header("🎓 Analisi Scuole 2026")

schools = [
    ["HEC Paris MiM", 705, "Round forte: Gen-Mar"],
    ["ESCP MiM", 690, "Round forte: Gen-Mar"],
    ["LBS MiM", 700, "Round forte: Gen-Feb"],
    ["Bocconi MiM", 680, "Round forte: Dic-Feb"],
    ["St. Gallen MiM", 695, "Round forte: Gen-Mar"],
]

df_schools = pd.DataFrame(
    schools,
    columns=["Programma", "GMAT Medio", "Periodo Forte"]
)

def admission_prob(predicted, avg):
    diff = predicted - avg
    if diff >= 20:
        return "Alta"
    elif diff >= 0:
        return "Media"
    elif diff >= -20:
        return "Bassa"
    else:
        return "Molto Bassa"

df_schools["Probabilità Stimata"] = df_schools["GMAT Medio"].apply(
    lambda x: admission_prob(current_projection, x)
)

st.dataframe(df_schools)

# ==========================================
# RISK ANALYSIS 2026
# ==========================================

st.header("⚠️ Analisi Rischio 2026")

if weeks_left <= 0:
    st.error("Tempo esaurito per 2026.")
elif current_projection < 650 and weeks_left < 6:
    st.warning("Alto rischio di non raggiungere 700 in tempo.")
elif current_projection >= 700:
    st.success("Sei competitivo per round centrali.")
else:
    st.info("Obiettivo realistico: 700 entro data esame.")

# ==========================================
# PIANO DINAMICO
# ==========================================

st.header("🗓 Piano Operativo Dinamico")

plan = []

for w in range(1, weeks_left + 1):
    if w <= weeks_left * 0.4:
        phase = "Fondamenta Verbal + Quant Core"
    elif w <= weeks_left * 0.8:
        phase = "Mixed Sets + Timing"
    else:
        phase = "Mock ufficiali + Revisione errori"
    plan.append([w, phase])

if plan:
    df_plan = pd.DataFrame(plan, columns=["Settimana", "Focus"])
    st.dataframe(df_plan)

# ==========================================
# DECISION ENGINE
# ==========================================

st.header("🧠 Decision Engine")

if current_projection >= 720:
    st.success("Strategia: Puntare forte su HEC + LBS per borse.")
elif current_projection >= 700:
    st.warning("Competitivo per ammissione, borse selettive.")
else:
    st.error("Considera piano 2027 per massimizzare borsa.")

st.markdown("---")
st.markdown("MiM Strategic Engine 2026")
