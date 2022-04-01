from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from database.connection import conn

from routes.users import user_router
from routes.events import event_router

import uvicorn

app = FastAPI()

# Register routes

app.include_router(user_router,  prefix="/user")
app.include_router(event_router, prefix="/event")

app.mount("/images", StaticFiles(directory="images"), name="images")


@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)