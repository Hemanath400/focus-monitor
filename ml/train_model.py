import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / r"C:\Users\HEMANATH\Desktop\focus-monitor\ml_dataset.csv")

# ---------------- LABELING ----------------
# Long session = productive (1), short = 0

df["label"] = df["session_duration"].apply(
    lambda x: 1 if x >= 25 else 0
)

X = df[["session_duration", "start_hour"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

acc = model.score(X_test, y_test)

print("Accuracy:", acc)

joblib.dump(model, BASE_DIR / "focus_model.pkl")

print("Model saved!")