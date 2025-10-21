from fastapi import FastAPI, APIRouter
from .Database import engine
from .config import settings
from .Routers import posts, users, votes, auth
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],
)


app.include_router(users.router)
app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(votes.router)


@app.get("/")
def root():
    return {"message": "Social Media Backend API is running successfully on Azure!"}
