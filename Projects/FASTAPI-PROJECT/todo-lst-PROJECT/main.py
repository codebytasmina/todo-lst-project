from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
todo_list=[]

class Task(BaseModel):
    id:int
    title:str
    is_done:bool=False

@app.get("/tasks")
def get_all_tasks():
    return{"Tasks":todo_list}

@app.post("/tasks")
def create_Task(new_task:Task):
    todo_list.append(new_task)
    return{"message":"successfully added"}

@app.put("/tasks/{task_id}")
def update_task(task_id:int,updated_task:Task):
    for i in range(len(todo_list)):
        if todo_list[i].id == task_id:
            todo_list[i]=updated_task
            return{"task":"task updated"}
        return{"error":"task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int):
    for i in range(len(todo_list)):
        if todo_list[i].id == task_id:
            del todo_list[i]
            return{"message":"Task Removed"}
        return{"message":"task not found"}