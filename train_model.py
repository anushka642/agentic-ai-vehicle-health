import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv("data/telemetry.csv")

df.columns = (
    df.columns
    .str.replace('\ufeff', '', regex=False) 
    .str.strip()                             
)

print("Cleaned columns:", list(df.columns))

X = df.drop(columns=["failure"])
y = df["failure"]


model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


y_pred = model.predict(X)

accuracy = accuracy_score(y, y_pred)
print(f"\nModel Accuracy: {accuracy:.2f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y, y_pred))

print("\nClassification Report:")
print(classification_report(y, y_pred))


importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(8, 4))
plt.barh(features, importances)
plt.xlabel("Importance Score")
plt.title("Feature Importance for Vehicle Failure Prediction")
plt.tight_layout()
plt.show()


with open("models/failure_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n✅ Model trained and saved successfully.")
