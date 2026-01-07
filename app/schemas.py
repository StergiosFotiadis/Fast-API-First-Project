from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True




class PostCreate(PostBase):                 #KANEI EXTEND TO POSTBASE
    pass


class PostUpdate(PostBase):                 #KANEI EXTEND TO POSTBASE
    pass





                    #<---------------------------------------RESPOSNE MODEL-------------------------------------->



class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime    
    
  
    class Config:
        from_attributes = True              #To orm_mode den douleyei




class PostResponse(PostBase):
    id: int
    created_at: datetime 
    owner_id: int
    owner: UserOut
  
    class Config:
        from_attributes = True              


class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        from_attributes = True




class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime    
    
    
    class Config:
        from_attributes = True             


class UserCreate(BaseModel):
    email: EmailStr
    password: str







class UserLogin(BaseModel):
    email: EmailStr
    password: str






class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None



class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)