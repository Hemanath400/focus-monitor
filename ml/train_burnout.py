import pandas as pd
import sqlite3
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
import joblib

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "focus_monitor.db"


def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM activity_logs", conn)
    conn.close()
    return df


def prepare_data(df):

    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # basic features
    df["coding_flag"] = (df["status"] == "Coding").astype(int)
    df["idle_flag"] = (df["status"] == "Idle").astype(int)

    session = df.groupby(df["timestamp"].dt.date).agg({
        "coding_flag": "sum",
        "idle_flag": "sum",
        "idle_seconds": "sum"
    }).reset_index()

    def label(row):
        if row["coding_flag"] > 50 and row["idle_seconds"] < 200:
            return 2  # HIGH burnout risk
        elif row["coding_flag"] > 20:
            return 1  # MEDIUM
        else:
            return 0  # LOW

    session["label"] = session.apply(label, axis=1)

    return session


def train():

    df = load_data()
    data = prepare_data(df)

    X = data[["coding_flag", "idle_flag", "idle_seconds"]]
    y = data["label"]

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    joblib.dump(model, "ml/burnout_model.pkl")

    print("Model trained and saved!")


if __name__ == "__main__":
    train()