import sqlite3
import time
from datetime import datetime, timedelta
from pathlib import Path

from plyer import notification
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "focus_monitor.db"

MODEL_PATH = BASE_DIR / "ml/burnout_model.pkl"
SCALER_PATH = BASE_DIR / "ml/burnout_scaler.pkl"

model = None
scaler = None

if MODEL_PATH.exists() and SCALER_PATH.exists():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)


last_notification_time = datetime.min
COOLDOWN_SECONDS = 30


def get_recent_logs(limit=20):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp, status
        FROM activity_logs
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows


def build_features(rows):

    if not rows:
        return None

    df = pd.DataFrame(rows, columns=["timestamp", "status"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    coding = df[df["status"] == "Coding"]
    idle = df[df["status"] == "Idle"]

    total = len(df)

    coding_ratio = len(coding) / max(total, 1)
    idle_ratio = len(idle) / max(total, 1)

    # session approx duration (5 sec logs assumption)
    session_duration = len(coding) * 5 / 60

    start_hour = datetime.now().hour
    day_of_week = datetime.now().weekday()

    return {
        "session_duration": session_duration,
        "start_hour": start_hour,
        "day_of_week": day_of_week,
        "idle_ratio": idle_ratio,
        "coding_ratio": coding_ratio
    }


def predict_burnout(features):

    if model is None:
        return None

    X = pd.DataFrame([{
        "session_duration": features["session_duration"],
        "start_hour": features["start_hour"],
        "day_of_week": features["day_of_week"],
        "idle_ratio": features["idle_ratio"]
    }])

    X_scaled = scaler.transform(X)

    return model.predict(X_scaled)[0]


def notify(title, message):

    global last_notification_time

    now = datetime.now()

    if (now - last_notification_time).total_seconds() < COOLDOWN_SECONDS:
        return

    notification.notify(
        title=title,
        message=message,
        timeout=4
    )

    last_notification_time = now


def analyze():

    rows = get_recent_logs()

    features = build_features(rows)

    if not features:
        return

    burnout_pred = predict_burnout(features)

    coding_ratio = features["coding_ratio"]

    # ---------------- DECISION TREE ----------------

    if burnout_pred == 1:
        notify(
            "⚠️ AI Focus Coach",
            "High burnout risk detected. Take a 10 min break."
        )

    elif coding_ratio > 0.75:
        notify(
            "🔥 Focus Coach",
            "Deep focus detected. Stay in flow state!"
        )

    elif coding_ratio > 0.4:
        notify(
            "🧠 Focus Coach",
            "Balanced productivity. Keep consistency."
        )

    else:
        notify(
            "⚠️ Focus Coach",
            "You seem distracted. Try refocusing on coding."
        )


if __name__ == "__main__":

    print("🧠 Real-Time AI Focus Coach Started...")

    while True:
        try:
            analyze()
            time.sleep(15)  # check every 15 seconds
        except Exception as e:
            print("Error:", e)
            time.sleep(5)