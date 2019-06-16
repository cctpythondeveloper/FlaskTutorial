# CRUD処理

## 使い方
```shell
$ pipenv shell
$ pipenv install
$ python server.py
```

## 画面
- ログインフォーム
- ユーザ登録フォーム
- ToDoList
- ToDo新規登録
- ToDo編集

## 機能
- ログイン
- ユーザ登録
- ToDo表示
- ToDo削除
- ToDo編集
- ToDo登録

## DB
USERS

|column_name|Type|Other|Description|
|:--|:--|:--|:---|
|id|int|primary||
|name|String(20)||ユーザの名前|
|password|String(20)||ログイン用パスワード|

TODOS

|column_name|Type|Other|Description|
|:--|:--|:--|:---|
|id|int|primary||
|title|String(20)||タイトル|
|content|Text||内容|
|userid|int|外部キー|USERSと紐付けるためのデータ|
|tododate|DateTime||いつのToDoか|

## データベースの作り方
