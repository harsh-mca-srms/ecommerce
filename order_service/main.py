from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import requests

app = FastAPI()
Instrumentator().instrument(app).expose(app)

orders = {}

@app.post("/orders/{user_id}")
def create_order(user_id: int):
    cart = requests.get(f"http://cart-service:8003/cart/{user_id}").json()

    if not cart:
        return {"error": "Cart is empty"}

    orders[user_id] = cart
    return {"message": "Order placed", "order": cart}

@app.get("/orders/{user_id}")
def get_orders(user_id: int):
    return orders.get(user_id, [])
