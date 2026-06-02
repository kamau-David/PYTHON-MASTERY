"""A CRUD REST API with FastAPI. Pydantic models define the request/response
shape and validate incoming data automatically - invalid data gets a 422
response before your code even runs."""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API", version="1.0.0")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    priority: int = Field(default=1, ge=1, le=5)


class Task(TaskCreate):
    id: int
    done: bool = False


# in-memory store for this demo
tasks: dict[int, Task] = {}
next_id = 1


@app.get("/")
def root():
    return {"message": "Task API - see /docs for interactive documentation"}


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate):
    global next_id
    task = Task(id=next_id, **payload.model_dump())
    tasks[next_id] = task
    next_id += 1
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks(done: bool | None = None):
    # optional query parameter: /tasks?done=true
    values = list(tasks.values())
    if done is not None:
        values = [t for t in values if t.done == done]
    return values


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return task


@app.patch("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="task not found")
    task.done = True
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="task not found")
    del tasks[task_id]
