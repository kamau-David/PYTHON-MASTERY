"""Classification: predicting a category. Uses the classic Iris dataset
built into scikit-learn, plus a confusion matrix and classification report."""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("accuracy:", accuracy_score(y_test, predictions))
print("\nconfusion matrix:\n", confusion_matrix(y_test, predictions))
print("\nclassification report:\n",
      classification_report(y_test, predictions, target_names=iris.target_names))

# Feature importance - which measurements mattered most to the model
for name, importance in zip(iris.feature_names, model.feature_importances_):
    print(f"{name}: {importance:.3f}")
