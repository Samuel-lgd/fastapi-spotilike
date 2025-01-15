from typing import List

from fastapi import Depends, HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.app.schemas import GenreResponse
from backend.app.utils import get_db
from backend.app.models import Genre

router = APIRouter()


@router.get("/api/genres", response_model=List[GenreResponse])
def get_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()

@router.get("/api/genres/{id}", response_model=GenreResponse)
def get_genre(id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

@router.delete("/api/genres/{id}")
def delete_genre(id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == id).first()
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    db.delete(genre)
    db.commit()
    return {"message": "Genre deleted"}
