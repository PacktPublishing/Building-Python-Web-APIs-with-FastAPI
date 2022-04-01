from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile, status, Form, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import select

from database.connection import get_session
from database.events import Events

event_router = APIRouter(
    tags=["Events"]
)

templates = Jinja2Templates(directory="templates/")


@event_router.get("/", response_class=HTMLResponse)
async def retrieve_all_events(request: Request, session=Depends(get_session)):
    statement = select(Events)
    events = session.exec(statement).all()
    return templates.TemplateResponse(
        "event.html",
        {
            "request": request,
            "events": events
        }
    )


@event_router.get("/new", response_class=HTMLResponse)
async def add_new_event_page(request: Request):
    return templates.TemplateResponse(
        "new_event.html",
        {
            "request": request
        }
    )


@event_router.get("/{id}", response_class=HTMLResponse)
async def retrieve_event(id: int, request: Request, session=Depends(get_session)):
    event = session.get(Events, id)
    if event:
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
async def create_event(request: Request, title: str = Form(...), description: str = Form(...), tags: str = Form(...), location: str = Form(...), image: UploadFile = File(...), session=Depends(get_session)):

    uploaded_image = f"images/{image.filename}"
    with open(uploaded_image, 'wb') as img:
        image_content = await image.read()
        img.write(image_content)

    tags = tags.split(",")
    new_event = Events(
        title=title,
        image=image.filename,
        description=description,
        tags=tags,
        location=location
    )
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    event = session.get(Events, new_event.id)

    return templates.TemplateResponse("event.html", {
        "request": request,
        "event": event
    })


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
