import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Agentic AI Vehicle Health Dashboard",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Agentic AI – Vehicle Health Dashboard")
st.caption("Predictive Maintenance using Multi-Agent AI")

df = pd.read_csv("data/telemetry.csv")

df.columns = (
    df.columns
    .str.replace('\ufeff', '', regex=False)
    .str.strip()
)

model = pickle.load(open("models/failure_model.pkl", "rb"))

st.sidebar.header("Vehicle Selection")
vehicle = st.sidebar.selectbox(
    "Select Vehicle ID",
    df["vehicle_id"].unique()
)

row = df[df["vehicle_id"] == vehicle].iloc[-1]

X = row.drop("failure").to_frame().T

X = X[model.feature_names_in_]

prediction = model.predict(X)[0]

st.subheader("🔍 Prediction Result")

if prediction == 1:
    st.error("⚠️ Failure Likely – Immediate Service Recommended")
else:
    st.success("✅ Vehicle Healthy")

st.subheader("📊 Telemetry Data")
st.dataframe(row)

st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Engine Temp (°C)", row["engine_temp"])
col2.metric("Battery Voltage (V)", row["battery_voltage"])
col3.metric("Mileage (km)", row["mileage"])

st.caption("Powered by Agentic AI System")
