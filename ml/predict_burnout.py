import joblib
import numpy as np

model = joblib.load("ml/burnout_model.pkl")


def predict(coding, idle, idle_seconds):

    pred = model.predict([[coding, idle, idle_seconds]])[0]

    if pred == 2:
        return "HIGH 🔴"
    elif pred == 1:
        return "MEDIUM 🟠"
    else:
        return "LOW 🟢"