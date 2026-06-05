"""A minimal FastAPI app demonstrating JWT-based authentication:
signup -> login (get a token) -> access a protected route with the token."""

import datetime
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
import jwt

SECRET_KEY = "dev-only-secret-change-me"   # in real apps: load from env vars
ALGORITHM = "HS256"

app = FastAPI(title="JWT Auth Demo")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# in-memory user store for this demo
users_db: dict[str, dict] = {}


def create_access_token(username: str) -> str:
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/signup")
def signup(username: str, password: str):
    if username in users_db:
        raise HTTPException(400, "user already exists")
    users_db[username] = {"hashed_password": pwd_context.hash(password)}
    return {"message": "user created"}


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(401, "incorrect username or password")
    token = create_access_token(form_data.username)
    return {"access_token": token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "invalid token")
    if username not in users_db:
        raise HTTPException(401, "user not found")
    return username


@app.get("/me")
def read_current_user(username: str = Depends(get_current_user)):
    # this route is "protected" - it 401s without a valid Bearer token
    return {"username": username}
