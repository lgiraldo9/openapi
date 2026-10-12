from fastapi import FastAPI#importamos lla libreria de fasapi
from schemas import Product
app = FastAPI()#instanciamos la aplicacion

@app.get("/")
def home():
    return{"mensaje":"hola mundo"} 

@app.get("/products")
def get_products(limit : int = 10):
    return{"products":[], "limit": limit}

@app.get("/products/{product_id}")
def get_product(product_id: int, include_desc : bool=False):
    return {"id": product_id,"include_desc":include_desc}

@app.post("/products",status_code=201)
def create_product(product: Product):
    return product