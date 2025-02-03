import os
from dotenv import load_dotenv

# 環境変数を読み込む
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./bookmarks.db")