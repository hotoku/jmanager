# Jmanager

A lightweight Jupyter process manager

## リリース手順

1. `make <major|minor|patch>`を実行。ソースファイル中のバージョン番号文字列が新しいバージョン番号に置換され、タグが打たれる。
1. 環境変数`PYPI_TOKEN`にリリース用のAPI TOKENを設定する。
1. `make publish`を実行。
