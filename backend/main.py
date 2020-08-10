from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from ml_controller.controller import getURL
from typing import List

app: FastAPI = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse('./static/index.html')


@app.get("/api/recommendation")
def recommendation(url: str) -> dict:

    charityUrl: List[str] = getURL(url)

    return {
        "original_url": url,
        "charity_url": charityUrl
    }
