from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from app.db.database import Base

class Bookmark(Base):
    """
    ブックマークを保存するためのDBモデル
    URL, タイトル, メモ, タグ, タイムスタンプ, 作成日時を管理する
    """
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)          # レコードで一意のID
    url = Column(String, index=True)                            # Youtube動画のURL
    title = Column(String)                                      # 動画タイトル
    memo = Column(String, nullable=True)                        # ユーザが追加するメモ
    tags = Column(JSON, nullable=True)                        # タグ（カンマ区切りで複数指定）
    timestamp = Column(Integer)                                 # 動画のタイムスタンプ
    created_at = Column(DateTime, default=datetime.utcnow)      # 登録日時（デフォルトは現在時刻）
