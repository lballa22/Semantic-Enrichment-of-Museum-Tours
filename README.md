# Smart Museum Tour Using Linked Data Generation


<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1150px-React-icon.svg.png" width="120" height="100" />
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="280" height="100" />
</p>

## Overview
This document presents the Smart Museum Tour project, an initiative leveraging Linked Data and Semantic Web technologies to enhance museum tours. The project involves mapping complex database data to Linked Data through RDF mapping and OWL ontologies, using datasets from the Smithsonian American Art Museum and Museum Of Modern Art.

## Key Features
- **Linked Data Utilization**: Incorporating Linked Open Data (LOD) for improved data structure and accessibility.
- **Enhanced Museum Experience**: Offering new ways of discovering artworks digitally, making museum visits more informative and engaging.
- **Semantic Web Technologies**: Implementing RDF and OWL to map and understand complex datasets.

## Problem Definition
The project addresses the challenge of accessing reliable and consistent data in vast databases, a common issue in museum management and visitor experience enhancement.

## Related Literature
- The paper includes an end-to-end procedure for mapping DB data to Linked Open Data and discusses various models and tools used for data mapping.
- It highlights challenges in data mapping, linking, and validation, particularly in the context of large museum datasets.

## Approach and High-Level System Design
- The system comprises front-end and back-end components, with the front-end developed using React and the back-end using FastAPI frameworks in Python.
- SPARQL queries are executed on an Apache Jena Fuseki server, providing visitors with detailed information about artworks and related pieces in other museums.

## Ontology Design and Visualization
- The project's ontology includes graphical representations of relationships between classes and properties, aiding in understanding the data's structure.

## Data Collection and Pre-Processing
- Data from multiple sources were pre-processed to create uniform datasets, addressing the challenge of merging datasets with different properties.

## Implementation
- The implementation involved data cleaning, preprocessing, ontology creation, and setting up a Fuseki server for SPARQL querying.
- The system integrates front-end and back-end components for seamless user interaction.

## SPARQL Querying
- Custom SPARQL queries were designed to fetch artist and artifact details based on titles and to locate related artworks in different museums.

## Roles and Responsibilities
- The team members contributed to various aspects of the project, including data collection, system design, backend development, and SPARQL query formulation.

## Challenges Faced
- The project encountered challenges in data mapping, importing data into OWL files, and maintaining the Fuseki server.

## Future Scope
- Expansion to include more datasets for richer information.
- Development of a mobile application version of the system.
- Scaling the application to cater to a larger user base.

## Conclusion
The Smart Museum Tour project effectively uses digital technology and Semantic Web tools to enhance the museum experience by providing detailed, linked information about artworks.
>>>>>>> ae2ad25 (Added backend logic to the code)
