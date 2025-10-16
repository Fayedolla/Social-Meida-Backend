from fastapi import APIRouter, Depends, HTTPException, status
from ..Database import get_db
from .. import schemes, Models, oauth2
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(prefix="/post", tags=["Posts"])

@router.get("/", response_model=List[schemes.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
                limit: int = 10, skip: int = 0, search: Optional[str] = ""):

    result = (
        db.query(Models.Post, func.count(Models.Vote.post_id).label("votes"))
        .join(Models.Vote, Models.Vote.post_id == Models.Post.id, isouter=True)
        .filter(Models.Post.title.ilike(f"%{search}%"))
        .group_by(Models.Post.id)
        .limit(limit)
        .offset(skip)
        .all()
    )

    formated_results = [{"Post": post, "votes": votes} for post, votes in result]

    return formated_results


@router.post("/", response_model=schemes.Post, status_code=status.HTTP_201_CREATED)
def create_post(post: schemes.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_post = Models.Post(owner_id = current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemes.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(Models.Post).filter(Models.Post.id == id).first()
    if post:
        return post
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post = db.query(Models.Post).filter(Models.Post.id == id).first()
    if post.owner_id == current_user.id:
        if post:
            db.delete(post)
            db.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found!")
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform this action!")
    

@router.put("/{id}", response_model=schemes.Post)
def update_post(updated_post: schemes.PostCreate ,id: int, db:Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(Models.Post).filter(Models.Post.id == id)
    post = post_query.first()

    if post.owner_id == current_user.id:
        if post:
            post_query.update(updated_post.model_dump(), synchronize_session=False)
            db.commit()
            return post
        
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found!")
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform this action!")