import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# ユーザー管理の例
user = auth.create_user(email="user@example.com", password="secretPassword")
