from fastapi import FastAPI
from backend.app.routers import albums, users, artists, genres
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(albums.router)
app.include_router(users.router)
app.include_router(artists.router)
app.include_router(genres.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)