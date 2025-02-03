from sqlalchemy.orm import Session
from app.db import models
from app.schemas import bookmark as schemas
from typing import List, Optional

def create_bookmark(db: Session, bookmark: schemas.BookmarkCreate) -> models.Bookmark:
    """
    新しいブックマークをDBに保存する

    Args:
        db (Session): データベースセッション
        bookmark (schemas.BookmarkCreate): 登録するブックマークのデータ

    Returns:
        models.Bookmark: 保存されたブックマークのオブジェクト
    """
    db_bookmark = models.Bookmark(
        url=bookmark.url,
        title=bookmark.title,
        memo=bookmark.memo,
        tags=bookmark.tags,
        timestamp=bookmark.timestamp
    )
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)

    return db_bookmark

def get_bookmarks(db: Session) -> List[models.Bookmark]:
    """
    すべてのブックマークを取得する。
    
    Args:
        db (Session): データベースセッション
    
    Returns:
        List[models.Bookmark]: 取得したブックマークのリスト
    """
    return db.query(models.Bookmark).all()

def delete_bookmark(db: Session, bookmark_id: int) -> bool:
    """
    指定されたIDのブックマークを削除する。
    
    Args:
        db (Session): データベースセッション
        bookmark_id (int): 削除するブックマークのID
    
    Returns:
        bool: 削除が成功した場合はTrue、失敗した場合はFalse
    """
    db_bookmark = db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()
    if db_bookmark:
        db.delete(db_bookmark)
        db.commit()
        return True
    return False

def update_bookmark(db: Session, bookmark_id: int, update_data: schemas.BookmarkUpdate) -> Optional[models.Bookmark]:
    """
    指定した ID のブックマークを更新する
    """
    db_bookmark = db.query(models.Bookmark).filter(models.Bookmark.id == bookmark_id).first()
    
    if not db_bookmark:
        return None  # 更新対象なし

    # 更新するフィールドのみ変更
    if update_data.title is not None:
        db_bookmark.title = update_data.title
    if update_data.memo is not None:
        db_bookmark.memo = update_data.memo
    if update_data.tags is not None:
        db_bookmark.tags = update_data.tags  # JSON 型なのでそのまま更新可能
    if update_data.timestamp is not None:
        db_bookmark.timestamp = update_data.timestamp

    db.commit()
    db.refresh(db_bookmark)  # 変更を反映
    return db_bookmark
