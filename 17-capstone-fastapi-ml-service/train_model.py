"""Trains a small classifier on the Iris dataset and persists it to disk
with joblib - the handoff point between the "data science" and
"backend service" worlds."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"trained model test accuracy: {accuracy:.3f}")

joblib.dump({"model": model, "target_names": list(iris.target_names)}, "model.joblib")
print("saved model.joblib")
