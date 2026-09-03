from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

class Students(BaseModel):
    name: str
    age: int
    grade: str      
    phone: str| None = None



@app.get("/")
async def root():
    return {"enter the name of the student you want to add "}

@app.post("/students")
async def create_student(student: Students):
    return student