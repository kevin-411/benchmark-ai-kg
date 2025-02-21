from rdflib import Graph
from neo4j import GraphDatabase

# Neo4j connection details
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

# Load ontology from an OWL file
def load_ontology(owl_file):
    g = Graph()
    g.parse(owl_file, format="xml")
    return g

# Convert RDF triples to Neo4j nodes and relationships
def rdf_to_neo4j(graph, neo4j_session):
    for subj, pred, obj in graph:
        neo4j_session.run(
            "MERGE (s:Resource {uri: $subj}) "
            "MERGE (o:Resource {uri: $obj}) "
            "MERGE (s)-[:RELATES_TO {predicate: $pred}]->(o)",
            subj=str(subj), pred=str(pred), obj=str(obj)
        )

# Main function
def main(owl_file):
    ontology_graph = load_ontology(owl_file)
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    with driver.session() as session:
        rdf_to_neo4j(ontology_graph, session)
    
    driver.close()
    print("Ontology loaded successfully into Neo4j!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python load_ontology.py <ontology.owl>")
    else:
        main(sys.argv[1])
