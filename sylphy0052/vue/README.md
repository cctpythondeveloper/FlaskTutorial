# VueとFlaskを連携させる

## 手順
### クライアントサイドを作成する

```shell
# installする(管理者権限ないと怒られた)
$ sudo npm install -g vue-cli
# フロント用のディレクトリを作成する
$ mkdir flaskvue
$ cd flaskvue
$ vue init webpack frontend
# 自分にあったものを応える
$ cd frontend
$ npm install
$ npm run dev
# http://localhost:8080/で見れるはず
```

- `frontend/src/components` にファイルを作る
- routeにテンプレートを登録する(`frontend/src/router/index.js`)
- build先を変更する(`frontend/config/index.js`)
- `npm run build`を実行し，frontendと同じディレクトリに`dist`というディレクトリを生成する

### サーバサイドを作成する

```shell
$ mkdir backend
$ cd backend
$ pipenv --three
$ pipenv shell
$ pipenv install Flask
$ cd ..
$ touch run.py
# run.pyを書く
$ FLASK_APP=run.py FLASK_DEBUG=1 flask run
$ cd frontend
$ npm install --save axios
$ npm run build
```

## 問題
1. `error code ELIFECYCLE`が出た

```shell

```

## 参考
1. [Vue.js(vue-cli)とFlaskを使って簡易アプリを作成する【前半 - フロントエンド編】](https://qiita.com/mitch0807/items/2a93d93adbf6b5fc445c)
2. [Vue.jsとFlaskでフルスタックなWebアプリの開発環境を構築 その１〜〜環境構築〜〜](https://kittagon.hateblo.jp/entry/2018/08/27/011354)
