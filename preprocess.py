import pandas as pd
import os

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
dataset_path = os.path.join(BASE_DIR, "dataset", "Iris.csv")

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

# Load dataset
df = pd.read_csv(dataset_path)

print("\nDataset Loaded Successfully!")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# Remove Id column if available
if "Id" in df.columns:
    df.drop("Id", axis=1, inplace=True)
    print("\nId column removed.")

print("\nFirst Five Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(df.shape)

# Save cleaned dataset
cleaned_path = os.path.join(BASE_DIR, "dataset", "cleaned_iris.csv")
df.to_csv(cleaned_path, index=False)

print("\nCleaned dataset saved successfully!")
print(cleaned_path)