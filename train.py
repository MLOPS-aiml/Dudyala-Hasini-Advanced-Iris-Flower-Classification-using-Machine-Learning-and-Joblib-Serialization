import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Load dataset
df = pd.read_csv("../dataset/processed_iris.csv")

X = df.drop("Species", axis=1)
y = df["Species"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42
    ),
    "Extra Trees": ExtraTreesClassifier(
        n_estimators=500,
        random_state=42
    ),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=3),
    "SVM": SVC(kernel="rbf", C=10)
}

# Optional XGBoost
try:
    from xgboost import XGBClassifier

    models["XGBoost"] = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        subsample=0.9,
        colsample_bytree=0.9,
        random_state=42,
        eval_metric="mlogloss"
    )

except:
    print("XGBoost not installed")

results = []

best_model = None
best_accuracy = 0
best_name = ""

print("=" * 70)
print("MODEL COMPARISON")
print("=" * 70)

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)

    results.append([name, acc])

    print(f"{name:<25} {acc:.4f}")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model
        best_name = name

joblib.dump(best_model, "best_model.pkl")

results = pd.DataFrame(
    results,
    columns=["Model", "Accuracy"]
).sort_values(
    by="Accuracy",
    ascending=False
)

print("\n")
print(results)

print("\nBest Model :", best_name)
print("Accuracy   :", round(best_accuracy * 100, 2), "%")

results.to_csv("model_comparison.csv", index=False)

print("\nSaved:")
print("✓ best_model.pkl")
print("✓ model_comparison.csv")