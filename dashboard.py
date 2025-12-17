import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
import json
import random

st.set_page_config(
    page_title="Agentic AI Vehicle Health Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Agentic AI – Vehicle Health Dashboard")

df = pd.read_csv("data/telemetry.csv")
df.columns = df.columns.str.replace("\ufeff", "").str.strip()

if os.path.exists("models/failure_model.pkl"):
    model = pickle.load(open("models/failure_model.pkl", "rb"))
else:
    X_train = df.drop(columns=["failure"])
    y_train = df["failure"]
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

vehicle_ids = sorted(df["vehicle_id"].unique())
query_params = st.query_params
default_vehicle = int(query_params.get("vehicle_id", vehicle_ids[0]))

vehicle_id = st.sidebar.selectbox(
    "Select Vehicle ID",
    vehicle_ids,
    index=vehicle_ids.index(default_vehicle) if default_vehicle in vehicle_ids else 0
)

st.query_params["vehicle_id"] = str(vehicle_id)

row = df[df["vehicle_id"] == vehicle_id].iloc[-1]
X_input = row.drop("failure").to_frame().T
X_input = X_input[model.feature_names_in_]

prediction = model.predict(X_input)[0]

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔍 Prediction Result")

    if prediction == 1:
        st.error("⚠ Failure Likely – Immediate Service Recommended")
    else:
        st.success("✅ Vehicle Healthy")

    st.markdown("### 📊 Telemetry Data")
    st.dataframe(row)

    st.markdown("### 📌 Key Metrics")
    m1, m2, m3 = st.columns(3)
    m1.metric("Engine Temp (°C)", row["engine_temp"])
    m2.metric("Battery Voltage (V)", row["battery_voltage"])
    m3.metric("Mileage (km)", row["mileage"])

with col2:
    
    st.markdown("")

    logs = ["System started"]

    st.markdown("### 💬 Agent Chat Simulation")
    st.markdown("**Diagnosis Agent:** Failure detected based on telemetry.")
    st.markdown("**Customer Agent:** Notifying customer about potential failure.")

    st.markdown("")
    st.divider()

    st.markdown("### 📅 Service Booking")
    slots_data = json.load(open("data/service_slots.json"))
    slots = slots_data.get("slots", []) if isinstance(slots_data, dict) else slots_data

    if slots:
        booked_slot = random.choice(slots)
        st.success(f"✅ Service booked at **{booked_slot}**")
        logs.append(f"Service booked at {booked_slot}")
    else:
        st.warning("⚠ No service slots available")

    st.markdown("")
    st.divider()

    st.markdown("### 🛠 RCA / Feedback Panel")
    st.info(
        f"""
        **Root Cause Analysis Summary**

        • Issue: Engine overheating suspected  
        • Engine Temp: {row['engine_temp']} °C  
        • Oil Level: {row['oil_level']}  
        • Recommended Action: Immediate inspection
        """
    )
    logs.append("RCA generated")

    st.markdown("")
    st.divider()

    st.markdown("### 📜 UEBA Logs")
    for log in logs:
        st.write(f"• {log}")
