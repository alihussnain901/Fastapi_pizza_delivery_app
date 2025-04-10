from fastapi import FastAPI
from routes import users, products, login, orders
from models.database import engine
from models import model


model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(login.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def welcome():
    return {"Hello welcome to the Pizza Delivery API!"}



