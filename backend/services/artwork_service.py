from SPARQLWrapper import SPARQLWrapper, JSON
from typing import List, Optional
from model.models import ArtworkSearchResult
from constants import SPARQL_SERVER_URL

def build_sparql_query(title: Optional[str], artist_name: Optional[str], medium: Optional[str], museum_name: Optional[str]) -> str:
    """
    Construct the SPARQL query based on the provided search parameters.
    """
    query_parts = []

    if title:
        query_parts.append(f'FILTER regex(?title, "{title}")')
    if artist_name:
        query_parts.append(f'FILTER regex(?artistName, "{artist_name}")')
    if medium:
        query_parts.append(f'FILTER regex(?medium, "{medium}")')
    if museum_name:
        query_parts.append(f'FILTER regex(?museumName, "{museum_name}")')

    filter_query = " . ".join(query_parts) if query_parts else ""

    return f"""
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX umt: <http://www.semanticweb.org/artifact#>
    SELECT ?artistName ?title ?artworkID ?productionYear ?dimensions ?description ?classification ?imageUrl ?width ?height ?nationality ?site ?room ?museumName ?lifePeriod ?artistDesc ?artistImageUrl ?medium 
    WHERE {{
        ?art rdf:type umt:Artifact;
        umt:hasTitle ?title;
        umt:isCreatedBy ?art2;
        umt:hasMedium ?medium;
        umt:hasDate ?productionYear;
        umt:hasArtifactID ?artworkID;
        umt:hasDimensions ?dimensions;
        umt:hasDescription ?description;
        umt:hasClassification ?classification;
        umt:hasImage ?imageUrl;
        umt:hasHeight ?height;
        umt:hasWidth ?width;
        umt:hasSite ?site;
        umt:hasRoom ?room;
        umt:hasMuseumName ?museumName.
    
    
        ?art2 rdf:type umt:Artist;
        umt:hasArtistName ?artistName;
        umt:hasNationality ?nationality;
        umt:hasLifeperiod ?lifePeriod;
        umt:hasArtistDescr ?artistDesc;
        umt:hasArtistImage ?artistImageUrl.
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
                artistName=r['artistName']['value'],
                artworkTitle=r['title']['value'],
                artworkWidth=r.get('width', {}).get('value'),
                artworkImage=r['imageUrl']['value'],
                artworkId=r['artworkID']['value'],
                productionYear=r['productionYear']['value'],
                nationality=r['nationality']['value'],
                site=r["site"]['value'],
                room=r["room"]['value'],
                museumName=r['museumName']['value'],
                lifePeriod=r["lifePeriod"]["value"],
                artistDesc=r['artistDesc']['value'],
                artistImage=r["artistImageUrl"]['value'],
                medium=r['medium']['value'],
                # ... map other fields as needed ...
            )
            artworks.append(artwork)
        except KeyError:
            pass
    return artworks

def search_artwork(title: Optional[str] = None, artist_name: Optional[str] = None, medium: Optional[str] = None, museum_name: Optional[str] = None) -> List[ArtworkSearchResult]:
    """
    Perform artwork search based on given parameters.
    """
    query = build_sparql_query(title, artist_name, medium, museum_name)
    results = execute_sparql_query(query)
    return map_results_to_model(results)
