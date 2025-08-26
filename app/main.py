from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import Query
from typing import List

app = FastAPI()

class Song(BaseModel):
    id: int
    title: str
    artist: str
    album: str
    year: int
    genre: str
    image_url: str
    description: str
    
# Sample data
songs: list[Song] = []

@app.get("/api/songs", response_model=List[Song])
async def read_songs():
    return songs

@app.get("/api/songs/{song_id}", response_model=Song)
async def read_song(song_id: int):
    song = next((s for s in songs if s.id == song_id), None)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@app.post("/api/song", response_model=Song)
async def create_song(song: Song):
    if any(s.id == song.id for s in songs):
        raise HTTPException(status_code=400, detail="Song with this ID already exists")
    songs.append(song)
    return song

@app.get("/api/songs/search", response_model=List[Song])
async def search_songs(q: str = Query(..., min_length=1)):
    ql = q.lower()
    return [s for s in songs if ql in s.title.lower()
                             or ql in s.artist.lower()
                             or ql in s.album.lower()
                             or ql in s.genre.lower()]
