import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / r"C:\Users\HEMANATH\Desktop\focus-monitor\ml_dataset.csv")

X = df[[
    "session_duration",
    "start_hour",
    "day_of_week"
]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X_scaled)

joblib.dump(kmeans, BASE_DIR / "kmeans_model.pkl")
joblib.dump(scaler, BASE_DIR / "scaler.pkl")

df.to_csv(BASE_DIR / "clustered_sessions.csv", index=False)

print("KMeans model trained!")
print(df["cluster"].value_counts())