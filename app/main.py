from fastapi import FastAPI
from app.routers import bookmarks
from app.db import models
from app.db.database import engine

# DBの作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ルーターを登録
app.include_router(bookmarks.router, prefix="/bookmarks", tags=["bookmarks"])

@app.get("/")
def read_root():
    return {"message": "YouTube Bookmark API"}
