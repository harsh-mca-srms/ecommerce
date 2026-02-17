from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import requests

app = FastAPI()
Instrumentator().instrument(app).expose(app)

cart = {}

@app.post("/cart/add/{user_id}/{product_id}")
def add_to_cart(user_id: int, product_id: int):
    user = requests.get(f"http://user-service:8001/users/{user_id}").json()
    product = requests.get(f"http://product-service:8002/products/{product_id}").json()

    if "error" in user or "error" in product:
        return {"error": "Invalid user or product"}

    cart.setdefault(user_id, []).append(product)
    return {"message": "Added to cart", "cart": cart[user_id]}

@app.get("/cart/{user_id}")
def view_cart(user_id: int):
    return cart.get(user_id, [])
