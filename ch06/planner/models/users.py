from typing import Optional, List

from fastapi import Form
from pydantic import BaseModel, EmailStr

from models.events import Event


class User(BaseModel):
    email: EmailStr
    username: str
    events: Optional[List[Event]]

    @classmethod
    def as_form(
            cls,
            email: EmailStr = Form(...),
            username: str = Form(...),
            password: str = Form(...)
    ):
        return cls(email=email, username=username, password=password)

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "fastapipackt001",
                "events": [],
            }
        }


class NewUser(User):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "Stro0ng!",
                "username": "FastPackt"
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    @classmethod
    def as_form(
            cls,
            email: EmailStr = Form(...),
            password: str = Form(...)
    ):
        return cls(email=email, password=password)


