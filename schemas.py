from pydantic import BaseModel,Field 
#llamamso a base model para la escrutura del objetoque vamos a crear 
#llamamos a Field para crear validadciones personalizadas

class Product(BaseModel):#creamos el objeto prodycto
    name : str = Field(min_length=3)
    description: str | None = None
    price:float = Field(gt=0)
    stock: int = Field(gt=0)