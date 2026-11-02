# Laptop Recommendation Expert System

A rule-based expert system developed in Python for recommending laptops based on user preferences. This project demonstrates the use of **forward chaining**, an inference technique used in artificial intelligence.

## Project Overview

The system asks users a series of questions about their laptop preferences, including budget, portability, battery life, gaming, and performance requirements.

Based on the answers, the system evaluates a knowledge base of IF–THEN rules and generates appropriate laptop recommendations.

## Features

- Rule-based inference using forward chaining.
- Knowledge base containing 10 laptop recommendation rules.
- User input collection and fact generation.
- Rule prioritization when multiple rules can fire.
- Inference trace showing which rules were triggered.
- Automated unit tests using Python's `unittest` framework.

## Project Structure

```text
Expert-System-Project/
│
├── engine.py
├── main.py
├── kb_loader.py
│
├── kb/
│   └── laptop_rules.json
│
└── tests/
    ├── README.txt
    └── test_engine.py
```

## How It Works

The expert system follows these steps:

1. Collects user preferences through questions.
2. Converts user responses into facts.
3. Loads the rules from the JSON knowledge base.
4. Evaluates rules using forward chaining.
5. Adds new conclusions to working memory.
6. Continues until no additional rules can fire.
7. Displays laptop recommendations and the rules that produced them.

### Example Rule

**IF:**
- Budget is high.
- Portability is important.
- Long battery life is required.

**THEN:**
- Recommend a Premium Ultrabook.

## Available Recommendations

The knowledge base currently supports the following laptop categories:

1. Premium Ultrabook
2. Budget Laptop
3. Gaming Laptop
4. Professional Workstation
5. Student Laptop
6. Business Ultrabook
7. Travel Laptop
8. Everyday Laptop
9. Performance Laptop
10. Affordable Ultrabook

## Requirements

- Python 3.x
- No external Python packages are required.

## Running the Program

Open a terminal in the project's root directory and run:

```bash
python main.py
```

Answer the questions presented by the program to receive laptop recommendations.

## Running the Tests

The project includes automated tests to verify the inference engine.

Run the following command from the project's root directory:

```bash
python -m unittest discover -s tests -v
```

The test suite currently contains four tests covering:

- Rule activation.
- Missing antecedents.
- Forward-chaining inference.
- Conclusion categorization.

**Current test result: 4 out of 4 tests passing.**

## Technologies Used

- Python
- JSON
- Rule-Based Systems
- Forward Chaining
- Python Unittest

## Project Purpose

This project was developed as a mini project for an Artificial Intelligence course to demonstrate knowledge representation, rule-based reasoning, and forward-chaining inference.