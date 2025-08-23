# Music iOS API 

Music API developed with Python's FastAPI framework and deployed on Docker. This API focuses on songs, making the user be able to get and post songs that he likes.

## API Reference

### Welcome Message

**GET /**

Returns a welcome message to test if the API is working.

**Response Example**
```json
{
  "Hi! This is a music API developed by Tono, welcome!, feel free to explore."
}
```

---

### Get All Songs

**GET /api/songs**

Returns a list of all songs available in the API.

**Response Example**
```json
{
  "songs": [
    {
      "id": 1,
      "title": "Song Title",
      "artist": "Artist Name",
      "album": "Album Name",
      "year": 2024,
      "genre": "Genre",
      "image_url": "https://example.com/image.jpg",
      "description": "Song description"
    }
  ]
}
```

---

### Get Song by ID

**GET /api/songs/{song_id}**

Returns the song with the specified ID.

**Path Parameters**
- `song_id` (integer): The ID of the song to retrieve.

**Response Example**
```json
{
  "song": {
    "id": 1,
    "title": "Song Title",
    "artist": "Artist Name",
    "album": "Album Name",
    "year": 2024,
    "genre": "Genre",
    "image_url": "https://example.com/image.jpg",
    "description": "Song description"
  }
}
```

**Error Response (404)**
```json
{
  "detail": "Song not found"
}
```

---

### Create a New Song

**POST /api/songs/**

Creates a new song and adds it to the list.

**Request Body Example**
```json
{
  "id": 2,
  "title": "New Song",
  "artist": "New Artist", 
  "album": "New Album",
  "year": 2025,
  "genre": "Pop",
  "image_url": "https://example.com/new-image.jpg",
  "description": "A new song description"
}
```

**Response Example**
```json
{
  "song": {
    "id": 2,
    "title": "New Song",
    "artist": "New Artist",
    "album": "New Album", 
    "year": 2025,
    "genre": "Pop",
    "image_url": "https://example.com/new-image.jpg",
    "description": "A new song description"
  }
}
```

---

## Song Model

| Field      | Type   | Description         |
|------------|--------|--------------------|
| id         | int    | Song ID            |
| title      | str    | Song title         |
| artist     | str    | Artist name        |
| album      | str    | Album name         |
| year       | int    | Release year       |
| genre      | str    | Genre              |
| image_url  | str    | Image URL          |
| description| str    | Song description   |

---

## Deployment & Usage

This API is deployed using Docker and available as a pre-built image on GitHub Container Registry.

### Running with Docker

Pull and run the pre-built Docker image:

```bash
# Pull the Docker image from GitHub Container Registry
docker pull ghcr.io/bashlui/music-api:latest

# Run the container
docker run -p 8000:8000 ghcr.io/bashlui/music-api:latest
```

### Alternative: Local Development

Start the API server locally:

```bash
cd app
uvicorn main:app --reload
```

### Testing the API

You can test the endpoints using:

1. **Interactive API Documentation**: Access the FastAPI automatic docs at [http://localhost:8000/docs](http://localhost:8000/docs)
2. **Postman**: Import the endpoints into Postman to test all API functionality
3. **curl commands**: Make direct HTTP requests from the command line

#### curl Examples

```bash
# Get welcome message
curl http://localhost:8000/

# Get all songs
curl http://localhost:8000/api/songs

# Get song by ID (replace {song_id} with actual ID)
curl http://localhost:8000/api/songs/1

# Create a new song
curl -X POST http://localhost:8000/api/songs/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "Example Song",
    "artist": "Example Artist",
    "album": "Example Album",
    "year": 2024,
    "genre": "Pop",
    "image_url": "https://example.com/image.jpg",
    "description": "An example song for testing"
  }'
```

The API will be available at `http://localhost:8000` when running with Docker or locally.


