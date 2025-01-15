from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from backend.app.schemas import ArtistResponse
from backend.app.utils import get_db
from backend.app.models import Artist

router = APIRouter()


@router.get("/api/artists", response_model=List[ArtistResponse])
def get_artists(db: Session = Depends(get_db)):
    return db.query(Artist).all()

@router.get("/api/artists/{id}", response_model=ArtistResponse)
def get_artist(id: int, db: Session = Depends(get_db)):
    artist = db.query(Artist).filter(Artist.id == id).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@router.delete("/api/artists/{id}")
def delete_artist(id: int, db: Session = Depends(get_db)):
    artist = db.query(Artist).filter(Artist.id == id).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    db.delete(artist)
    db.commit()
    return {"message": "Artist deleted"}