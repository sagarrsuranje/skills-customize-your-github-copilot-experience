# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build and deploy REST APIs using the FastAPI framework in Python. Students will create endpoints, handle requests, and return responses in JSON format.

## 📝 Tasks

### 🛠️ Task 1: Create a Basic FastAPI App

#### Description
Set up a FastAPI project and implement a simple API endpoint that returns a welcome message.

#### Requirements
Completed program should:
- Start a FastAPI server
- Provide a `/` endpoint that returns `{ "message": "Welcome to FastAPI!" }`
- Use proper Python file structure

### 🛠️ Task 2: Implement CRUD Operations

#### Description
Expand your FastAPI app to include CRUD (Create, Read, Update, Delete) endpoints for managing a list of items (e.g., books, tasks, or users).

#### Requirements
Completed program should:
- Provide endpoints for adding, retrieving, updating, and deleting items
- Use Pydantic models for data validation
- Return responses in JSON format
- Handle errors gracefully

### 🛠️ Task 3: (Optional) Add Authentication

#### Description
Add basic authentication to protect certain endpoints (e.g., using API keys or simple token-based auth).

#### Requirements
Completed program should:
- Require authentication for modifying data
- Return appropriate error messages for unauthorized access
