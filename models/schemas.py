from pydantic import BaseModel, EmailStr
from datetime import datetime

class CreateUser(BaseModel):
    
    name: str
    email: EmailStr
    password: str
    class Config:
        orm_mode = True

class UpdateUser(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

    class Config:
        orm_mode = True        

class UserOut(BaseModel):

    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class User(BaseModel):
    email: EmailStr
    password: str 

class CreateProduct(BaseModel):
    name: str
    description: str | None = None
    price: int

    class Config:
        orm_mode =  True

class UpdateProduct(BaseModel):
    name: str | None = None
    description: str | None = None
    price: int | None = None

    class Config:
        orm_mode = True

class ProductOut(BaseModel):    
    id: int
    name: str
    description: str | None = None
    price: int
    created_at: datetime

    class Config:
        orm_mode = True

class CreateOrder(BaseModel):
    user_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class UpdateOrder(BaseModel):
    user_id: int | None = None
    product_id: int | None = None
    quantity: int | None = None

    class Config:
        orm_mode = True

class OrderOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode = True

class TokenData(BaseModel):
    id: int | None = None
    name: str | None = None
    email: str | None = None
    class Config:
        orm_mode = True

class Login(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True