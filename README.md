# Auto Ticket Categorization System

## Project Overview

Auto Ticket Categorization System is an AI-powered application that automatically classifies IT service desk tickets into predefined categories, subcategories, and priorities. The system helps reduce manual effort, improve consistency, and speed up ticket routing.


## Problem Statement

Manual ticket categorization is time-consuming and inconsistent. Support teams often spend significant effort identifying the correct category and priority for incoming tickets.

This project automates the process using Artificial Intelligence.


## Features

* Automatic ticket categorization
* Subcategory prediction
* Priority assignment
* AI-generated reasoning
* Dashboard analytics
* Prediction logs
* Search functionality
* CSV log export
* Responsive web interface


## AI Techniques Used

* Prompt Engineering
* Few-Shot Prompting
* Natural Language Processing (NLP)
* Rule-Based Validation
* Structured JSON Output


## Technology Stack

### Backend

* Python
* FastAPI
* Ollama
* Llama 3.2

### Frontend

* HTML
* CSS
* JavaScript

### Data Storage

* JSON
* CSV


## Project Structure

Auto-Ticket-Categorization/

app/

* classifier.py
* main.py
* prompts.py
* validator.py

data/

* examples.json
* tickets.json
* prediction_logs.csv
* sample_data.csv

docs/

* AI_USAGE_NOTE.md
* PROMPTS_USED.md
* TEST_CASES.md

static/

* style.css

templates/

* dashboard.html
* classify.html
* history.html

requirements.txt



## Installation

1. Clone the repository

2. Install dependencies

pip install -r requirements.txt

3. Start Ollama

ollama run llama3.2

4. Run the application

uvicorn app.main:app --reload

5. Open browser

http://127.0.0.1:8000



## Workflow

1. User submits ticket.
2. FastAPI receives request.
3. Llama 3.2 analyzes subject and description.
4. Category, subcategory, and priority are predicted with AI analysis.
5. Output is validated.
6. Results are stored in logs.
7. Dashboard displays statistics.


## 🎬 Demo Videos

### Project Demonstration
📺 **YouTube Demo**
https://youtu.be/UUNEOGkEzl4

📁 **Full Demo Recordings**
https://drive.google.com/drive/folders/1DCCYuT6jVC8FS40e-bJpy8mWkm0Tgdbv?usp=drive_link



## Future Enhancements

* Real-time notifications
* Email integration
* Ticket routing automation
* User authentication
* Advanced analytics dashboard
* Multi-language support

## Team Members

1. Birunthadevi S
2. Bowyashree K
3. Darsan V
4. Priyadharshini D
