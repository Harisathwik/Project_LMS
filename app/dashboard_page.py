import mesop as me
from app import global_state
from components.side_navigation_bar import side_navigation
from components.popupbox_page import popup_box

def dashboard():
    if not global_state.logged_status:
        popup_box(actions=["Login to access the classroom", "Login", "/login", "SignUp", "/signup"])
    else:

        # Background styling
        with me.box(
                style=me.Style(
                    background="content-box linear-gradient(#0B0C10,#1F2833)",
                    width=me.viewport_size().width - 8,
                    height=me.viewport_size().height - 4,
                )
        ):
            # Function call to display side navigation bar from sie_navigation_bar.py
            side_navigation()
            # Main Content Box
            with me.box(style=me.Style(
                    # background="content-box radial-gradient(#0B0C10, #1F2833)",
                    padding=me.Padding.all(10),
                    width=me.viewport_size().width-10,
                    height=me.viewport_size().height-50,
                    display="flex",
                    justify_self="center",
                    justify_content="center",
                    align_items="center",
                    flex_direction="column",
                    flex_grow=1,
            )
            ):
                me.markdown("##Welcome to the Classroom", style=me.Style(color="white", font_size=15,font_family="montserrat"))

