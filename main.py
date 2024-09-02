import mesop as me
from app.login_page import login
from app.signup_page import signup
from app.error_page import error
from app.logout_page import logout
from app.profile_page import profile
from app.dashboard_page import dashboard
from app.chatwithus_page import chat_with_us
from app.landing_page import landing
from app.about_page import about
from app.subjects_page import subjects

@me.page(path="/profile")
def profile_page():
    profile()


@me.page(path="/")
def main():
    landing()

@me.page(path="/about")
def about_page():
    about()

@me.page(path="/login")
def login_page():
    login()

@me.page(path="/signup")
def signup_page():
    signup()

@me.page(path="/dashboard")
def dashboard_page():
    dashboard()

@me.page(path="/chatwithus")
def chatbot_page():
    chat_with_us()

@me.page(path="/subjects")
def subjects_page():
    subjects()

@me.page(path="/logout")
def logout_page():
    logout()

@me.page(path="/error")
def error_page():
    error()
