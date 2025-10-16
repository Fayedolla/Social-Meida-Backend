from fastapi import FastAPI, APIRouter
from .Database import engine
from .config import settings
from .Routers import posts, users, votes, auth

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(votes.router)