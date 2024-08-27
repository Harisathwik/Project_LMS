import mesop as me
from app import global_state
from app.login_page import login
from app.signup_page import signup
from app.error_page import error
from app.logout_page import logout
from app.profile_page import profile


@me.page(path="/profile")
def profile_page():
    profile()


@me.page(path="/")
def main():
    if not global_state.logged_status:
        me.text("Main Page")
        me.text("Login Status: Not logged in")
        me.button("Login", on_click=lambda event: me.navigate("/login"))
        me.button("Signup", on_click=lambda event: me.navigate("/signup"))
    else:
        me.text("Main Page")
        me.text("Login Status: Logged in")

        me.button("Profile", on_click=lambda event: me.navigate("/profile"))
        me.button("Logout", on_click=lambda event: me.navigate("/logout"))


@me.page(path="/login")
def login_page():
    login()

@me.page(path="/signup")
def signup_page():
    signup()

@me.page(path="/logout")
def logout_page():
    logout()

@me.page(path="/error")
def error_page():
    error()
