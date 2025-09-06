# google-cloud-study

このリポジトリは Google Cloud Platform (GCP) の学習用リポジトリです。

## Quick Start for Development with gcloud and docker

### Windows PowerShell
#### ポリシー緩める
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

#### 現在シェルに設定されているプロジェクトIDの確認
```bash
gcloud config get-value project
```

#### プロジェクトID がわからない場合
```bash
gcloud projects list
```

#### 例: プロジェクトIDが web-gas-test2 の場合
```bash
gcloud config set project web-gas-test2
```

#### docker build
##### web-gas-test2 が今いるディレクトリ
```bash
docker build -t web-gas-test2 .
```

#### gcloud に転送してビルド
- 現在のディレクトリの内容を Google Cloud Build に送信し、
- Dockerイメージをビルドして 
- Google Container Registry（GCR）に 
- gcr.io/PROJECT_ID/IMAGE_NAME という名前で保存する

```bash
gcloud builds submit --tag gcr.io/web-gas-test2/test
gcloud builds submit --tag gcr.io/PROJECT_ID/IMAGE_NAME
```

#### サービスを起動
```bash
gcloud run deploy web-gas-test2 --image gcr.io/web-gas-test2/test --platform managed --region asia-northeast1 --allow-unauthenticated
```

#### サービス起動を確認
```bash
curl 起動したURL
```

#### 現在のサービス一覧を確認
```bash
gcloud run services list
gcloud run services list --region asia-northeast1
```

#### 特定サービスの詳細を確認
```bash
gcloud run services describe web-gas-test2 --region asia-northeast1
```

#### サービスの完全削除（停止）
```bash
gcloud run services delete web-gas-test2 --region asia-northeast1
```

## 基本的な Google Cloud CLI コマンド

Google Cloud を使い始めるために必要な基本的なコマンドを紹介します。

| コマンド | 説明 | 実行内容 | 初心者向けポイント |
|---------|------|----------|-------------------|
| `gcloud init` | 初回セットアップ（対話式） | • Google アカウントでのログイン<br>• プロジェクトの選択または作成<br>• デフォルトのリージョン・ゾーンの設定 | • 初めて Google Cloud CLI を使う場合は、まずこのコマンドを実行<br>• ブラウザが開いて Google アカウントでの認証が必要<br>• 複数のプロジェクトがある場合は選択可能 |
| `gcloud auth login` | Google アカウント認証 | • ブラウザが開いて Google アカウントでの認証<br>• Google Cloud リソースへのアクセス権限の取得 | • `gcloud init` 実行済みの場合は通常不要<br>• 別のアカウントでログインし直したい場合に使用<br>• 複数のアカウントを管理している場合に便利 |
| `gcloud projects list` | プロジェクト一覧表示 | • アクセス可能な全ての Google Cloud プロジェクトを表示<br>• プロジェクト ID、名前、ステータスを確認<br>• 使用可能なプロジェクトの選択に役立つ | • 認証後にまず実行すると良い<br>• プロジェクト ID をコピーして設定コマンドで使用<br>• 権限がないプロジェクトは表示されない |
| `gcloud config set project PROJECT_ID` | プロジェクト設定 | • デフォルトで使用するプロジェクトの設定<br>• 以降の gcloud コマンドでこのプロジェクトが使用される | • `PROJECT_ID` は実際のプロジェクト ID に置き換える<br>• プロジェクト ID は `gcloud projects list` で確認<br>• プロジェクトを切り替えたい場合に使用 |
| `gcloud services enable SERVICE_NAME` | サービスの有効化 | • 指定した Google Cloud サービスを有効化<br>• API の使用許可を設定 | • 例: `gcloud services enable compute.googleapis.com`<br>• サービスを使用する前に必ず有効化が必要<br>• 有効化には数分かかる場合がある |
| `gcloud builds submit --tag gcr.io/PROJECT_ID/IMAGE_NAME` | Cloud Build でイメージをビルド | • ソースコードから Docker イメージを自動ビルド<br>• Google Container Registry (GCR) に自動プッシュ<br>• クラウド上でのビルド処理 | • Cloud Build API の有効化が必要<br>• PROJECT_ID は実際のプロジェクト ID に置き換える<br>• IMAGE_NAME は任意のイメージ名を指定<br>• Dockerfile または buildpacks が必要 |
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

# 利用可能なプロジェクト一覧を確認
gcloud projects list

# プロジェクト設定
gcloud config set project my-gcp-project-123

# サービスの有効化（例：Compute Engine）
gcloud services enable compute.googleapis.com

