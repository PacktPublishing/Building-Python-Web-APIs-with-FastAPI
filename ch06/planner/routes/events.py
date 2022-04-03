from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, status, File, Form
from fastapi.templating import Jinja2Templates
from sqlmodel import select

from database.connection import get_session
from database.events import Events, EventUpdate

event_router = APIRouter(
    tags=["Events"]
)

templates = Jinja2Templates(directory="templates/")


@event_router.get("/", response_model=List[Events])
async def retrieve_all_events(session=Depends(get_session)):
    statement = select(Events)
    events = session.exec(statement).all()
    return events


@event_router.get("/{id}", response_model=Events)
async def retrieve_event(id: int, session=Depends(get_session)):
    event = session.get(Events, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.post("/new")
async def create_event(title: str = Form(...), description: str = Form(...), tags: str = Form(...), location: str = Form(...), image: UploadFile = File(...), session=Depends(get_session)):
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

    return {
        "message": "Event created successfully"
    }


@event_router.put("/edit/{id}", response_model=Events)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)
):
    event = session.get(Events, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)

        session.add(event)
        session.commit()
        session.refresh(event)

        return event

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )


@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session)):
    event = session.get(Events, id)
    if event:
        session.delete(event)
        session.commit()

        return {
            "message": "Event deleted successfully"
        }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
