from fastapi import APIRouter, Form
from typing import Optional
from model.models import SearchResponse
from services import artwork_service

router = APIRouter()

@router.post("/search", response_model=SearchResponse)
async def search_artwork(
    title: Optional[str] = Form(None),
    artist_name: Optional[str] = Form(None),
    classification_name: Optional[str] = Form(None)
):
    results = artwork_service.search_artwork(title, artist_name, classification_name)
    print(results)
    return SearchResponse(results=results)
