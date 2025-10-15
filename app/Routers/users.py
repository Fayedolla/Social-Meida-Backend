from ..Database import get_db
from .. import Models, schemes, utils
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemes.UserOut)
def create_user(user: schemes.UserOut, db: Session = Depends(get_db)):
        new_user = Models.User(**user.model_dump())
        new_user.password = utils.hash(new_user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

@router.get("/{id}", response_model=schemes.UserOut)
def get_user(user: schemes.UserOut, db: Session = Depends(get_db)):
    user = db.query(Models.user).filter(Models.user.id == id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} was not found!")
