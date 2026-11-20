from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Task(BaseModel):
    # Add the fields described in the assignment
    pass


tasks = []


@app.get("/")
def read_root():
    # Return a welcome message
    pass


@app.get("/tasks")
def read_tasks():
    # Return all tasks
    pass


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    # Find and return the requested task
    pass


@app.post("/tasks")
def create_task(task: Task):
    # Add the task to the list and return it
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    # Find and update the requested task
    pass
