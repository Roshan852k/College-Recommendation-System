# Importing Dependencies
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

from Alerts_and_Messages import Message

cred = credentials.Certificate("C:\\Users\\ROSHAN YADAV\\Contacts\\Desktop\\WORK\\FrontEnd\\Service_Account_Key.json")                        # Credentials of the Cloud Database
firebase_admin.initialize_app(cred)                                               # Initializing the Connection

db = firestore.client()                                                             # Database Object


def user_exists(collection_name, document_id):
    """Checks if a Document is present in the Database"""
    if db.collection(collection_name).document(document_id).get().exists:
        return 1

    else:
        return 0


def push_user_to_database(new_user):
    """Add User to The Database The input Parameter is a Dictionary"""
    document_id = new_user["Username"]                                              # Each Document Id is set to respective Username

    if user_exists("Users", document_id):                                           # If User Already Registered return -1
        return 0

    else:
        db.collection("Users").document(document_id).set(new_user)                  # Document Reference
        return 1


def get_data(document_id, field):
    user = db.collection("Users").document(document_id).get().to_dict()
    return user[field]


def generate_log(username, action):
    timestamp = datetime.now()
    document_id = timestamp.strftime("%d-%m-%Y %H:%M:%S")

    log = {
        "Username": username,
        "Action": action,
        "Time Stamp": timestamp
    }

    db.collection("Logs").document(document_id).set(log)


def generate_feedback(username, college_name, infra_review, placement_review, academics_review, campus_review):
    """Generate a Feedback and push it to the database"""

    feedback = {
            "Username" : username,
            "College Name" : college_name,
            "Infrastructure" : infra_review if infra_review else None,
            "Placement" : placement_review if placement_review else None,
            "Academics" : academics_review if academics_review else None,
            "Campus" : campus_review if campus_review else None
    }

    db.collection("Feedback").document(username).set(feedback)
