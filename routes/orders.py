from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import Oauth2
import models
import schemas
from database import get_db


router = APIRouter( 
    prefix="/orders",
    tags=["orders"],
)

# Create a new order
@router.post("/", response_model=schemas.OrderOut, status_code=status.HTTP_201_CREATED)
def create_order(order: schemas.CreateOrder, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == order.user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    db_product = db.query(models.Product).filter(models.Product.id == order.product_id).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    new_order = models.Order(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    return new_order

# Update order
@router.put("/{order_id}", response_model=schemas.OrderOut)
def update_order(order_id: int, order: schemas.UpdateOrder, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    
    for key, value in order.model_dump(exclude_unset=True).items():
        setattr(db_order, key, value)
    
    db.commit()
    db.refresh(db_order)
    
    return db_order

# Delete order
@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    
    db.delete(db_order)
    db.commit()
    
    return {"details": "Order deleted successfully"}

# Get all orders
@router.get("/", response_model=list[schemas.OrderOut])
def get_orders(db: Session = Depends(get_db), user: str = Depends(Oauth2.get_current_user)):
    orders = db.query(models.Order).all()
    return orders

# Get order by ID
@router.get("/{order_id}", response_model=schemas.OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    
    return order

# Get orders by user ID
@router.get("/user/{user_id}", response_model=list[schemas.OrderOut])
def get_orders_by_user(user_id: int, db: Session = Depends(get_db)):
    orders = db.query(models.Order).filter(models.Order.user_id == user_id).all()
    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found for this user")
    
    return orders
