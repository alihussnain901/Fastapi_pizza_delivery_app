from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, Oauth2
from ..database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"],
)
# Create a new product
@router.post("/", response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product: schemas.CreateProduct, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.name == product.name).first()
    if db_product:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product already exists")
    new_product = models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product

# Update product
@router.put("/{product_name}", response_model=schemas.ProductOut)
def update_product(product_name: str, product: schemas.UpdateProduct, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.name == product_name).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(db_product, key, value)
    
    db.commit()
    db.refresh(db_product)
    
    return db_product

# Delete product
@router.delete("/{product_name}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_name: str,  db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.name == product_name).first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    db.delete(db_product)
    db.commit()
    
    return {"details": "Product deleted successfully"}

# Get all products
@router.get("/", response_model=list[schemas.ProductOut])
def get_products(db: Session = Depends(get_db), user: str = Depends(Oauth2.get_current_user)):
    products = db.query(models.Product).all()
    return products

#  Get product by name 
@router.get("/{product_name}", response_model=schemas.ProductOut)
def get_product_by_name(product_name: str, db: Session = Depends(get_db), user: str = Depends(Oauth2.get_current_user)):
    product = db.query(models.Product).filter(models.Product.name == product_name).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return product