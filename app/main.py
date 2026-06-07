import os
import json
import csv
from fastapi.responses import FileResponse
from datetime import datetime


from pydantic import BaseModel
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

from app.classifier import classify_ticket

load_dotenv()

app = FastAPI(title="AI Ticket Categorization System")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

TICKETS_FILE = "data/tickets.json"


class TicketRequest(BaseModel):
    ticket_id: str
    subject: str
    description: str


def load_tickets():
    if not os.path.exists(TICKETS_FILE):
        return []

    try:
        with open(TICKETS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return []


def save_ticket(ticket):
    tickets = load_tickets()
    tickets.append(ticket)

    with open(TICKETS_FILE, "w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):

    tickets = load_tickets()

    total = len(tickets)

    high = len([t for t in tickets if t.get("priority") == "High"])
    medium = len([t for t in tickets if t.get("priority") == "Medium"])
    low = len([t for t in tickets if t.get("priority") == "Low"])

    recent = sorted(
        tickets,
        key=lambda x: x.get("timestamp", ""),
        reverse=True
    )[:5]

    category_counts = {}

    for ticket in tickets:
        category = ticket.get("category", "Unknown")

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "total": total,
            "high": high,
            "medium": medium,
            "low": low,
            "recent": recent,
            "category_counts": category_counts
        }
    )


@app.get("/classify", response_class=HTMLResponse)
async def classify_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="classify.html",
        context={
            "result": None
        }
    )


@app.post("/classify", response_class=HTMLResponse)
async def classify_ticket_page(
    request: Request,
    ticket_id: str = Form(...),
    subject: str = Form(...),
    description: str = Form(...)
):

    result = classify_ticket(
        subject,
        description,
        None
    )

    ticket = {
        "ticket_id": ticket_id,
        "subject": subject,
        "description": description,
        "category": result["category"],
        "subcategory": result["subcategory"],
        "priority": result["priority"],
        "reason": result["reason"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_ticket(ticket)

    return templates.TemplateResponse(
        request=request,
        name="classify.html",
        context={
            "result": ticket
        }
    )


@app.get("/history", response_class=HTMLResponse)
async def history(request: Request):

    tickets = load_tickets()

    tickets = sorted(
        tickets,
        key=lambda x: x.get("timestamp", ""),
        reverse=True
    )

    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "tickets": tickets
        }
    )
@app.get("/download-logs")
async def download_logs():

    tickets = load_tickets()

    csv_file = "data/prediction_logs.csv"

    with open(csv_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Ticket ID",
            "Subject",
            "Description",
            "Category",
            "Subcategory",
            "Priority",
            "Timestamp"
        ])

        for ticket in tickets:

            writer.writerow([
                ticket.get("ticket_id"),
                ticket.get("subject"),
                ticket.get("description"),
                ticket.get("category"),
                ticket.get("subcategory"),
                ticket.get("priority"),
                ticket.get("timestamp")
            ])

    return FileResponse(
        path=csv_file,
        filename="prediction_logs.csv",
        media_type="text/csv"
    )

@app.post("/api/classify")
async def api_classify(ticket: TicketRequest):

    result = classify_ticket(
        ticket.subject,
        ticket.description,
        None
    )

    log_entry = {
        "ticket_id": ticket.ticket_id,
        "subject": ticket.subject,
        "description": ticket.description,
        "category": result["category"],
        "subcategory": result["subcategory"],
        "priority": result["priority"],
        "reason": result["reason"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_ticket(log_entry)

    return log_entry