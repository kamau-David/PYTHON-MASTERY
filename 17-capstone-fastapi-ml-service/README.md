# 17 — Capstone: FastAPI ML Service

Ties Track 2 (backend/APIs) and Track 3 (data/AI) together: train a small
model, save it to disk, then serve predictions from a FastAPI endpoint -
the same basic shape as a real production ML service.

## Files
- `train_model.py` — trains a classifier and saves it with joblib
- `service.py` — FastAPI app that loads the model and serves `/predict`
- `requirements.txt`

## Run
```bash
pip install -r requirements.txt
python3 train_model.py          # produces model.joblib
uvicorn service:app --reload
# visit http://127.0.0.1:8000/docs and try POST /predict
```
