# Benchmarking AI-KG Hybrid System for Software Quality Control

## Overview

This project evaluates the performance of an AI-KG (Artificial Intelligence + Knowledge Graph) hybrid system 
against traditional rule-based methods for software quality control. 
The benchmarking script assesses precision, recall, F1-score, and execution time using a dataset of software defects and test cases.

## Features

- Automated benchmarking of AI-generated test cases.

- Comparison between AI-KG hybrid system and traditional methods.

- Dataset integration for real-world evaluation.

- Execution time measurement for performance analysis.

## Prerequisites

Ensure the following dependencies are installed:

- Python 3.8+

- Pandas

- NumPy

- scikit-learn

- Flask

- Neo4j

- pip (Python package manager)

- Docker (optional, for containerization)

Install dependencies using:

`pip install pandas numpy scikit-learn flask`

Setup

1. Clone the Repository

`git clone https://github.com/kevin-411/benchmark-ai-kg.git`
`cd benchmark-ai-kg`


2. Prepare the Dataset

Ensure you have a CSV file (benchmark_dataset.csv) with the following columns:

actual_defects (0 or 1 indicating real defects)

predicted_ai_kg (0 or 1 predictions from AI-KG system)

predicted_traditional (0 or 1 predictions from the traditional method)

Place this file in the project directory.

3. Run the Benchmarking Script

Execute the following command:

`python benchmark.py`

## Output

The script will display benchmarking results, including:

Precision, Recall, and F1-score for AI-KG and Traditional methods.

Execution time for each method.

Overall benchmark execution time.

## Setting Up Neo4j

1. Start Neo4j locally:

`neo4j console`

or using Docker:

`docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j:latest`

Load the ontology into Neo4j:

`python scripts/load_ontology.py ontology.owl`

## Running the Flask Server

Start the Flask API server:

`python ai_ontology.py`

By default, it runs on [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## API Endpoints

1. Generate Test Cases

Endpoint: `POST /generate-test-cases`

- Parameters:

  - `requirement`: (string) Software requirement description

- Example Request:

```curl -X POST "http://127.0.0.1:5000/generate-test-cases" \
     -H "Content-Type: application/json" \
     -d '{"requirement": "The system should allow user login via OAuth."}' 
	 ```

- Response:

```{
    "test_cases": [
        "Verify login with valid OAuth credentials",
        "Verify login with expired OAuth token",
        "Verify login with incorrect credentials"
    ]
}
```

2. Detect Defects

Endpoint: `POST /detect-defects`

- Parameters:

  - `code_snippet`: (string) Code to analyze

- Example Request:

```curl -X POST "http://127.0.0.1:5000/detect-defects" \
     -H "Content-Type: application/json" \
     -d '{"code_snippet": "def divide(a, b): return a / b"}'
	 ```

- Response:

```{
    "defects": [
        {
            "type": "ZeroDivisionError",
            "suggestion": "Ensure denominator is checked before division."
        }
    ]
}
```

3. Query the Ontology

- Endpoint: `GET /query-ontology`

- Parameters:

  - `query`: (string) Cypher query

- Example Request:

`curl -G "http://127.0.0.1:5000/query-ontology" --data-urlencode "query=MATCH (n) RETURN n LIMIT 10"`

- Response:

```{
    "results": [
        {"name": "SoftwareRequirement", "description": "A structured requirement node."}
    ]
}
```


## License

This project is licensed under the MIT License.

## Contact

For issues or contributions, reach out to me at k.odhiambo@students.jkuat.ac.ke