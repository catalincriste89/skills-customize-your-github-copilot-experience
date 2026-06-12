"""
FastAPI Assignment - Starter Code
Building REST APIs with FastAPI

This starter code provides the basic structure to get you started.
Fill in the implementation for each task.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI app
app = FastAPI()

# TODO: Define a Pydantic model for Book (Task 3)
# class Book(BaseModel):
#     id: int
#     title: str
#     author: str
#     year: int

# In-memory storage for books
books_db: List[dict] = []


# TODO: Task 1 - Create the welcome endpoint
@app.get("/")
async def welcome():
    """Return a welcome message"""
    return {"message": "Welcome to the Book API!"}


# TODO: Task 1 - Create the books list endpoint
@app.get("/books")
async def list_books():
    """Return the list of all books"""
    return books_db


# TODO: Task 2 - Create POST endpoint to add a new book
# @app.post("/books")
# async def create_book(book: dict):
#     """Add a new book to the collection"""
#     pass


# TODO: Task 2 - Create GET endpoint to retrieve a specific book
# @app.get("/books/{book_id}")
# async def get_book(book_id: int):
#     """Retrieve a book by ID"""
#     pass


# TODO: Task 2 - Create PUT endpoint to update a book
# @app.put("/books/{book_id}")
# async def update_book(book_id: int, book: dict):
#     """Update a book by ID"""
#     pass


# TODO: Task 2 - Create DELETE endpoint to remove a book
# @app.delete("/books/{book_id}")
# async def delete_book(book_id: int):
#     """Delete a book by ID"""
#     pass


# Run the app with: uvicorn main:app --reload
