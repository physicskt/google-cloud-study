# google-cloud-study

このリポジトリは Google Cloud Platform (GCP) の学習用リポジトリです。

## 基本的な Google Cloud CLI コマンド

Google Cloud を使い始めるために必要な基本的なコマンドを紹介します。

### 1. gcloud init

初回セットアップを行うコマンドです。Google Cloud CLI の設定を対話式で行います。

```bash
gcloud init
```

**このコマンドで行われること:**
- Google アカウントでのログイン
- プロジェクトの選択または作成
- デフォルトのリージョン・ゾーンの設定

**初心者向けポイント:**
- 初めて Google Cloud CLI を使う場合は、まずこのコマンドを実行してください
- ブラウザが開いて Google アカウントでの認証が求められます
- 複数のプロジェクトがある場合は、どれを使うか選択できます

### 2. gcloud auth login

Google アカウントでの認証を行うコマンドです。

```bash
gcloud auth login
```

**このコマンドで行われること:**
- ブラウザが開いて Google アカウントでの認証
- Google Cloud リソースへのアクセス権限の取得

**初心者向けポイント:**
- すでに `gcloud init` を実行済みの場合は通常不要です
- 別のアカウントでログインし直したい場合に使います
- 複数のアカウントを管理している場合に便利です

### 3. gcloud config set project

使用するプロジェクトを設定するコマンドです。

```bash
gcloud config set project PROJECT_ID
```

**例:**
```bash
gcloud config set project my-gcp-project-123
```

**このコマンドで行われること:**
- デフォルトで使用するプロジェクトの設定
- 以降の gcloud コマンドでこのプロジェクトが使用される

**初心者向けポイント:**
- `PROJECT_ID` は実際のプロジェクト ID に置き換えてください
- プロジェクト ID は Google Cloud Console で確認できます
- プロジェクトを切り替えたい場合にこのコマンドを使います

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

## 参考リンク

- [Google Cloud CLI ドキュメント](https://cloud.google.com/sdk/docs)
- [gcloud コマンドリファレンス](https://cloud.google.com/sdk/gcloud/reference)