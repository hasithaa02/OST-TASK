import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import argparse

# Argument parser for command-line execution
parser = argparse.ArgumentParser()
parser.add_argument("--data", required=True, help="Path to dataset")
parser.add_argument("--output", required=True, help="Path to save model")
args = parser.parse_args()

# Load dataset (Replace with real dataset)
data = pd.read_csv(f"{args.data}/fraud_data.csv")
X = data.drop(columns=["fraudulent"])
y = data["fraudulent"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
with open(args.output, "wb") as f:
    pickle.dump(model, f)

print(f"Model trained and saved to {args.output}")