# Cloud Build でコンテナイメージをビルド・プッシュ
gcloud builds submit --tag gcr.io/my-gcp-project-123/my-app

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
| `docker images` | Docker イメージ一覧表示 | • ローカルに保存されている全ての Docker イメージを表示<br>• イメージ名、タグ、作成日時、サイズを確認 | • ビルドしたイメージの確認に使用<br>• 不要なイメージの特定にも便利<br>• `docker rmi` でイメージを削除可能 |
| `docker run -d -p 8080:8080 今のディレクトリ` | コンテナの実行 | • ビルドしたイメージからコンテナを起動<br>• `-d` でバックグラウンド実行<br>• `-p 8080:8080` でポート 8080 をマッピング | • `-d` がないとターミナルがブロックされる<br>• ポート番号はアプリケーションに合わせて変更<br>• イメージ名は build 時のタグと一致させる |
| `http://localhost:8080` | アプリケーションへのアクセス | • ブラウザで実行中のコンテナにアクセス<br>• ローカル開発環境での動作確認 | • コンテナが正常に起動していることを確認<br>• ポート番号は docker run で指定したものと一致<br>• アプリケーションの起動に時間がかかる場合がある |
| `docker ps` | 実行中コンテナ一覧 | • 現在実行中の全てのコンテナを表示<br>• コンテナ ID、イメージ名、ポートマッピングなどを確認 | • `-a` オプションで停止済みコンテナも表示<br>• コンテナの動作状況を確認<br>• コンテナ ID は stop コマンドで使用 |
| `docker logs CONTAINER_ID` | コンテナのログ表示 | • 指定したコンテナの標準出力とエラーログを表示<br>• アプリケーションの動作状況やエラーを確認 | • コンテナ ID は `docker ps` で確認<br>• `-f` オプションでリアルタイム表示<br>• デバッグ時に最も重要なコマンド |
| `docker exec -it CONTAINER_ID bash` | コンテナ内でコマンド実行 | • 実行中のコンテナ内でコマンドを実行<br>• `-it` オプションで対話モード<br>• コンテナ内部の調査や設定変更が可能 | • コンテナが実行中である必要がある<br>• `bash` の代わりに `sh` を使用する場合もある<br>• デバッグや調査に便利 |
| `docker stop CONTAINER_ID` | コンテナの停止 | • 指定したコンテナを安全に停止<br>• CONTAINER_ID は `docker ps` で確認 | • コンテナ ID は最初の数文字のみでも可<br>• 複数のコンテナを同時に停止可能<br>• 強制停止は `docker kill` を使用 |
| `docker rm CONTAINER_ID` | コンテナの削除 | • 停止済みのコンテナを完全に削除<br>• ディスク容量の節約とクリーンアップ | • 実行中のコンテナは削除できない<br>• 先に `docker stop` で停止が必要<br>• `-f` オプションで強制削除可能 |
| `docker container prune` | 停止済みコンテナの一括削除 | • 停止している全てのコンテナを一括削除<br>• 確認プロンプトが表示される<br>• ディスク容量を効率的に節約 | • 実行中のコンテナには影響しない<br>• 削除前に確認プロンプトで `y` を入力<br>• 定期的なクリーンアップに便利 |
| `docker rmi IMAGE_ID` | イメージの削除 | • 不要な Docker イメージを削除<br>• IMAGE_ID は `docker images` で確認 | • 使用中のイメージは削除できない<br>• 関連コンテナを先に削除が必要<br>• ディスク容量の節約に重要 |
| `docker image prune -a` | 未使用イメージの一括削除 | • 使用されていない全ての Docker イメージを削除<br>• ディスク容量を大幅に節約<br>• 確認プロンプトが表示される | • `-a` は全ての未使用イメージを対象<br>• 削除前に確認プロンプトで `y` を入力<br>• 定期的な実行でディスク容量を管理 |
| `docker pull IMAGE_NAME` | イメージのダウンロード | • Docker Hub やレジストリからイメージをダウンロード<br>• Google Cloud Container Registry からも取得可能 | • `docker run` 時に自動でダウンロードも可能<br>• 事前ダウンロードで起動時間短縮<br>• バージョンタグの指定も可能 |
| `docker info` | Docker システム情報表示 | • Docker の設定情報とシステム状態を表示<br>• インストール状況やリソース使用量を確認 | • Docker が正しくインストールされているかの確認<br>• トラブルシューティング時に有用<br>• システムリソースの確認にも使用 |

**Docker 使用例:**
```bash
# Docker イメージをビルド（例：my-app という名前）
docker build -t my-app .

# ビルド済みイメージの確認
docker images

# コンテナをバックグラウンドで実行
docker run -d -p 8080:8080 my-app

# ブラウザでアクセス
# http://localhost:8080

# 実行中のコンテナを確認
docker ps

# コンテナのログを確認（デバッグ時）
docker logs CONTAINER_ID

# コンテナ内部にアクセス（調査・デバッグ時）
docker exec -it CONTAINER_ID bash

# Docker Hub からイメージをダウンロード
docker pull nginx:latest

# Docker システム情報を確認
docker info

# コンテナを停止（CONTAINER_ID は docker ps で確認）
docker stop CONTAINER_ID

# 停止済みコンテナを削除
docker rm CONTAINER_ID

# 停止済みコンテナを一括削除（クリーンアップ）
docker container prune

# 不要なイメージを削除
docker rmi IMAGE_ID

# 未使用イメージを一括削除（ディスク容量節約）
docker image prune -a
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