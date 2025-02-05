from datetime import date, time

from pydantic import BaseModel, ConfigDict


class AlbumBase(BaseModel):
    title: str
    cover_image: str
    release_date: date
    artist_id: int


class AlbumCreate(AlbumBase):
    pass


class AlbumResponse(AlbumBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ArtistBase(BaseModel):
    name: str
    avatar: str
    biography: str

class ArtistCreate(ArtistBase):
    pass

class ArtistResponse(ArtistBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class GenreBase(BaseModel):
    title: str
    description: str
    
    
class GenreCreate(GenreBase):
    pass


class GenreResponse(GenreBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SongBase(BaseModel):
    title: str
    duration: str
    album_id: int


class SongResponse(SongBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
