from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Annotated


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    email: str
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True  # fixed: was orm_mode


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True  # fixed: was orm_mode

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(UserCreate):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]  # fixed: was conint