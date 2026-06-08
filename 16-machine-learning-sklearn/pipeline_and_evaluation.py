"""Pipelines (bundle preprocessing + model into one object) and
cross-validation (a more robust evaluation than a single train/test split)."""

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X, y = iris.data, iris.target

# A Pipeline chains steps together - scaling always happens before fitting,
# and importantly, the scaler is fit ONLY on training data to avoid leakage.
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=200)),
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

pipeline.fit(X_train, y_train)
print("test accuracy:", pipeline.score(X_test, y_test))

# Cross-validation: fit/evaluate 5 times on different splits of the data,
# giving a more reliable estimate than any single train/test split.
scores = cross_val_score(pipeline, X, y, cv=5)
print("cross-val scores:", scores)
print(f"mean accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")
