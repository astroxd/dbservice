from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)


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