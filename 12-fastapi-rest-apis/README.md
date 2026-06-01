# 12 — FastAPI REST APIs

A CRUD REST API with FastAPI and Pydantic - includes automatic request
validation and interactive docs out of the box.

## Files
- `main.py` — the FastAPI app with full CRUD for a "tasks" resource
- `requirements.txt`

## Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
# visit http://127.0.0.1:8000/docs for interactive Swagger UI
```
