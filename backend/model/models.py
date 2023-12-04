from pydantic import BaseModel
from typing import List, Optional

class ArtworkSearchResult(BaseModel):
    artifactId: Optional[str] = None
    artifactImage: Optional[str] = None
    artifactTitle: Optional[str] = None
    artifactWidth: Optional[str] = None
    artifactHeight: Optional[str] = None
    depth: Optional[str] = None
    diameter: Optional[str] = None
    department: Optional[str] = None
    location: Optional[str] = None
    medium: Optional[str] = None
    provenance: Optional[str] = None
    artistId: Optional[str] = None
    artistImage: Optional[str] = None
    artistName: Optional[str] = None
    birthDate: Optional[str] = None
    birthPlace: Optional[str] = None
    deathDate: Optional[str] = None
    deathPlace: Optional[str] = None
    nationality: Optional[str] = None
    classificationName: Optional[str] = None

class SearchResponse(BaseModel):
    results: Optional[List[ArtworkSearchResult]] = None
