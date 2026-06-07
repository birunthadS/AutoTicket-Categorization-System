# AI Usage Note

## Project Title

Auto Ticket Categorization System

## AI Model Used

* Llama 3.2
* Ollama

## AI Techniques Used

* Prompt Engineering
* Few-Shot Prompting
* Natural Language Processing (NLP)
* Structured JSON Output Generation
* Rule-Based Validation

## Purpose of AI

The AI model analyzes IT service desk ticket subjects and descriptions and automatically predicts:

* Category
* Subcategory
* Priority
* Reason for classification

## Workflow

1. User submits a ticket.
2. FastAPI receives the request.
3. The ticket is sent to the Llama 3.2 model.
4. The model classifies the ticket using predefined categories and examples.
5. The output is validated using business rules.
6. The result is stored and displayed on the dashboard.

## Benefits

* Reduces manual ticket tagging effort.
* Improves categorization consistency.
* Supports faster ticket routing.
* Provides explainable classification results.

## Technologies

* FastAPI
* Python
* Ollama
* Llama 3.2
* HTML
* CSS
* JSON
