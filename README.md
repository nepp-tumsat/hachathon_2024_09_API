# hachathon_2024_09_API
##　共同開発者;

Doragon-RH

taqtq



https://github.com/user-attachments/assets/fbf7e268-9424-40b4-9b89-e603c4682b75


## 苦労したこと
日時をフロント側で入力することなく、自動的に処理いたタイミングでDBの方に送る処理の記述、型定義

同じファイルを編集してしまい、コンフリクトの解決を行なったこと

# 以下ルートディレクトリでコマンドラインに打ち込む
## Docker imageの作成
docker-compose build

## 定義ファイル作成
docker-compose run \
  --entrypoint "poetry init \
    --name demo-app \
    --dependency fastapi \
    --dependency uvicorn[standard]" \
  demo-app

## FASTapiインストール
docker-compose run --entrypoint "poetry install --no-root" demo-app

## ビルド
docker-compose build --no-cache

## API立ち上げ
docker-compose up

## Swagger UIのリンク
http://localhost:8000/docs

## mysql 立ち上げ
docker-compose exec db mysql demo

## パッケージのインストール
docker-compose exec demo-app poetry add sqlalchemy aiomysql

## DB作成
docker-compose exec demo-app poetry run python -m api.migrate_db

## mysql起動
docker-compose exec db mysql demo

## httpxインストール
docker-compose exec demo-app poetry add -D pytest-asyncio aiosqlite httpx

## テスト実行(ルートディレクトリ内で)
docker-compose run --entrypoint "poetry run pytest" demo-app

