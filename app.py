import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

st.set_page_config(page_title="MiM 2026 Strategic Planner", layout="wide")

st.title("🎓 MiM 2026 – Strategic Control Panel")

# =============================
# DEADLINE DATABASE
# =============================

schools = pd.DataFrame({
    "School": [
        "HEC Paris",
        "LBS MiM",
        "ESSEC",
        "Bocconi",
        "St. Gallen",
        "Tsinghua",
        "MIT Sloan MFin"
    ],
    "Country": [
        "France",
        "UK",
        "France",
        "Italy",
        "Switzerland",
        "China",
        "USA"
    ],
    "Round 1 Deadline": [
        "2025-10-01",
        "2025-09-15",
        "2025-10-15",
        "2025-11-01",
        "2025-10-30",
        "2025-12-01",
        "2025-09-20"
    ],
    "Avg GMAT": [700, 690, 680, 670, 690, 710, 720]
})

st.subheader("📅 Target Schools & Deadlines")
st.dataframe(schools)

# =============================
# GMAT TRACKER
# =============================

st.subheader("📊 GMAT Performance Tracker")

current_score = st.number_input("Current GMAT Score", 200, 805, 575)
target_score = st.number_input("Target Score", 200, 805, 720)

weeks_available = st.number_input("Weeks until GMAT", 1, 40, 24)

required_growth = target_score - current_score
weekly_growth = required_growth / weeks_available

st.metric("Points to Gain", required_growth)
st.metric("Required Weekly Improvement", round(weekly_growth, 2))

# Probability Estimation
if current_score < 600:
    prob = 20
elif current_score < 650:
    prob = 40
elif current_score < 700:
    prob = 60
elif current_score < 720:
    prob = 75
else:
    prob = 85

st.progress(prob / 100)
st.write(f"Estimated Admission Strength: {prob}% (heuristic model)")

# =============================
# STUDY PLANNER
# =============================

st.subheader("📅 Weekly Time Allocation")

gmat_hours = st.slider("GMAT Study Hours / Week", 5, 40, 20)
thesis_hours = st.slider("Thesis Hours / Week", 5, 40, 15)
gym_hours = st.slider("Gym Hours / Week", 2, 10, 4)
rest_hours = st.slider("Rest / Social", 2, 20, 8)

total = gmat_hours + thesis_hours + gym_hours + rest_hours

st.write(f"Total Structured Hours: {total}")

if total > 60:
    st.warning("⚠️ Risk of burnout. Optimize.")
else:
    st.success("Balanced structure.")

# =============================
# TASK BOARD
# =============================

st.subheader("🗂️ Task Tracker")

task = st.text_input("Add Task")
deadline = st.date_input("Deadline", datetime.date.today())

if st.button("Add Task"):
    st.write(f"Task Added: {task} – Due {deadline}")

# =============================
# STRATEGIC ADVICE ENGINE
# =============================

st.subheader("🧠 Strategic Recommendation")

today = datetime.date.today()
gmattargetdate = datetime.date(2025, 9, 15)

if today > gmattargetdate:
    st.error("You are late for Round 1. Consider Round 2 or Plan B.")
else:
    days_left = (gmattargetdate - today).days
    st.write(f"Days until ideal GMAT date: {days_left}")

    if days_left < 90:
        st.warning("High intensity mode required.")
    else:
        st.success("On track if disciplined.")

st.markdown("---")
st.write("System Designed for Elite Execution.")
