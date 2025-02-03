from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List

class BookmarkBase(BaseModel):
    """
    ブックマークのベースデータモデル
    """
    url: str    # Youtube動画のURL
    title: str  # 動画タイトル
    memo: Optional[str] = None  # ユーザが追加するメモ
    tags: Optional[List[str]] = None  # タグ（カンマ区切りで複数指定）
    timestamp: int  # 動画のタイムスタンプ

class BookmarkCreate(BookmarkBase):
    """
    ブックマーク作成用のデータモデル
    """
    pass

class BookmarkUpdate(BaseModel):
    """
    ブックマーク更新用のデータモデル
    """
    title: Optional[str] = None
    memo: Optional[str] = None
    tags: Optional[List[str]] = None
    timestamp: Optional[int] = None

class Bookmark(BookmarkBase):
    """
    ブックマークのデータモデル
    """
    id: int # レコードで一意のID
    created_at: datetime # 登録日時
    
    class Config:
        """
        PydanticのORMモード定義
        """
        orm_mode = True