from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/products")
def read_item():
    with open('./src/data.json', 'r') as file:
        data = json.load(file)

        products = []
        for product in data['products']:
            products.append(product)

    return {'products': products}