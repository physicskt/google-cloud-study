# google-cloud-study

このリポジトリは Google Cloud Platform (GCP) の学習用リポジトリです。

## 基本的な Google Cloud CLI コマンド

Google Cloud を使い始めるために必要な基本的なコマンドを紹介します。

| コマンド | 説明 | 実行内容 | 初心者向けポイント |
|---------|------|----------|-------------------|
| `gcloud init` | 初回セットアップ（対話式） | • Google アカウントでのログイン<br>• プロジェクトの選択または作成<br>• デフォルトのリージョン・ゾーンの設定 | • 初めて Google Cloud CLI を使う場合は、まずこのコマンドを実行<br>• ブラウザが開いて Google アカウントでの認証が必要<br>• 複数のプロジェクトがある場合は選択可能 |
| `gcloud auth login` | Google アカウント認証 | • ブラウザが開いて Google アカウントでの認証<br>• Google Cloud リソースへのアクセス権限の取得 | • `gcloud init` 実行済みの場合は通常不要<br>• 別のアカウントでログインし直したい場合に使用<br>• 複数のアカウントを管理している場合に便利 |
| `gcloud config set project PROJECT_ID` | プロジェクト設定 | • デフォルトで使用するプロジェクトの設定<br>• 以降の gcloud コマンドでこのプロジェクトが使用される | • `PROJECT_ID` は実際のプロジェクト ID に置き換える<br>• プロジェクト ID は Google Cloud Console で確認<br>• プロジェクトを切り替えたい場合に使用 |

**使用例:**
```bash
# 初回セットアップ
gcloud init

# 認証（必要に応じて）
gcloud auth login

# プロジェクト設定
gcloud config set project my-gcp-project-123
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

## 参考リンク

- [Google Cloud CLI ドキュメント](https://cloud.google.com/sdk/docs)
- [gcloud コマンドリファレンス](https://cloud.google.com/sdk/gcloud/reference)