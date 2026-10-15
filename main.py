from fastapi import FastAPI

app = FastAPI(
    title="My First Public API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "API is online!"}

@app.get("/products")
def get_products():
    return {
        "products": ["Laptop", "Phone"]
    }
