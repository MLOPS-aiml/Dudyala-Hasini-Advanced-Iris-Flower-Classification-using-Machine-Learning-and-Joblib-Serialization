import joblib
import pandas as pd
import os

# ==========================================
# Load Saved Model
# ==========================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "best_model.pkl")

model = joblib.load(model_path)

# ==========================================
# Enter New Flower Details
# ==========================================

new_flower = pd.DataFrame({

    "SepalLengthCm": [6.5],
    "SepalWidthCm": [3.2],
    "PetalLengthCm": [5.1],
    "PetalWidthCm": [2.0],
    "SepalArea": [20.80],
    "PetalArea": [10.20],
    "TotalFlowerArea": [31.00],
    "SepalPetalRatio": [1.275],
    "PetalAspectRatio": [2.55],
    "FlowerVolumeIndex": [10.61],
    "Temperature": [25.5],
    "Humidity": [65],
    "SunlightHours": [7.5],
    "SoilPH": [6.5],
    "SoilMoisture": [55],
    "Rainfall": [120],
    "HealthScore": [92],
    "DiseaseRisk": [1]

})

# ==========================================
# Prediction
# ==========================================

prediction = model.predict(new_flower)

species = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

print("=" * 50)
print("IRIS FLOWER PREDICTION")
print("=" * 50)

print("Predicted Species :", species[prediction[0]])