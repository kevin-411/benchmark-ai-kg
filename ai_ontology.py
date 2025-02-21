from flask import Flask, request, jsonify
from py2neo import Graph
from transformers import pipeline
import benchmarking  # Importing the benchmarking script
import rdflib

# Initialize Flask app
app = Flask(__name__)

# Connect to Neo4j
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "<neo4j password here>"
graph = Graph(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Load ontology from TTL file
def load_ontology(ttl_file):
    g = rdflib.Graph()
    g.parse(ttl_file, format="ttl")
    for subj, pred, obj in g:
        graph.run("MERGE (:Entity {subject: $subj, predicate: $pred, object: $obj})", 
                  subj=str(subj), pred=str(pred), obj=str(obj))

# Initialize Generative AI Model
generative_model = pipeline("text-generation", model="gpt-3.5-turbo")

@app.route("/generate_test_case", methods=["POST"])
def generate_test_case():
    data = request.json
    requirement = data.get("requirement", "")
    
    # Use AI model to generate test case
    response = generative_model(requirement, max_length=100, num_return_sequences=1)
    test_case = response[0]["generated_text"]
    
    # Store test case in Neo4j
    graph.run("CREATE (:TestCase {description: $desc})", desc=test_case)
    
    return jsonify({"generated_test_case": test_case})

@app.route("/query_ontology", methods=["GET"])
def query_ontology():
    query = "MATCH (e:Entity) RETURN e.subject, e.predicate, e.object LIMIT 10"
    results = graph.run(query).data()
    return jsonify(results)

@app.route("/benchmark", methods=["GET"])
def run_benchmark():
    benchmarking.main()
    return jsonify({"message": "Benchmarking completed. Check console output."})

if __name__ == "__main__":
    load_ontology("ontology.ttl")  # Load ontology from TTL file
    app.run(debug=True)
