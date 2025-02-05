from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
from backend.app.utils import engine

Base = declarative_base()


class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    cover_image = Column(String)
    release_date = Column(String)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    artist = relationship("Artist", back_populates="albums")
    songs = relationship("Song", back_populates="album")


class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    duration = Column(String)
    genre_id = Column(Integer, ForeignKey("genres.id"))
    artist_id = Column(Integer, ForeignKey("artist.id"))
    album_id = Column(Integer, ForeignKey("albums.id"))
    album = relationship("Album", back_populates="songs")


class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    avatar = Column(String)
    biography = Column(String)
    albums = relationship("Album", back_populates="artist")


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


Base.metadata.create_all(bind=engine)
