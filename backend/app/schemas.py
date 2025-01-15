from datetime import date, time

from pydantic import BaseModel


class AlbumBase(BaseModel):
    title: str
    cover_image: str
    release_date: date
    artist_id: int


class AlbumCreate(AlbumBase):
    pass


class AlbumResponse(AlbumBase):
    id: int

    class Config:
        orm_mode = True


class ArtistBase(BaseModel):
    name: str
    avatar: str
    biography: str


class ArtistResponse(ArtistBase):
    id: int

    class Config:
        orm_mode = True


class GenreBase(BaseModel):
    title: str
    description: str


class GenreResponse(GenreBase):
    id: int

    class Config:
        orm_mode = True


class SongBase(BaseModel):
    title: str
    duration: str
    album_id: int


class SongResponse(SongBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
