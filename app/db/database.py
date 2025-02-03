from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

# データベースエンジンを作成（SQLiteを使用）
# `check_same_thread=False` はSQLiteのスレッド制約を無効化するために必要
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# セッションの作成（自動コミットなし、フラッシュなし）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラスの定義（SQLAlchemyのORMで使用）
Base = declarative_base()
