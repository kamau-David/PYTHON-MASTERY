"""Linear regression: predicting a continuous number (house price) from
features (size, bedrooms, age)."""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Synthetic dataset for demo purposes: [size_sqm, bedrooms, age_years]
rng = np.random.default_rng(42)
n = 200
size = rng.uniform(40, 250, n)
bedrooms = rng.integers(1, 6, n)
age = rng.uniform(0, 40, n)

# Made-up "true" relationship + noise, to fit against
price = 3000 * size + 15000 * bedrooms - 800 * age + rng.normal(0, 20000, n)

X = np.column_stack([size, bedrooms, age])
y = price

# ALWAYS split before fitting - test data must stay unseen until evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("coefficients (size, bedrooms, age):", model.coef_)
print("intercept:", model.intercept_)
print("MAE:", mean_absolute_error(y_test, predictions))
print("R^2:", r2_score(y_test, predictions))

# Predict on a brand-new example
new_house = np.array([[120, 3, 10]])   # 120 sqm, 3 bedrooms, 10 years old
print("predicted price:", model.predict(new_house)[0])
