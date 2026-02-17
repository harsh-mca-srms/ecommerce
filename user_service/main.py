from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

users = {
    1: {"id": 1, "name": "Harsh"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users.get(user_id, {"error": "User not found"})
