import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="CEO Roadmap 2026 - Strategic Edition", layout="wide")

st.title("🎯 CEO Roadmap 2026 – Strategic MBA Engine")

# =========================
# SIDEBAR – PROFILO
# =========================

st.sidebar.header("📊 Profilo")

current_gmat = st.sidebar.number_input("GMAT attuale", value=575)
target_gmat = st.sidebar.number_input("GMAT target", value=730)
study_hours = st.sidebar.slider("Ore studio/settimana", 5, 40, 20)

post_mba_salary = st.sidebar.number_input("Stipendio atteso post-MBA (€)", value=110000)
current_salary = st.sidebar.number_input("Stipendio attuale (€)", value=30000)

country_filter = st.sidebar.multiselect(
    "Paesi target",
    ["USA", "Germany", "China"],
    default=["USA", "Germany"]
)

# =========================
# DATABASE MASTER (Strategic)
# =========================

master_data = [
    ["Harvard MBA", "USA", 730, 75000, "Round 1: Sept 2026", 150000],
    ["Stanford MBA", "USA", 735, 80000, "Round 1: Sept 2026", 155000],
    ["MIT Sloan", "USA", 720, 70000, "Round 1: Sept 2026", 145000],
    ["WHU MBA", "Germany", 650, 30000, "June 2026", 65000],
    ["Mannheim MBA", "Germany", 640, 25000, "May 2026", 60000],
    ["Tsinghua MBA", "China", 680, 35000, "May 2026", 80000],
]

df = pd.DataFrame(master_data, columns=[
    "Program", "Country", "Avg GMAT", "Avg Scholarship €",
    "Deadline", "Tuition €"
])

if country_filter:
    df = df[df["Country"].isin(country_filter)]

# =========================
# SIMULAZIONE GMAT NON LINEARE
# =========================

st.header("📈 Simulazione Crescita GMAT")

weeks = 24
growth_curve = []

score = current_gmat
for w in range(weeks):
    improvement = (target_gmat - score) * 0.12 * (study_hours / 20)
    score += improvement
    growth_curve.append(score)

growth_df = pd.DataFrame({
    "Week": range(1, weeks + 1),
    "Projected GMAT": growth_curve
})

fig = px.line(growth_df, x="Week", y="Projected GMAT",
              title="GMAT Growth Simulation (Diminishing Returns)")
st.plotly_chart(fig, use_container_width=True)

predicted_final = int(growth_curve[-1])
st.metric("GMAT previsto tra 6 mesi", predicted_final)

# =========================
# PROBABILITÀ AMMISSIONE
# =========================

st.header("🎓 Probabilità Ammissione")

def admission_probability(predicted, avg):
    diff = predicted - avg
    if diff >= 30:
        return 0.65
    elif diff >= 0:
        return 0.4
    elif diff >= -30:
        return 0.2
    else:
        return 0.08

df["Admission Probability"] = df["Avg GMAT"].apply(
    lambda x: admission_probability(predicted_final, x)
)

# =========================
# PROBABILITÀ BORSA
# =========================

def scholarship_probability(predicted, avg):
    diff = predicted - avg
    if diff >= 40:
        return 0.5
    elif diff >= 20:
        return 0.35
    elif diff >= 0:
        return 0.2
    else:
        return 0.05

df["Scholarship Probability"] = df["Avg GMAT"].apply(
    lambda x: scholarship_probability(predicted_final, x)
)

# =========================
# ROI CALCULATION
# =========================

def calculate_roi(tuition, scholarship_avg):
    net_cost = tuition - scholarship_avg
    salary_gain = post_mba_salary - current_salary
    if salary_gain <= 0:
        return None
    return round(net_cost / salary_gain, 2)

df["Years to Break Even"] = df.apply(
    lambda row: calculate_roi(row["Tuition €"], row["Avg Scholarship €"]), axis=1
)

st.dataframe(df, use_container_width=True)

# =========================
# STRATEGIC RECOMMENDATION
# =========================

st.header("🧠 Strategic Recommendation Engine")

elite_targets = df[df["Admission Probability"] >= 0.4]
safe_targets = df[df["Admission Probability"] < 0.4]

if predicted_final >= 720:
    st.success("Strategia: Applicare Round 1 USA + Germania come hedge.")
elif predicted_final >= 680:
    st.warning("Strategia: Germania + Cina primario. USA solo se profilo extra-forte.")
else:
    st.error("Priorità: Portare GMAT sopra 700 prima di pensare a top-tier USA.")

st.subheader("🎯 Elite Targets")
st.dataframe(elite_targets[["Program", "Admission Probability",
                             "Scholarship Probability",
                             "Years to Break Even"]])

st.subheader("🛡 Safe Targets")
st.dataframe(safe_targets[["Program", "Admission Probability",
                            "Scholarship Probability",
                            "Years to Break Even"]])

st.markdown("---")
st.markdown("Strategic MBA Decision Engine – Built for Scholarship Optimization.")
