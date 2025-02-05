from typing import List

from fastapi import Depends, HTTPException, APIRouter

from sqlalchemy.orm import Session
from backend.app.schemas import AlbumResponse, SongResponse, AlbumCreate
from backend.app.utils import get_db
from backend.app.models import Album

router = APIRouter()


@router.get("/api/albums", response_model=List[AlbumResponse])
def get_albums(db: Session = Depends(get_db)):
    return db.query(Album).all()


@router.get("/api/albums/{id}", response_model=AlbumResponse)
def get_album(id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album


@router.get("/api/albums/{id}/songs", response_model=List[SongResponse])
def get_album_songs(id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album.songs


@router.post("/api/albums", response_model=AlbumResponse)
def create_album(album: AlbumCreate, db: Session = Depends(get_db)):
    db_album = Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

@router.put("/api/albums/edit/{id}", response_model=AlbumResponse)
def update_album(id: int, album: AlbumCreate, db: Session = Depends(get_db)):
    db_album = db.query(Album).filter(Album.id == id).first()
    if not db_album:
        raise HTTPException(status_code=404, detail="Album not found")

    for key, value in album.dict().items():
        setattr(db_album, key, value)

    db.commit()    
    db.refresh(db_album) 
    return db_album


@router.delete("/api/albums/{id}")
def delete_album(id: int, db: Session = Depends(get_db)):
    album = db.query(Album).filter(Album.id == id).first()
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    db.delete(album)
    db.commit()
    return {"message": "Album deleted"}
