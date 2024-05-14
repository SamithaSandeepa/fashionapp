import pyrebase
from django.conf import settings
import firebase_admin
from firebase_admin import credentials

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
storage = firebase.storage()

def upload_image_to_firebase(file, file_name):
    try:
        # Upload image to Firebase Storage
        storage.child(f'images/{file_name}').put(file)

        # Get the download URL
        download_url = storage.child(f'images/{file_name}').get_url(None)

        return download_url

    except Exception as e:
        print(f"Error uploading image to Firebase: {e}")
        return None
