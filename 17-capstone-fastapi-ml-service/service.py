"""FastAPI service that loads the trained model once at startup and serves
predictions - the model itself never gets retrained or touched here, this
process only does inference."""

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Iris Classifier Service")

try:
    bundle = joblib.load("model.joblib")
    model = bundle["model"]
    target_names = bundle["target_names"]
except FileNotFoundError:
    model, target_names = None, None


class IrisFeatures(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)


class Prediction(BaseModel):
    species: str
    confidence: float


@app.get("/")
def root():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict", response_model=Prediction)
def predict(features: IrisFeatures):
    if model is None:
        raise HTTPException(
            503, "model not loaded - run train_model.py first to produce model.joblib"
        )

    row = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width,
    ]]
    predicted_class = model.predict(row)[0]
    probabilities = model.predict_proba(row)[0]

    return Prediction(
        species=target_names[predicted_class],
        confidence=round(float(max(probabilities)), 4),
    )
