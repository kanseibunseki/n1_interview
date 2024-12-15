import pyrebase

config = {
  "apiKey": "your-api-key",
  "authDomain": "your-project.firebaseapp.com",
  "databaseURL": "https://your-project.firebaseio.com",
  "storageBucket": "your-project.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# ユーザー登録の例
user = auth.create_user_with_email_and_password("user@example.com", "password")
