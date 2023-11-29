# Artwork Search Backend API

## Overview
This project is a FastAPI-based backend service designed to search for artwork information. It utilizes SPARQL queries to fetch data from a RDF database, providing a flexible API endpoint for searching artworks by various criteria such as title, artist name, medium, and museum name.

## Features
- Search for artworks with various filters (title, artist name, etc.).
- Modular architecture for easy maintenance and scalability.
- Integration with a SPARQL endpoint for querying RDF data.

## Installation

### Prerequisites
- Python 3.8 or higher
- SPARQL endpoint running and accessible

### Setup
1. Clone the repository:
   ```bash
   git clone [URL of the repository]
   cd [repository name]
   ```

2. Install required packages:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

### Running the Server
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`.

## Usage

### API Endpoints
- **POST `/search`**: Search for artworks.
  - Parameters (sent as form data):
    - `title` (optional): Title of the artwork.
    - `artist_name` (optional): Name of the artist.
    - `medium` (optional): Medium of the artwork.
    - `museum_name` (optional): Name of the museum.

### Example Request
```bash
curl -X POST "http://localhost:8000/search" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -F "title=Mona Lisa" \
     -F "artist_name=Leonardo da Vinci"
```

## Project Structure
- `main.py`: Entry point for the FastAPI application.
- `models.py`: Defines Pydantic models for data validation.
- `services/artwork_service.py`: Contains the business logic for artwork search.
- `routers/artwork_router.py`: Defines the API routes for artwork search.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.