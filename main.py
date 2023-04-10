from fastapi import FastAPI
import time
from profiler import profiler

app = FastAPI()

@profiler
@app.get('/')
def test_function():
    print("Hello")
    time.sleep(10)
    print("world")
    return {"status":"ALL OK"}