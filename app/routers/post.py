from .. import models, schemas
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends, Response, APIRouter
from typing import List
from .. import oauth2
from typing import Optional
from sqlalchemy import func
from ..schemas import PostOut


router = APIRouter(
    prefix="/posts" ,
    tags=["Posts"]
)




@router.get("/", response_model=List[schemas.PostOut])

def get_posts(db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""): 
    
    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    
    return posts






@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post:schemas.PostCreate, db: Session = Depends(get_db),   get_current_user: int = Depends(oauth2.get_current_user)):


    new_post = models.Post(owner_id = get_current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


    
@router.get("/{id}", response_model=schemas.PostOut) 
def  get_post(id: int, db: Session = Depends(get_db)):
   
    
    
    
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()             #FILTER == WHERE
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} was not found")
    return   post    






@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id :int, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
   
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} was not found")




    if post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


 

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostUpdate, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
   
    post_query = db.query(models.Post).filter(models.Post.id == id)
    

    existing_post = post_query.first()

    if existing_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} was not found")

    if existing_post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action") 
    
    post_query.update(post.dict(), synchronize_session=False)  
    db.commit()




    return post_query.first()