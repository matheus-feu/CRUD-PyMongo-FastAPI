import uuid
from typing import Optional

from pydantic import BaseModel, Field


class BookCreateSchema(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id", Optional=True)
    title: str
    author: str
    synopsis: str
    description: Optional[str] = None
    price: float
    quantity: int

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "5f8f8a8b-8b7a-4c5a-9b1a-9c4a5d8b7a8b",
                "title": "The Lord of the Rings",
                "author": "J. R. R. Tolkien",
                "synopsis": "The Lord of the Rings is an epic high fantasy novel written by English author and scholar J. R. R. Tolkien.",
                "description": "The story began as a sequel to Tolkien's 1937 fantasy novel The Hobbit, but eventually developed into a much larger work.",
                "price": 10.99,
                "quantity": 10
            }
        }


class BookUpdateSchema(BookCreateSchema):
    id: Optional[str]
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]
    description: Optional[str]
    price: Optional[float]
    quantity: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "title": "The Lord of the Rings",
                "author": "J. R. R. Tolkien",
                "synopsis": "The Lord of the Rings is an epic high fantasy novel written by English author and scholar J. R. R. Tolkien.",
                "description": "The story began as a sequel to Tolkien's 1937 fantasy novel The Hobbit, but eventually developed into a much larger work.",
                "price": 10.99,
                "quantity": 10
            }
        }
