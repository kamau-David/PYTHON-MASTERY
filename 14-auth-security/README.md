# 14 — Auth & Security

Password hashing and JWT-based authentication protecting a FastAPI route.

## Files
- `password_hashing.py` — why you never store plaintext passwords, using bcrypt
- `jwt_auth.py` — a minimal FastAPI app with signup/login/protected route
- `requirements.txt`

## Run
```bash
pip install -r requirements.txt
python3 password_hashing.py
uvicorn jwt_auth:app --reload
```
