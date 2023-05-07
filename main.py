from fastapi import FastAPI
from pydantic import BaseModel
import time
from profiler import profiler

app = FastAPI()

class Message(BaseModel):
    message: str


@app.get('/')
@profiler
def test_function():
    print("Hello")
    time.sleep(10)
    print("world")
    return {"status":"ALL OK"}


@app.post("/post")
@profiler
def post_message(message: Message):
    print(message)
    return message.message