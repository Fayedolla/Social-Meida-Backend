from fastapi import FastAPI, APIRouter, status, HTTPException, Depends
from .. import schemes, Models, oauth2
from sqlalchemy.orm import Session
from ..Database import get_db

router = APIRouter(prefix="/vote",tags=['Votes'])

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemes.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(Models.Post).filter(Models.Post.id == vote.post_id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.id} was not found!")

    vote_query = db.query(Models.Vote).filter(Models.Vote.post_id == vote.post_id, Models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f"User: {current_user.email} has already voted on post: {vote.post_id}")
        
        new_vote = Models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"message", "Successfully added vote!"}
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail=f"User: {current_user.email} has already voted on post: {vote.post_id}")
        else:
            db.delete(found_vote)
            db.commit()
            return {"message": "Successfully delete vote!"}