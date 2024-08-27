import mesop as me
from app import global_state

def profile():
    if not global_state.logged_status:
        me.text("Please login to access this page")
        me.button("Login", on_click=lambda event: me.navigate("/login"))
    else:
        me.text("Profile Page")
        me.text(f"Name: {global_state.user_name}")
        me.text(f"Email: {global_state.user_email}")