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

Install dependencies using:

`pip install pandas numpy scikit-learn`

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

## License

This project is licensed under the MIT License.

## Contact

For issues or contributions, reach out to me at k.odhiambo@students.jkuat.ac.ke