from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models import model
from ..models.database import get_db
from ..models.utils import verify_password 
from fastapi.security import OAuth2PasswordRequestForm 
from ..models.Oauth2 import create_access_token

router = APIRouter(
    prefix="/login",
    tags=["login"],
)

# Login user
@router.post("/")
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.email == user.username).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}