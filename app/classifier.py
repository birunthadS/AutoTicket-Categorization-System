import json
import ollama

from app.prompts import CLASSIFICATION_PROMPT
from app.validator import validate_classification


def classify_ticket(subject, description, api_key=None):

    prompt = f"""
{CLASSIFICATION_PROMPT}

Ticket Subject:
{subject}

Ticket Description:
{description}

Return ONLY valid JSON.
"""

    try:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = response["message"]["content"].strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        result = json.loads(text)

        if validate_classification(result):
            return result

        return {
            "category": "Service Request",
            "subcategory": "Access Request",
            "priority": "Medium",
            "reason": "Ticket content could not be mapped to a valid supported category."
        }

    except Exception as e:

        print("OLLAMA ERROR:", str(e))

        return {
            "category": "Service Request",
            "subcategory": "Access Request",
            "priority": "Medium",
            "reason": f"Processing error: {str(e)}"
        }