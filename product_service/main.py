from fastapi import FastAPI

app = FastAPI()

products = {
    1: {
        "id": 1,
        "name": "Laptop",
        "price": 500,
        "image": "https://picsum.photos/300?1"
    },
    2: {
        "id": 2,
        "name": "Phone",
        "price": 300,
        "image": "https://picsum.photos/300?2"
    },
    3: {
        "id": 3,
        "name": "Headphones",
        "price": 100,
        "image": "https://picsum.photos/300?3"
    }
}

@app.get("/products")
def get_products():
    return products
