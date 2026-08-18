import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../dataset/cleaned_iris.csv")

print("="*60)
print("Feature Engineering Started")
print("="*60)

# Remove ID
if "Flower_ID" in df.columns:
    df.drop("Flower_ID", axis=1, inplace=True)

# Encode DiseaseRisk
disease_encoder = LabelEncoder()
df["DiseaseRisk"] = disease_encoder.fit_transform(df["DiseaseRisk"])

# Encode Species (Target)
species_encoder = LabelEncoder()
df["Species"] = species_encoder.fit_transform(df["Species"])

# Save processed dataset
df.to_csv("../dataset/processed_iris.csv", index=False)

print("\nProcessed Dataset Shape:")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nFeature Engineering Completed Successfully")