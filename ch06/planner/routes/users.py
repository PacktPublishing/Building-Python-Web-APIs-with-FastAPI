from fastapi import APIRouter, HTTPException, Request, status, Depends
from fastapi.templating import Jinja2Templates

from models.users import NewUser, UserSignIn

user_router = APIRouter(
    tags=["User"],
)

users = {}
templates = Jinja2Templates(directory="templates/")


@user_router.post("/signup")
async def sign_user_up(request: Request, data: NewUser = Depends(NewUser.as_form)):
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    users[data.email] = data

    return templates.TemplateResponse("user.html", {
        "request": request,
        "signed_in": True,
    })


@user_router.post("/signin")
async def sign_user_in(request: Request, user: UserSignIn = Depends(UserSignIn.as_form)):
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "signed_in": True
        }
    )


@user_router.get("/")
async def render_login_page(request: Request):
    return templates.TemplateResponse(
        "user.html", {
            "request": request,
            "sign_in": True
        }
    )


@user_router.get("/signup")
async def render_signup_page(request: Request):
    return templates.TemplateResponse(
        "user.html", {
            "request": request,
            "sign_in": False
        }
    )