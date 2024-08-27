from app import global_state
from app.views import logout_click
import mesop as me

def logout():
    if not global_state.logged_status:
        me.text("You haven't logged in.")
        me.button("Login", on_click=lambda event: me.navigate("/login"))
    else:
        me.text("Logout Page")
        me.button("Logout", on_click=logout_click)
