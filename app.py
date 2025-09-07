"""
FastAPI サンプルアプリケーション
複数ポートでの実行例を含む
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import asyncio
from typing import Optional

# FastAPIアプリケーションのインスタンス作成
app = FastAPI(
    title="FastAPI Example",
    description="Google Cloud Study用のFastAPIサンプル",
    version="1.0.0"
)

# データモデルの定義
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

# インメモリデータストア（実際の本番環境ではデータベースを使用）
items_db = {}
users_db = {}

# ルートエンドポイント
@app.get("/")
async def read_root():
    return {
        "message": "FastAPI サンプルアプリケーション",
        "status": "running",
        "endpoints": {
            "items": "/items",
            "users": "/users",
            "health": "/health"
        }
    }

# ヘルスチェックエンドポイント
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "fastapi-example"}

# アイテム関連のエンドポイント
@app.post("/items/")
async def create_item(item: Item):
    item_id = len(items_db) + 1
    items_db[item_id] = item.model_dump()
    return {"item_id": item_id, "item": item}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": items_db[item_id]}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    items_list = []
    for item_id, item_data in list(items_db.items())[skip:skip + limit]:
        items_list.append({"item_id": item_id, "item": item_data})
    return {"items": items_list, "total": len(items_db)}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.model_dump()
    return {"item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item}

# ユーザー関連のエンドポイント
@app.post("/users/")
async def create_user(user: User):
    user_id = len(users_db) + 1
    users_db[user_id] = user.model_dump()
    return {"user_id": user_id, "user": user}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "user": users_db[user_id]}

@app.get("/users/")
async def read_users():
    users_list = []
    for user_id, user_data in users_db.items():
        users_list.append({"user_id": user_id, "user": user_data})
    return {"users": users_list, "total": len(users_db)}

# 複数ポート対応のための追加アプリケーション
app_secondary = FastAPI(title="Secondary FastAPI App")

@app_secondary.get("/")
async def secondary_root():
    return {"message": "Secondary FastAPI App", "port": "8001"}

@app_secondary.get("/secondary/health")
async def secondary_health():
    return {"status": "healthy", "service": "secondary-app"}

# メイン実行部分
if __name__ == "__main__":
    # 複数ポートでの実行例
    async def run_multiple_servers():
        # メインアプリ（ポート8000）
        config1 = uvicorn.Config(app, host="0.0.0.0", port=8000)
        server1 = uvicorn.Server(config1)
        
        # セカンダリアプリ（ポート8001）
        config2 = uvicorn.Config(app_secondary, host="0.0.0.0", port=8001)
        server2 = uvicorn.Server(config2)
        
        # 両方のサーバーを並行実行
        await asyncio.gather(
            server1.serve(),
            server2.serve()
        )
    
    # 単一ポートでの実行（デフォルト）
    print("FastAPI アプリケーションを起動中...")
    print("メインアプリ: http://localhost:8000")
    print("ドキュメント: http://localhost:8000/docs")
    print("複数ポートで実行する場合は、Dockerfileを使用してください")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)