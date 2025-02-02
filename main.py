from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import random

# Create a dictionary with 100 students and random marks (0 to 100)
students = {f"Student{i}": random.randint(0, 100) for i in range(1, 101)}

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api")
def get_marks(name: list[str]):
    marks = []
    for student in name:
        marks.append(students.get(student, None))  # None if student not found
    return JSONResponse(content={"marks": marks})
