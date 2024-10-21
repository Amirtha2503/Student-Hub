from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# CORS (Allow frontend to access the API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PostgreSQL connection
conn = psycopg2.connect(
    dbname="DBNAME", user="USERNAME", password="PASSWORD", host="localhost"
)
cursor = conn.cursor()

# User model
class User(BaseModel):
    username: str
    password: str

@app.post("/register")
async def register(user: User):
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user.username, user.password))
    conn.commit()
    return {"message": "User registered successfully"}

@app.post("/login")
async def login(user: User):
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (user.username, user.password))
    result = cursor.fetchone()
    if result:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}
