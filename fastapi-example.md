# FastAPI Example Project

このディレクトリには FastAPI を使用したサンプルアプリケーションが含まれています。

## ファイル構成

- `app.py` - メインの FastAPI アプリケーション
- `requirements.txt` - Python 依存関係
- `Dockerfile.fastapi` - FastAPI 用の Dockerfile
- `test_app.py` - アプリケーションのテストファイル
- `fastapi-example.md` - この説明ファイル

## 機能

このサンプルアプリケーションには以下の機能が含まれています：

### エンドポイント

- `GET /` - ルートエンドポイント（アプリケーション情報）
- `GET /health` - ヘルスチェック
- `POST /items/` - アイテム作成
- `GET /items/{item_id}` - 特定アイテムの取得
- `GET /items/` - アイテム一覧取得
- `PUT /items/{item_id}` - アイテム更新
- `DELETE /items/{item_id}` - アイテム削除
- `POST /users/` - ユーザー作成
- `GET /users/{user_id}` - 特定ユーザーの取得
- `GET /users/` - ユーザー一覧取得

### データモデル

- `Item` - アイテムのデータモデル（name, description, price, tax）
- `User` - ユーザーのデータモデル（username, email, full_name）

## ローカル実行

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. アプリケーションの起動

```bash
python app.py
```

または

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 3. アクセス

- アプリケーション: http://localhost:8000
- API ドキュメント: http://localhost:8000/docs
- ReDoc ドキュメント: http://localhost:8000/redoc

## Docker での実行

### 1. イメージのビルド

```bash
docker build -f Dockerfile.fastapi -t fastapi-example .
```

### 2. コンテナの実行

```bash
docker run -p 8000:8000 fastapi-example
```

### 3. 複数ポートでの実行

```bash
docker run -p 8000:8000 -p 8001:8001 -p 8002:8002 fastapi-example
```

## テストの実行

```bash
pytest test_app.py -v
```

## Google Cloud での実行

### 1. Cloud Build でビルド

```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/fastapi-example
```

### 2. Cloud Run にデプロイ

```bash
gcloud run deploy fastapi-example \
  --image gcr.io/PROJECT_ID/fastapi-example \
  --platform managed \
  --region asia-northeast1 \
  --allow-unauthenticated \
  --port 8000
```

## API の使用例

### アイテムの作成

```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Sample Item",
    "description": "This is a sample item",
    "price": 29.99,
    "tax": 2.99
  }'
```

### ユーザーの作成

```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe"
  }'
```

### ヘルスチェック

```bash
curl http://localhost:8000/health
```