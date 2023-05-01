from typing import List

from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.schemas.book import BookCreateSchema, BookUpdateSchema

router = APIRouter()


@router.post("/", response_description="Create a new book", status_code=status.HTTP_201_CREATED,
             response_model=BookCreateSchema)
async def create_book(request: Request, book: BookCreateSchema = Body(...)):
    book = jsonable_encoder(book)

    if "_id" in book and request.app.mongodb["books"].find_one({"_id": book["_id"]}) is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Book with id {book['_id']} already exists")

    try:
        new_book = request.app.mongodb["books"].insert_one(book)
        created_book = request.app.mongodb["books"].find_one({"_id": new_book.inserted_id})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    return created_book


@router.get("/", response_description="List all books", response_model=List[BookCreateSchema])
async def list_books(request: Request):
    books = list(request.app.mongodb["books"].find(limit=100))
    return books


@router.get("/{id}", response_description="Get a single book by id", response_model=BookCreateSchema)
async def show_book(id: str, request: Request):
    if (book := request.app.mongodb["books"].find_one({"_id": id})) is not None:
        return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")


@router.put("/{id}", response_description="Update a book", response_model=BookCreateSchema)
async def update_book(id: str, request: Request, book: BookUpdateSchema = Body(...)):
    book = {k: v for k, v in book.dict().items() if v is not None}

    if len(book) >= 1:
        update_result = request.app.mongodb["books"].update_one({"_id": id}, {"$set": book})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")

    if (existing_book := request.app.mongodb["books"].find_one({"_id": id})) is not None:
        return existing_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")


@router.delete("/{id}", response_description="Delete a book")
async def delete_book(id: str, request: Request):
    delete_result = request.app.mongodb["books"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")
