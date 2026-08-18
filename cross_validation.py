import pandas as pd
import joblib
import os

from sklearn.model_selection import cross_val_score, StratifiedKFold

# ==========================================
# Load Dataset
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(BASE_DIR, "dataset", "processed_iris.csv")
model_path = os.path.join(BASE_DIR, "models", "best_model.pkl")

df = pd.read_csv(dataset_path)

# Features and Target
X = df.drop("Species", axis=1)
y = df["Species"]

# ==========================================
# Load Best Model
# ==========================================

model = joblib.load(model_path)

# ==========================================
# 5-Fold Cross Validation
# ==========================================

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

# ==========================================
# Display Results
# ==========================================

print("=" * 60)
print("5-FOLD CROSS VALIDATION RESULTS")
print("=" * 60)

for i, score in enumerate(scores, start=1):
    print(f"Fold {i} Accuracy : {score:.4f}")

print("\nMean Accuracy :", round(scores.mean(), 4))
print("Standard Deviation :", round(scores.std(), 4))

# ==========================================
# Save Results
# ==========================================

result_file = os.path.join(BASE_DIR, "evaluation", "cross_validation_report.txt")

with open(result_file, "w") as file:
    file.write("5-FOLD CROSS VALIDATION REPORT\n")
    file.write("=" * 50 + "\n\n")

    for i, score in enumerate(scores, start=1):
        file.write(f"Fold {i} Accuracy : {score:.4f}\n")

    file.write(f"\nMean Accuracy : {scores.mean():.4f}\n")
    file.write(f"Standard Deviation : {scores.std():.4f}\n")

print("\nCross Validation Report Saved Successfully!")