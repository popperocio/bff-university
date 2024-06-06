from fastapi import APIRouter

version = APIRouter()


@version.get("/")
async def index() -> dict:
    return {"Backend for Frontend Final Project University 2.0": "0.1"}
