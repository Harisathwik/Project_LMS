import mesop as me
from app import temp_state, global_state


def reset_state(temp_state):
    temp_state.user_email = ""
    temp_state.user_password = ""
    temp_state.user_name = ""
    temp_state.error_message = "Page Not Found"
    temp_state.logged_status = False


def logout_click(event: me.ClickEvent):
    reset_state(global_state)
    me.navigate("/")  # Redirect to Main Page after logout


def on_blur_email(event: me.InputBlurEvent):
    temp_state.user_email = event.value


def on_blur_password(event: me.InputBlurEvent):
    temp_state.user_password = event.value

def on_blur_name(event: me.InputBlurEvent):
    temp_state.user_name = event.value
