from pydantic import BaseModel
from typing import List, Optional

class ArtworkSearchResult(BaseModel):
    artistName: Optional[str] = None
    artworkTitle: Optional[str] = None
    artworkWidth: Optional[str] = None
    artworkImage: Optional[str] = None
    artworkId: Optional[int] = None
    productionYear: Optional[str] = None
    nationality: Optional[str] = None
    site: Optional[str] = None
    room: Optional[int] = None
    museumName: Optional[str] = None
    lifePeriod: Optional[str] = None
    artistDesc: Optional[str] = None
    artistImage: Optional[str] = None
    medium: Optional[str] = None
    # ... other fields ...

class SearchResponse(BaseModel):
    results: Optional[List[ArtworkSearchResult]] = None
