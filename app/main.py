from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

@app.get("/")
async def read_root():
    return {"Hi! This is a music API developed by Tono, welcome!, feel free to explore."}

# Method to request the list of songs
@app.get("/api/songs")
async def read_songs():
    return {"songs": songs}

# Method to get song or songs by ID
@app.get("/api/songs/{song_id}")
async def read_song(song_id: int):
    song = next((s for s in songs if s.id == song_id), None)
    if song:
        return {"song": song}
    raise HTTPException(status_code=404, detail="Song not found")

# Method to create a new song
@app.post("/api/songs/")
async def create_song(song: Song):
    songs.append(song)
    return {"song": song}

