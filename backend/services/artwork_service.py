from SPARQLWrapper import SPARQLWrapper, JSON
from typing import List, Optional
from model.models import ArtworkSearchResult
from constants import SPARQL_SERVER_URL

def build_sparql_query(title: Optional[str], artist_name: Optional[str], classification_name: Optional[str]) -> str:
    """
    Construct the SPARQL query based on the provided search parameters.
    """
    query_parts = []

    if title:
        query_parts.append(f'FILTER regex(?artifactTitle, "{title}")')
    if artist_name:
        query_parts.append(f'FILTER regex(?artistName, "{artist_name}")')
    if classification_name:
        query_parts.append(f'FILTER regex(?classificationName, "{classification_name}")')


    filter_query = " . ".join(query_parts) if query_parts else ""

    return f"""
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX umt: <http://www.semanticweb.org/semantic-museum.owl#>
    SELECT 
        ?artifactId
        ?artifactImage
        ?artifactTitle
        ?artifactWidth
        ?artifactHeight
        ?depth
        ?diameter
        ?department
        ?location
        ?medium
        ?provenance
        ?artistId
        ?artistImage
        ?artistName
        ?birthDate
        ?birthPlace
        ?deathDate
        ?deathPlace
        ?nationality
        ?classificationName
        ?role
    WHERE {{
        ?artifact rdf:type umt:Artifact;
        umt:hasArtifactDepth ?depth;
        umt:hasArtifactDiameter ?diameter;
        umt:hasArtifactHeight ?height;
        umt:hasArtifactID ?artifactId;
        umt:hasArtifactImage ?artifactImage;
        umt:hasArtifactTitle ?artifactTitle;
        umt:hasArtifactWidth ?artifactWidth;
        umt:hasDepartment ?department;
        umt:hasLocation ?location;
        umt:hasMedium ?medium;
        umt:hasProvenance ?provenance;
        umt:hasArtist ?artist;
        umt:hasClassification ?classification;
        umt:hasRole ?role.


        ?artist rdf:type umt:Artist;
        umt:hasArtistID ?artistId;
        umt:hasArtistImage ?artistImage;
        umt:hasArtistName ?artistName;
        umt:hasBirthDate ?birthDate;
        umt:hasBirthPlace ?birthPlace;
        umt:hasDeathDate ?deathDate;
        umt:hasDeathPlace ?deathPlace;
        umt:hasNationality ?nationality.


        ?classification rdf:type umt:Classification;
        umt:hasClassificationName ?classificationName.

        {filter_query}
    }}
    LIMIT 30000
    """

def execute_sparql_query(query: str):
    """
    Execute the SPARQL query and return the results.
    """
    sparql = SPARQLWrapper(SPARQL_SERVER_URL)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

def map_results_to_model(results):
    """
    Map the SPARQL query results to the ArtworkSearchResult model.
    """
    artworks = []
    for r in results['results']['bindings']:
        try:
            artwork = ArtworkSearchResult(
                artifactId=r.get('artifactId', {}).get('value'),
                artifactImage=r.get('artifactImage', {}).get('value'),
                artifactTitle=r.get('artifactTitle', {}).get('value'),
                artifactWidth=r.get('artifactWidth', {}).get('value'),
                artifactHeight=r.get('artifactHeight', {}).get('value'),
                depth=r.get('depth', {}).get('value'),
                diameter=r.get('diameter', {}).get('value'),
                department=r.get('department', {}).get('value'),
                location=r.get('location', {}).get('value'),
                medium=r.get('medium', {}).get('value'),
                provenance=r.get('provenance', {}).get('value'),
                artistId=r.get('artistId', {}).get('value'),
                artistImage=r.get('artistImage', {}).get('value'),
                artistName=r.get('artistName', {}).get('value'),
                birthDate=r.get('birthDate', {}).get('value'),
                birthPlace=r.get('birthPlace', {}).get('value'),
                deathDate=r.get('deathDate', {}).get('value'),
                deathPlace=r.get('deathPlace', {}).get('value'),
                nationality=r.get('nationality', {}).get('value'),
                role=r.get('role', {}).get('value'),
                classificationName=r.get('classificationName', {}).get('value')
            )
            artworks.append(artwork)
        except KeyError:
            pass
    return artworks

def search_artwork(title: Optional[str] = None, artist_name: Optional[str] = None, classification_name: Optional[str] = None) -> List[ArtworkSearchResult]:
    """
    Perform artwork search based on given parameters.
    """
    query = build_sparql_query(title, artist_name, classification_name)
    results = execute_sparql_query(query)
    return map_results_to_model(results)
