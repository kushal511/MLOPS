from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# Load wine dataset
X, y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a simple model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model in the same directory as app.py
model_path = os.path.join(os.path.dirname(__file__), "wine_model.pkl")
joblib.dump(model, model_path)

print("✅ Model trained and saved at:", model_path)
