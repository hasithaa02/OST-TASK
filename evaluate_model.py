import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model", required=True, help="Path to trained model")
args = parser.parse_args()

# Load test data
test_data = pd.read_csv("data/fraud_data.csv")
X_test = test_data.drop(columns=["fraudulent"])
y_test = test_data["fraudulent"]

# Load model
with open(args.model, "rb") as f:
    model = pickle.load(f)

# Predict and evaluate
y_pred = model.predict(X_test)
score = accuracy_score(y_test, y_pred)

print(score)
