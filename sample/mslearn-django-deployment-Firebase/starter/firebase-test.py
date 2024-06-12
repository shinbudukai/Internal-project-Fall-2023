import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("sample-deployment-2034e-firebase-adminsdk-4rzsk-87e8544ad9.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {

    'task':'wash the dishes',
    'status':'TODOO'
}

doc_ref = db.collection("taskCollection").document()
doc_ref.set(data)

print("Document ID:", doc_ref.id)