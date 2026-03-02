import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import date, datetime, timedelta

# --- 1. CONFIGURAZIONE SISTEMA & STILE ---
st.set_page_config(page_title="CEO OS v6.0", layout="wide", initial_sidebar_state="expanded")

# CSS "Bloomberg Terminal" - Nero assoluto, font tecnici, zero distrazioni
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #e0e0e0; font-family: 'Roboto Mono', monospace; }
    .stMetric { background-color: #111; border: 1px solid #333; padding: 10px; border-radius: 5px; }
    h1, h2, h3 { color: #00ff41; font-family: 'Orbitron', sans-serif; letter-spacing: 1px; }
    .stProgress > div > div > div > div { background-color: #00ff41; }
    .stTabs [data-baseweb="tab-list"] { gap: 2px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #111; border-radius: 4px 4px 0px 0px; color: #888; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #00ff41; color: #000; font-weight: bold; }
    div[data-testid="stExpander"] div[role="button"] p { font-size: 1.1rem; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GESTIONE STATO (SESSION STATE) ---
# Inizializza i dati se non esistono (simula un database)
if 'gmat_scores' not in st.session_state:
    st.session_state.gmat_scores = pd.DataFrame([
        {"Date": "2025-10-01", "Type": "Cold Test", "Total": 575, "Quant": 79, "Verbal": 79, "DI": 78},
    ])
if 'todo_thesis' not in st.session_state:
    st.session_state.todo_thesis = [
        {"Task": "Analisi Competitor (Strategic)", "Done": False},
        {"Task": "Clean Dataset Excel", "Done": True},
        {"Task": "Literature Review Cap 1", "Done": False},
        {"Task": "Drafting Indice Tesi", "Done": True}
    ]

# --- 3. SIDEBAR: PROFILO & NAVIGAZIONE ---
with st.sidebar:
    st.title("👤 CEO PROFILE")
    st.image("https://ui-avatars.com/api/?name=CEO+2026&background=00ff41&color=000", width=100)
    st.markdown("---")
    st.metric("GPA", "29.2 / 30", "Excellence")
    
    # Calcolo Giorni alla Deadline HEC
    today = date.today()
    hec_deadline = date(2026, 4, 9)
    delta = hec_deadline - today
    st.metric("HEC COUNTDOWN", f"{delta.days} Days", "Critical Path", delta_color="inverse")
    
    st.markdown("---")
    nav = st.radio("SISTEMA OPERATIVO", ["DASHBOARD", "GMAT WAR ROOM", "ACADEMIC PM", "MASTER CRM", "AGENDA DETTAGLIATA"])
    
    st.info("💡 **Daily Mantra:**\n\n'Discipline equals Freedom.'")

# --- 4. MODULI DEL SISTEMA ---

# === MODULO 1: DASHBOARD (PANORAMICA) ===
if nav == "DASHBOARD":
    st.title("🚀 MAIN COMMAND CENTER")
    
    # KPI Row
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("GMAT Gap", "-70 pts", "Target 645")
    k2.metric("Thesis Burn", "35%", "Deadline Luglio")
    k3.metric("Gym Streak", "3 Weeks", "Body & Mind")
    k4.metric("Audio Hours", "12h", "Commute Learning")
    
    st.markdown("---")
    
    # Grafico Radar Competence
    c1, c2 = st.columns([1, 1.5])
    with c1:
        st.subheader("⚠️ WEAKNESS DETECTOR")
        radar_data = pd.DataFrame(dict(
            r=[79, 79, 78, 90, 85],
            theta=['Quant', 'Verbal', 'Data Insights', 'Leadership', 'Strategic Vision']))
        fig = px.line_polar(radar_data, r='r', theta='theta', line_close=True, range_r=[0,100], template="plotly_dark")
        fig.update_traces(fill='toself', line_color='#00ff41')
        st.plotly_chart(fig, use_container_width=True)
        st.error("ACTION REQUIRED: **Verbal Reasoning** is the bottleneck.")
        
    with c2:
        st.subheader("🔥 IMMEDIATE ACTIONS")
        st.markdown("""
        1.  **Prenotare GMAT:** Confermare data Aprile 2026.
        2.  **Strategic Mgmt:** Chiudere analisi "Five Forces" entro Venerdì.
        3.  **HEC Essay:** Scrivere bozza "Leadership Failure" story.
        4.  **Networking:** Contattare 1 Alumni HEC su LinkedIn.
        """)
        st.progress(0.4)

# === MODULO 2: GMAT WAR ROOM (TRACKING AVANZATO) ===
elif nav == "GMAT WAR ROOM":
    st.title("📉 GMAT ADVANCED ANALYTICS")
    
    col_input, col_graph = st.columns([1, 2])
    
    with col_input:
        st.subheader("📝 Log New Mock")
        with st.form("mock_form"):
            d_date = st.date_input("Data Simulazione")
            d_type = st.selectbox("Tipo", ["Official Mock", "Manhattan", "GMAT Club"])
            d_tot = st.number_input("Score Totale", 205, 805, 575)
            d_q = st.number_input("Quant Score", 60, 90, 79)
            d_v = st.number_input("Verbal Score", 60, 90, 79)
            d_di = st.number_input("DI Score", 60, 90, 78)
            submitted = st.form_submit_button("REGISTRA SCORE")
            
            if submitted:
                new_row = {"Date": str(d_date), "Type": d_type, "Total": d_tot, "Quant": d_q, "Verbal": d_v, "DI": d_di}
                st.session_state.gmat_scores = pd.concat([st.session_state.gmat_scores, pd.DataFrame([new_row])], ignore_index=True)
                st.success("Dati Salvati!")

    with col_graph:
        st.subheader("📈 Performance Trend")
        if not st.session_state.gmat_scores.empty:
            df_gmat = st.session_state.gmat_scores
            fig_trend = px.line(df_gmat, x="Date", y="Total", markers=True, title="Score Evolution vs Target (645)", template="plotly_dark")
            fig_trend.add_hline(y=645, line_dash="dot", line_color="red", annotation_text="TARGET")
            fig_trend.update_traces(line_color='#00ff41')
            st.plotly_chart(fig_trend, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🧠 Verbal Error Log Analysis")
    err1, err2, err3 = st.columns(3)
    err1.warning("**Critical Reasoning**\n\nAccuracy: 45%\n\nProblem: Assumption Negation")
    err2.info("**Reading Comp.**\n\nAccuracy: 60%\n\nProblem: Science Passages")
    err3.success("**Sentence Corr.**\n\nN/A (Removed in Focus)")

# === MODULO 3: ACADEMIC PM (TESI & ESAMI) ===
elif nav == "ACADEMIC PM":
    st.title("🎓 ACADEMIC PROJECT MANAGEMENT")
    
    tab_thesis, tab_exams = st.tabs(["🔬 TESI GANTT", "📚 ESAMI CHECKLIST"])
    
    with tab_thesis:
        st.subheader("Thesis Execution Timeline")
        # Dati Gantt Chart
        df_gantt = pd.DataFrame([
            dict(Task="Ricerca Bibliografica", Start='2026-01-10', Finish='2026-02-28', Resource='Research'),
            dict(Task="Analisi Dati & Python", Start='2026-03-01', Finish='2026-03-30', Resource='Analytics'),
            dict(Task="Scrittura Cap 1-2", Start='2026-03-15', Finish='2026-04-15', Resource='Writing'),
            dict(Task="Scrittura Cap 3-4", Start='2026-04-16', Finish='2026-05-30', Resource='Writing'),
            dict(Task="Revisione Finale", Start='2026-06-01', Finish='2026-06-20', Resource='Review')
        ])
        fig_gantt = px.timeline(df_gantt, x_start="Start", x_end="Finish", y="Task", color="Resource", template="plotly_dark", color_discrete_sequence=['#888', '#00ff41', '#00d4ff'])
        st.plotly_chart(fig_gantt, use_container_width=True)
        
        st.markdown("#### 📝 Micro-Tasks Tesi")
        for i, task in enumerate(st.session_state.todo_thesis):
            cols = st.columns([0.1, 0.9])
            done = cols[0].checkbox("", value=task["Done"], key=f"t_{i}")
            cols[1].write(f"**{task['Task']}**")
            # Aggiorna stato (logica visuale)
            
    with tab_exams:
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("### 🏛️ STRATEGIC")
            st.checkbox("Project: 5 Forces", value=True)
            st.checkbox("Project: Business Model Canvas", value=False)
            st.checkbox("Study: Chapters 1-5")
            st.progress(0.4)
        with c2:
            st.markdown("### ⚙️ SERVICE")
            st.checkbox("Project: Blueprinting", value=False)
            st.checkbox("Study: Queue Theory")
            st.progress(0.2)
        with c3:
            st.markdown("### 💻 LAB")
            st.checkbox("Code: Python Script", value=False)
            st.checkbox("Report Finale")
            st.progress(0.1)

# === MODULO 4: MASTER CRM (APPLICAZIONI) ===
elif nav == "MASTER CRM":
    st.title("🏛️ MASTER APPLICATION PIPELINE")
    
    hec, mann, escp = st.tabs(["🇫🇷 HEC PARIS", "🇩🇪 MANNHEIM", "🇪🇺 ESCP"])
    
    with hec:
        st.markdown("## 🦅 HEC Paris - MSc in Management")
        st.warning("DEADLINE: 09 APRILE 2026 (Priority 1)")
        
        col_docs, col_essay = st.columns(2)
        with col_docs:
            st.subheader("📂 Document Checklist")
            st.checkbox("CV (McKinsey Format)", value=True)
            st.checkbox("GMAT Official Report (Target 645+)", value=False)
            st.checkbox("Transcript Tradotto (GPA 29.2)", value=True)
            st.checkbox("2 Lettere di Referenza (Prof + Stage)", value=False)
            st.checkbox("TOEFL/IELTS (Se richiesto)", value=True)
            
        with col_essay:
            st.subheader("✍️ Essays Strategy")
            st.markdown("""
            * **Essay 1 (Why HEC?):** Focus su Entrepreneurship center & Alumni network. (Stato: *Drafting*)
            * **Essay 2 (Leadership):** Raccontare gestione team progetto universitario. (Stato: *To-Do*)
            * **Essay 3 (Achievement):** Focus su media voti + Sport costanza. (Stato: *To-Do*)
            """)
            st.text_area("Note Essay HEC", "Inserire qui spunti per i saggi...")

# === MODULO 5: AGENDA DETTAGLIATA (MATRIX) ===
elif nav == "AGENDA DETTAGLIATA":
    st.title("📆 THE MATRIX: WEEKLY EXECUTION")
    
    # Selector Giorno
    selected_day = st.select_slider("Select Operational Day", options=["LUN", "MAR", "MER", "GIO", "VEN", "SAB"])
    
    # Dati precisi come richiesto
    schedules = {
        "LUN": [
            ("08:00-09:00", "GMAT Verbal", "Critical Reasoning Drill"),
            ("09:00-10:00", "GMAT Verbal", "Reading Comprehension"),
            ("10:00-12:00", "TESI", "Analisi Dati & Progettazione"),
            ("12:00-13:00", "PRANZO", "Power Nap + Podcast"),
            ("13:00-14:00", "MASTER", "Admin & Application Check"),
            ("14:00-16:00", "STRATEGIC", "Project Work Deep Dive"),
            ("16:00-17:00", "LAB", "Coding & Testing"),
            ("17:00-18:00", "COMMUTE", "🚗 Audio: GMAT Ninja Verbal"),
            ("18:00-19:30", "GYM", "🏋️ Strength Training")
        ],
        "MAR": [
            ("08:00-11:00", "GMAT Quant", "Hard Quant Practice"),
            ("11:00-12:00", "TESI", "Scrittura Capitolo"),
            ("12:00-13:00", "COMMUTE", "🚗 Audio: Case Interview Prep"),
            ("14:00-18:00", "UNI: SERVICE", "Lezione in Presenza"),
            ("18:00-19:00", "COMMUTE", "🚗 Audio: Podcast Economia")
        ],
        "MER": [
            ("08:00-09:00", "COMMUTE", "🚗 Audio: GMAT Logic"),
            ("09:00-13:00", "UNI: STRATEGIC", "Lezione in Presenza"),
            ("13:00-14:00", "PRANZO", "Mensa Uni / Networking"),
            ("14:00-16:00", "UNI: LAB", "Lezione Pratica"),
            ("16:00-18:00", "PROJECTS", "Lavoro di gruppo in Uni"),
            ("18:00-19:00", "COMMUTE", "🏠 Rientro Base")
        ]
        # Puoi aggiungere GIO/VEN/SAB qui...
    }
    
    # Rendering Tabella Custom
    if selected_day in schedules:
        st.subheader(f"Protocollo Operativo: {selected_day}")
        for slot in schedules[selected_day]:
            with st.container():
                c1, c2, c3 = st.columns([1, 1, 3])
                c1.code(slot[0]) # Orario
                c2.markdown(f"**{slot[1]}**") # Attività
                c3.caption(slot[2]) # Dettaglio
                st.markdown("---")
    else:
        st.info("Configurazione per GIO/VEN/SAB in caricamento... (Aggiungere nel codice)")

st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)
st.sidebar.caption("CEO OS v6.0 • SYSTEM ACTIVE")
