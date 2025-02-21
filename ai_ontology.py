from flask import Flask, request, jsonify
from benchmarking import main as run_benchmark
from neo4j import GraphDatabase
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Neo4j Connection
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# Function to query ontology from Neo4j
def query_ontology(query):
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]

# Function to generate AI responses
def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI assistant for software engineering."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Route for AI-generated test cases
@app.route("/generate_test_case", methods=["POST"])
def generate_test_case():
    data = request.json
    prompt = f"Generate test cases for the requirement: {data['requirement']}"
    ai_response = generate_text(prompt)
    return jsonify({"test_cases": ai_response})

# Route to query the ontology
@app.route("/query_ontology", methods=["POST"])
def ontology_query():
    data = request.json
    query = data.get("query")
    results = query_ontology(query)
    return jsonify({"ontology_results": results})

# Route to run benchmarks
@app.route("/run_benchmark", methods=["GET"])
def benchmark():
    results = run_benchmark()
    return jsonify({"benchmark_results": results})

if __name__ == "__main__":
    app.run(debug=True)
