import firebase_admin
from firebase_admin import credentials
from firebase_functions import https_fn
from flask import Flask, request

cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello from Firebase and Flask!'

@https_fn.on_request()
def my_function(request):
    return app(request)
