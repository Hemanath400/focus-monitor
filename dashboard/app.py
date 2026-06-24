import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import streamlit as st
import sqlite3
import pandas as pd
import time
from pathlib import Path
import plotly.express as px

from ml.predict_burnout import predict  # your ML model

st.set_page_config(page_title="AI Focus Coach", layout="wide")

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "focus_monitor.db"


def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM activity_logs ORDER BY id DESC", conn)
    conn.close()

    if not df.empty:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    return df


def compute_metrics(df):
    total = len(df)
    coding = len(df[df["status"] == "Coding"])
    idle = len(df[df["status"] == "Idle"])

    focus_score = round((coding / total) * 100, 2) if total > 0 else 0

    return total, coding, idle, focus_score


st.title("🧠 AI Focus Coach — Real-Time Productivity System")


placeholder = st.empty()


while True:

    df = load_data()

    if df.empty:
        st.warning("No activity data yet from VS Code extension...")
        time.sleep(2)
        st.rerun()

    total, coding, idle, focus_score = compute_metrics(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Events", total)
    col2.metric("Coding Events", coding)
    col3.metric("Idle Events", idle)
    col4.metric("Focus Score (%)", focus_score)

    st.divider()

    latest = df.head(50)

    coding_count = len(latest[latest["status"] == "Coding"])
    idle_count = len(latest[latest["status"] == "Idle"])
    idle_seconds = latest["idle_seconds"].sum()

    burnout = predict(coding_count, idle_count, idle_seconds)

    st.subheader("🧠 Burnout Risk Level")

    if "HIGH" in burnout:
        st.error(burnout)
    elif "MEDIUM" in burnout:
        st.warning(burnout)
    else:
        st.success(burnout)

    fig1 = px.histogram(df, x="status", title="Activity Distribution")
    st.plotly_chart(fig1, use_container_width=True)

    df_sorted = df.sort_values("timestamp")

    fig2 = px.line(
        df_sorted,
        x="timestamp",
        y="idle_seconds",
        title="Idle Time Trend Over Time"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📌 Recent Activity Logs")
    st.dataframe(df.head(15), use_container_width=True)

    time.sleep(2)
    st.rerun()