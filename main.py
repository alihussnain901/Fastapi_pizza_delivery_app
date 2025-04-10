from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import users, products, login, orders


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(login.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def welcome():
    return {"Hello welcome to the Pizza Delivery API!"}



