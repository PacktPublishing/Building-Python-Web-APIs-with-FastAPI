from fastapi import APIRouter, Body, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

templates = Jinja2Templates(directory="templates/")

events = []


@event_router.get("/", response_class=HTMLResponse)
async def retrieve_all_events(request: Request):
    return templates.TemplateResponse(
        "event.html",
        {
            "request": request,
            "events": events
        }
    )


@event_router.get("/{id}", response_class=HTMLResponse)
async def retrieve_event(id: int, request: Request):
    for event in events:
        if event.id == id:
            return templates.TemplateResponse(
                "event.html",
                {
                    "request": request,
                    "event": event
                }
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.post("/new")
async def create_event(body: Event = Body(...)):
    events.append(body)
    return {
        "message": "Event created successfully"
    }


@event_router.delete("/{id}")
async def delete_event(id: int):
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Event deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
