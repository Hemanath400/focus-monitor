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
        "day_of_week": day
    })

ml_df = pd.DataFrame(data)

ml_df = ml_df[ml_df["session_duration"] > 0]

ml_df.to_csv(BASE_DIR / "ml_dataset.csv", index=False)

print("Dataset created:", ml_df.shape)
print(ml_df.head())