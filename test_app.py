"""
FastAPI アプリケーションのテストファイル
"""

import pytest
from fastapi.testclient import TestClient
from app import app

# テストクライアントの作成
client = TestClient(app)

def test_read_root():
    """ルートエンドポイントのテスト"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "running"

def test_health_check():
    """ヘルスチェックエンドポイントのテスト"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "fastapi-example"

def test_create_item():
    """アイテム作成のテスト"""
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 100.0,
        "tax": 10.0
    }
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert "item_id" in data
    assert data["item"]["name"] == "Test Item"

def test_read_item():
    """アイテム取得のテスト"""
    # まずアイテムを作成
    item_data = {
        "name": "Test Item 2",
        "description": "Another test item",
        "price": 200.0
    }
    create_response = client.post("/items/", json=item_data)
    item_id = create_response.json()["item_id"]
    
    # 作成したアイテムを取得
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["item"]["name"] == "Test Item 2"

def test_read_nonexistent_item():
    """存在しないアイテムの取得テスト"""
    response = client.get("/items/999")
    assert response.status_code == 404

def test_create_user():
    """ユーザー作成のテスト"""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert data["user"]["username"] == "testuser"

def test_read_users():
    """ユーザー一覧取得のテスト"""
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert "total" in data