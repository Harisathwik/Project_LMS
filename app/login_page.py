import mesop as me
from services.authentication import authenticate_user
from app import global_state
from app.views import on_blur_email, on_blur_password


def login():
    if not global_state.logged_status:
        me.text("Login Page")

        me.input(label="Email", type="email", required=True, on_blur=on_blur_email)
        me.input(label="Password", type="password", required=True, on_blur=on_blur_password)

        me.button("Login", on_click=authenticate_user)  # Assume signup also logs in the user
        me.button("Signup", on_click=lambda event: me.navigate("/signup"))
    else:
        me.text("You are already logged in.")
        me.button("Home", on_click=lambda event: me.navigate("/"))
