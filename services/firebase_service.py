import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
import json


# User login system
with open("app_credentials.json", "r") as f:
    config_app = json.load(f)
    firebase_app = pyrebase.initialize_app(config_app)
    authentication = firebase_app.auth()


# Initialize Firebase firestore
cred = credentials.Certificate('firestore_credentials.json')
firebase_admin.initialize_app(cred)

# Initialize Firestore Database
db = firestore.client()
