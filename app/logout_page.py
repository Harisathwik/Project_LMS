from app import global_state
from app.views import logout_click
import mesop as me
from components.popupbox_page import popup_box

def logout():
    if not global_state.logged_status:
        popup_box(actions=["You haven't logged in.", "Login", "/login", "Back to Home", "/"])

    else:
        popup_box(actions=["Are you sure you want to Logout?", "Yes", "logout", "No", "/"])
