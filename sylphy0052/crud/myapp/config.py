"""
設定ファイル
"""

import os

# Debugモード ON
DEBUG = True

# セッション情報を暗号化するためのシークレットキーをランダムに設定する
SECRET_KEY = os.urandom(24)

# database用の設定
SQLALCHEMY_DATABASE_URI = 'sqlite:///crudtb.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True