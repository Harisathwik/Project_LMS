import mesop as me
from app import global_state
from app.views import on_blur_email, on_blur_password, on_blur_name
from services.authentication import create_user

def signup():
    if global_state.logged_status:
        me.text("You already logged in.")
        me.button("Home", on_click=lambda event: me.navigate("/"))
    else:
        me.text("Signup Page")

        me.input(label="Name", type="text", required=True, on_blur=on_blur_name)
        me.input(label="Email", type="email", required=True, on_blur=on_blur_email)
        me.input(label="Password", type="password", required=True, on_blur=on_blur_password)

        me.button("Signup", on_click=create_user)  # Assume signup also logs in the user
        me.button("Login", on_click=lambda event: me.navigate("/login"))
