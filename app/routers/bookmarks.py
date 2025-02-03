from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud, models
from app.db.database import SessionLocal
from app.schemas import bookmark as schemas

router = APIRouter()

# DBセッションを取得する関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ブックマーク登録
@router.post("/", response_model=schemas.Bookmark)
def create_bookmark(bookmark: schemas.BookmarkCreate, db: Session = Depends(get_db)):
    return crud.create_bookmark(db=db, bookmark=bookmark)

# ブックマーク一覧取得
@router.get("/", response_model=list[schemas.Bookmark])
def get_bookmarks(db: Session = Depends(get_db)):
    return crud.get_bookmarks(db)

# ブックマーク削除
@router.delete("/{bookmark_id}")
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db)):
    success = crud.delete_bookmark(db, bookmark_id)
    if not success:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return {"message": "Bookmark deleted successfully"}

# ブックマーク更新
@router.put("/{bookmark_id}", response_model=schemas.Bookmark)
def update_bookmark(bookmark_id: int, update_data: schemas.BookmarkUpdate, db: Session = Depends(get_db)):
    """
    指定したブックマークの情報を更新する
    """
    updated_bookmark = crud.update_bookmark(db, bookmark_id, update_data)
    
    if updated_bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    
    return updated_bookmark