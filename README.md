# google-cloud-study

このリポジトリは Google Cloud Platform (GCP) の学習用リポジトリです。

## 基本的な Google Cloud CLI コマンド

Google Cloud を使い始めるために必要な基本的なコマンドを紹介します。

| コマンド | 説明 | 実行内容 | 初心者向けポイント |
|---------|------|----------|-------------------|
| `gcloud init` | 初回セットアップ（対話式） | • Google アカウントでのログイン<br>• プロジェクトの選択または作成<br>• デフォルトのリージョン・ゾーンの設定 | • 初めて Google Cloud CLI を使う場合は、まずこのコマンドを実行<br>• ブラウザが開いて Google アカウントでの認証が必要<br>• 複数のプロジェクトがある場合は選択可能 |
| `gcloud auth login` | Google アカウント認証 | • ブラウザが開いて Google アカウントでの認証<br>• Google Cloud リソースへのアクセス権限の取得 | • `gcloud init` 実行済みの場合は通常不要<br>• 別のアカウントでログインし直したい場合に使用<br>• 複数のアカウントを管理している場合に便利 |
| `gcloud config set project PROJECT_ID` | プロジェクト設定 | • デフォルトで使用するプロジェクトの設定<br>• 以降の gcloud コマンドでこのプロジェクトが使用される | • `PROJECT_ID` は実際のプロジェクト ID に置き換える<br>• プロジェクト ID は Google Cloud Console で確認<br>• プロジェクトを切り替えたい場合に使用 |
| `gcloud services enable SERVICE_NAME` | サービスの有効化 | • 指定した Google Cloud サービスを有効化<br>• API の使用許可を設定 | • 例: `gcloud services enable compute.googleapis.com`<br>• サービスを使用する前に必ず有効化が必要<br>• 有効化には数分かかる場合がある |
| `gcloud compute instances list` | VM インスタンス一覧表示 | • 現在のプロジェクトの全ての VM インスタンスを表示<br>• インスタンス名、ゾーン、ステータスなどの情報を確認 | • Compute Engine サービスが有効でない場合はエラー<br>• インスタンスがない場合は空の結果が表示<br>• `--zones=ZONE` でゾーンを指定可能 |
| `gsutil ls` | Cloud Storage バケット一覧 | • プロジェクト内の全ての Cloud Storage バケットを表示<br>• `gs://` から始まるバケット URL を表示 | • Cloud Storage API が有効である必要がある<br>• `gsutil ls gs://バケット名` で特定バケット内を表示<br>• バケットがない場合は空の結果 |
| `gsutil cp FILE gs://BUCKET/` | ファイルをクラウドストレージにアップロード | • ローカルファイルを Cloud Storage バケットにコピー<br>• `-r` オプションでディレクトリも再帰的にコピー可能 | • バケットが存在しない場合は事前に作成が必要<br>• `gsutil mb gs://バケット名` でバケット作成<br>• ファイルサイズが大きい場合は時間がかかる |
| `gcloud app deploy` | App Engine にアプリをデプロイ | • 現在のディレクトリのアプリを App Engine にデプロイ<br>• app.yaml ファイルに基づいて設定 | • app.yaml ファイルが必要<br>• 初回デプロイ時は App Engine アプリの作成が必要<br>• デプロイには数分かかる場合がある |
| `gcloud info` | 環境情報表示 | • gcloud の設定情報、インストール状況、アカウント情報を表示<br>• トラブルシューティング時に有用 | • 設定に問題がある場合の診断に便利<br>• サポートに問い合わせる際の情報収集に使用<br>• バージョン情報も含まれる |

**使用例:**
```bash
# 初回セットアップ
gcloud init

# 認証（必要に応じて）
gcloud auth login

# プロジェクト設定
gcloud config set project my-gcp-project-123

# サービスの有効化（例：Compute Engine）
gcloud services enable compute.googleapis.com

# VM インスタンス一覧の確認
gcloud compute instances list

# Cloud Storage バケット一覧の確認
gsutil ls

# ファイルのアップロード例
gsutil cp myfile.txt gs://my-bucket/

# App Engine にデプロイ（app.yaml が必要）
gcloud app deploy

# 環境情報の確認
gcloud info
```

### 現在の設定を確認する

設定済みの内容を確認したい場合は以下のコマンドを使用します:

```bash
# 現在の設定を確認
gcloud config list

# 現在のプロジェクトを確認  
gcloud config get-value project

# 認証済みアカウントを確認
gcloud auth list
```

## Docker コマンド

アプリケーションのコンテナ化とローカル実行に必要な基本的な Docker コマンドを紹介します。

| コマンド | 説明 | 実行内容 | 初心者向けポイント |
|---------|------|----------|-------------------|
| `docker build -t 今のディレクトリ .` | Docker イメージのビルド | • 現在のディレクトリの Dockerfile からイメージを作成<br>• `-t` オプションでイメージに名前（タグ）を付与<br>• `.` は現在のディレクトリを指定 | • Dockerfile が現在のディレクトリに必要<br>• 「今のディレクトリ」部分は実際のプロジェクト名に変更<br>• ビルドには時間がかかる場合がある |
| `docker run -d -p 8080:8080 今のディレクトリ` | コンテナの実行 | • ビルドしたイメージからコンテナを起動<br>• `-d` でバックグラウンド実行<br>• `-p 8080:8080` でポート 8080 をマッピング | • `-d` がないとターミナルがブロックされる<br>• ポート番号はアプリケーションに合わせて変更<br>• イメージ名は build 時のタグと一致させる |
| `http://localhost:8080` | アプリケーションへのアクセス | • ブラウザで実行中のコンテナにアクセス<br>• ローカル開発環境での動作確認 | • コンテナが正常に起動していることを確認<br>• ポート番号は docker run で指定したものと一致<br>• アプリケーションの起動に時間がかかる場合がある |
| `docker info` | Docker システム情報表示 | • Docker の設定情報とシステム状態を表示<br>• インストール状況やリソース使用量を確認 | • Docker が正しくインストールされているかの確認<br>• トラブルシューティング時に有用<br>• システムリソースの確認にも使用 |
| `docker ps` | 実行中コンテナ一覧 | • 現在実行中の全てのコンテナを表示<br>• コンテナ ID、イメージ名、ポートマッピングなどを確認 | • `-a` オプションで停止済みコンテナも表示<br>• コンテナの動作状況を確認<br>• コンテナ ID は stop コマンドで使用 |
| `docker stop CONTAINER_ID` | コンテナの停止 | • 指定したコンテナを安全に停止<br>• CONTAINER_ID は `docker ps` で確認 | • コンテナ ID は最初の数文字のみでも可<br>• 複数のコンテナを同時に停止可能<br>• 強制停止は `docker kill` を使用 |

**Docker 使用例:**
```bash
# Docker イメージをビルド（例：my-app という名前）
docker build -t my-app .

# コンテナをバックグラウンドで実行
docker run -d -p 8080:8080 my-app

# ブラウザでアクセス
# http://localhost:8080

# 実行中のコンテナを確認
docker ps

# Docker システム情報を確認
docker info

# コンテナを停止（CONTAINER_ID は docker ps で確認）
docker stop CONTAINER_ID
```

### Dockerfile の基本例

Docker を使用するには、プロジェクトルートに Dockerfile が必要です：

```dockerfile
# 例：Node.js アプリケーション用 Dockerfile
FROM node:18
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 8080
CMD ["npm", "start"]
```

## 参考リンク

- [Google Cloud CLI ドキュメント](https://cloud.google.com/sdk/docs)
- [gcloud コマンドリファレンス](https://cloud.google.com/sdk/gcloud/reference)