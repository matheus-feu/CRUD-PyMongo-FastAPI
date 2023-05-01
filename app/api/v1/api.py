from fastapi import APIRouter

from app.api.v1.routes import book

api_router = APIRouter()

api_router.include_router(book.router, prefix="/book", tags=["book"])
