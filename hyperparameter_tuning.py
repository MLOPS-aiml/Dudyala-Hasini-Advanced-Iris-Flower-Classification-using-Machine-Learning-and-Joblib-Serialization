import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("../dataset/processed_iris.csv")

X = df.drop("Species", axis=1)
y = df["Species"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Base Model
model = ExtraTreesClassifier(random_state=42)

# Parameters to Search
params = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 10, 20],
    "min_samples_split": [2, 5],
    "min_samples_leaf": [1, 2]
}

grid = GridSearchCV(
    estimator=model,
    param_grid=params,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid.fit(X_train, y_train)

best_model = grid.best_estimator_

prediction = best_model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("="*60)
print("BEST PARAMETERS")
print("="*60)

print(grid.best_params_)

print("\nAccuracy :", accuracy)

joblib.dump(best_model, "best_model_tuned.pkl")

print("\nTuned model saved successfully")