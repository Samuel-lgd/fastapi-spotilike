from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from backend.app.schemas import ArtistResponse, SongResponse, ArtistCreate
from backend.app.utils import get_db
from backend.app.models import Artist, Song, Album

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


@router.post("/api/artists", response_model=ArtistResponse)
def create_artist(artist: ArtistCreate, db: Session = Depends(get_db)):
    db_artist = Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

@router.put("/api/artists/edit/{id}", response_model=ArtistResponse)
def update_artist(id: int, artist: ArtistCreate, db: Session = Depends(get_db)):
    db_artist = db.query(Artist).filter(Artist.id == id).first()
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")

    for key, value in artist.dict().items():
        setattr(db_artist, key, value)

    db.commit()    
    db.refresh(db_artist) 
    return db_artist


@router.get("/api/artists/{id}/songs", response_model=List[SongResponse])
def get_artist_songs(id: int, db: Session = Depends(get_db)):
    artist = db.query(Artist).filter(Artist.id == id).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")

    songs = db.query(Song).filter(Song.artist_id == id).all()
    
    return [SongResponse.from_orm(song).model_dump() for song in songs] # ne marche pas

@router.delete("/api/artists/{id}")
def delete_artist(id: int, db: Session = Depends(get_db)):
    artist = db.query(Artist).filter(Artist.id == id).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    db.delete(artist)
    db.commit()
    return {"message": "Artist deleted"}