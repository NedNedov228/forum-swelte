from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel , validator
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
isAuth = False

# CORS middleware setup
origins = [
    "http://localhost:5000", 
    "http://localhost:5173", 
    "http://37.26.14.48:5173"
]

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    @validator('username')
    def username_must_contain_space(cls, v):
        if ' ' in v:
            raise ValueError('username must not contain a space')
        return v
    @validator('password')
    def password_must_contain_space(cls, v):
        if ' ' in v:
            raise ValueError('password must not contain a space')
        return v


db = []


@app.post("/auth/register/")
async def create_user(user: User):
    db.append(user.dict())
    print(db)
    return {"username": user.username, "email": user.email}

@app.post("/auth/login/")
async def login_user(user: User):
    for i in db:
        if i['username'] == user.username and i['password'] == user.password:
            global isAuth
            isAuth = True
            return {"username": user.username, "email": user.email}
    return HTTPException(status_code=400, detail="Invalid username or password")
    
