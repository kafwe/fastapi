from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint

class User(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime 

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
 
class PostCreate(PostBase):
    pass

class Post(PostBase):
    user_id: int
    id: int
    created_at: datetime
    user: User

    class Config:
        orm_mode = True

class PostVote(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    direction: conint(le=1, ge=0)