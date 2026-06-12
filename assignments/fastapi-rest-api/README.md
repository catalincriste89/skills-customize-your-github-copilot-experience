# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

You will build a RESTful API using the FastAPI framework that manages a collection of books. Through this assignment, you'll learn how to create HTTP endpoints, handle request/response data with Pydantic models, and implement CRUD operations.

## 📝 Tasks

### 🛠️ Task 1: Create Your First FastAPI Endpoint

#### Description
Set up a basic FastAPI application with a welcome endpoint. This will introduce you to the FastAPI framework and how to run a simple server.

#### Requirements
Your application should:

- Import and initialize a FastAPI application
- Create a GET endpoint at `/` that returns a welcome message
- Create a GET endpoint at `/books` that returns an empty list
- Run the server on port 8000 using uvicorn

**Hint:** Use `fastapi` and `uvicorn` packages. Run your app with `uvicorn main:app --reload`


### 🛠️ Task 2: Build CRUD Endpoints for Books

#### Description
Expand your API with endpoints to Create, Read, Update, and Delete books from an in-memory list. Each book should have an id, title, author, and year.

#### Requirements
Your application should:

- Create a POST endpoint at `/books` to add a new book to the collection
- Create a GET endpoint at `/books/{book_id}` to retrieve a specific book
- Create a PUT endpoint at `/books/{book_id}` to update a book
- Create a DELETE endpoint at `/books/{book_id}` to remove a book
- Store books in a Python list (in-memory storage is fine for this assignment)

**Hint:** Use path parameters like `{book_id}` and request body for POST/PUT operations.


### 🛠️ Task 3: Add Data Validation with Pydantic Models

#### Description
Improve your API by using Pydantic models to validate and serialize book data. This ensures consistent data structure and automatic validation.

#### Requirements
Your application should:

- Create a Pydantic `Book` model with fields: `id`, `title`, `author`, and `year`
- Use the `Book` model for request bodies (POST and PUT)
- Return `Book` models from all endpoints
- Ensure year is an integer and title/author are non-empty strings

**Hint:** Define Pydantic models before your route definitions. Use type hints in your function parameters.


### 🛠️ Task 4: Handle Errors and Status Codes (Stretch Goal)

#### Description
Make your API more robust by handling errors gracefully and returning appropriate HTTP status codes.

#### Requirements
Your application should:

- Return a 404 error when a book is not found
- Return a 400 error when invalid data is submitted
- Return appropriate status codes: 201 for creation, 200 for success, 204 for deletion
- Include meaningful error messages in responses

**Hint:** Use FastAPI's `HTTPException` and the `status` module for proper status codes.

