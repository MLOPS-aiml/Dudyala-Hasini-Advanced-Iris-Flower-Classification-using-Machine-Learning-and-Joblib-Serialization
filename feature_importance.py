import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(BASE_DIR, "dataset", "processed_iris.csv")
model_path = os.path.join(BASE_DIR, "models", "best_model.pkl")

# ==========================================
# Load Dataset & Model
# ==========================================

df = pd.read_csv(dataset_path)

X = df.drop("Species", axis=1)

model = joblib.load(model_path)

# ==========================================
# Check Feature Importance Support
# ==========================================

if not hasattr(model, "feature_importances_"):
    print("The selected model does not support feature importance.")
    exit()

# ==========================================
# Feature Importance
# ==========================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

print(importance)

# ==========================================
# Save CSV
# ==========================================

csv_path = os.path.join(
    BASE_DIR,
    "evaluation",
    "feature_importance.csv"
)

importance.to_csv(csv_path, index=False)

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(10,7))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Feature Importance")
plt.gca().invert_yaxis()

plt.tight_layout()

image_path = os.path.join(
    BASE_DIR,
    "evaluation",
    "feature_importance.png"
)

plt.savefig(image_path)

plt.show()

print("\nFeature importance saved successfully!")
print("CSV :", csv_path)
print("Image :", image_path)