import mesop as me
# from app import global_state
from app.login_page import login
from app.signup_page import signup
from app.error_page import error
from app.logout_page import logout
from app.profile_page import profile
from app.dashboard_page import dashboard
from app.landing_page import landing
from app.subjects_page import subjects

@me.page(path="/profile")
def profile_page():
    profile()


@me.page(path="/")
def main():
    landing()

@me.page(path="/login")
def login_page():
    login()

@me.page(path="/signup")
def signup_page():
    signup()

@me.page(path="/dashboard")
def dashboard_page():
    dashboard()

@me.page(path="/subjects")
def subjects_page():
    subjects()

@me.page(path="/logout")
def logout_page():
    logout()

@me.page(path="/error")
def error_page():
    error()
