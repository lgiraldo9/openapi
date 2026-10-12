from pydantic import BaseModel


class Product(BaseModel):#creamos el objeto prodycto
    name : str
    description: str | None = None
    price:float
    stock: int