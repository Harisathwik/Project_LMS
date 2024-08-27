import mesop as me
from app import global_state

def error():
    if global_state.logged_status:
        me.text(global_state.error_message)
        me.button("Home", on_click=lambda event: me.navigate("/"))
    else:
        me.text(global_state.error_message)
        me.button("Login", on_click=lambda event: me.navigate("/login"))
