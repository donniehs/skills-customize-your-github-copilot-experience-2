# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test a REST API with the FastAPI framework using routes, request models, and in-memory data.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Set up a FastAPI application and define a Pydantic model that represents a task.

#### Requirements
Completed program should:

- Import and instantiate `FastAPI`
- Define a `Task` model with an integer `id`, a string `title`, and a boolean `completed`
- Start with an in-memory list of tasks
- Define a root route that returns a welcome message

### 🛠️ Implement Read Routes

#### Description
Create endpoints that retrieve all tasks or an individual task by ID.

#### Requirements
Completed program should:

- Define `GET /tasks` to return the complete task list
- Define `GET /tasks/{task_id}` to return the matching task
- Return a 404 status with a helpful message when the task ID does not exist

### 🛠️ Implement Create and Update Routes

#### Description
Add endpoints that accept request data and update the in-memory task list.

#### Requirements
Completed program should:

- Define `POST /tasks` to add a new task
- Automatically assign a new task ID
- Define `PUT /tasks/{task_id}` to update an existing task
- Return a 404 status when updating a task that does not exist

