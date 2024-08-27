import mesop as me
from services.firebase_service import authentication, db
from app import global_state, temp_state


# Authenticate a user using email/password
def authenticate_user(event: me.ClickEvent):
    try:
        user = authentication.sign_in_with_email_and_password(temp_state.user_email, temp_state.user_password)

        global_state.logged_status = True
        global_state.user_name = temp_state.user_name
        global_state.user_email = temp_state.user_email
        global_state.user_id = user['localId']


        # User is authenticated, you can access user data here
        me.text(f"User authenticated: {global_state.user_email}")

        me.text(f"User ID: {user['localId']}")
        me.navigate("/")  # Redirect to Main Page after login
        return None
    except Exception as e:
        global_state.error_message = f"Authentication error: {e}"
        me.navigate("/error")

def create_user_in_firestore(user_id, email, name):
    try:
        # Reference to the users collection
        users_ref = db.collection('UserProfileDetails')

        # Create a new document in the users collection with user_id as the document ID
        users_ref.document(user_id).set({
            'email': email,
            'name': name,
            'role': 'student'  # You can set roles like 'student', 'teacher', etc.
        })
        me.text(f"User {email} added to Firestore.")
    except Exception as e:
        me.text(f"Error adding user to Firestore: {e}")



# Create a new user
def create_user(event: me.ClickEvent):
    try:
        user = authentication.create_user_with_email_and_password(email=temp_state.user_email, password=temp_state.user_password)
        global_state.password = ""  # Clear the password after user creation
        global_state.logged_status = True
        global_state.user_id = user['localId']
        global_state.user_name = temp_state.user_name
        global_state.user_email = temp_state.user_email
        me.text(f"User ID: {user['localId']}")
        # Example usage after user signup
        create_user_in_firestore(global_state.user_id, global_state.user_email, global_state.user_name)
        me.navigate("/")  # Redirect to Main Page after user
    except Exception as e:
        global_state.error_message = f"Error: {e}"
        me.navigate("/error")
