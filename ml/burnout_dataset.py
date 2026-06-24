import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "focus_monitor.db"

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql("SELECT * FROM activity_logs", conn)
conn.close()

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")

def build_sessions(df, gap_threshold=10):

    sessions = []
    start = None
    last = None

    for _, row in df.iterrows():

        if row["status"] != "Coding":
            continue

        ts = row["timestamp"]

        if start is None:
            start = ts
            last = ts
            continue

        gap = (ts - last).total_seconds()

        if gap > gap_threshold:
            sessions.append((start, last))
            start = ts

        last = ts

    if start and last:
        sessions.append((start, last))

    return sessions


sessions = build_sessions(df)

data = []

for start, end in sessions:

    duration = (end - start).total_seconds() / 60

    hour = start.hour

    day = start.weekday()

    data.append({
        "session_duration": duration,
        "start_hour": hour,
        "day_of_week": day,
        "idle_ratio": len(df[df["status"] == "Idle"]) / max(len(df), 1)
    })

ml_df = pd.DataFrame(data)

def label_burnout(row):

    if row["session_duration"] < 10:
        return 1   # HIGH burnout risk (low focus)
    elif row["session_duration"] < 25:
        return 0   # medium
    else:
        return 0   # low risk (stable)

ml_df["burnout_risk"] = ml_df.apply(label_burnout, axis=1)

ml_df.to_csv(BASE_DIR / "burnout_dataset.csv", index=False)

print("Dataset ready:", ml_df.shape)
print(ml_df.head())