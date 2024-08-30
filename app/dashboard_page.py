import mesop as me
from app import global_state
from components.side_navigation_bar import side_navigation

def dashboard():
    if not global_state.logged_status:
        # Background styling
        with me.box(style=me.Style(
                background="content-box radial-gradient(#0B0C10, #1F2833)",
                width=me.viewport_size().width,
                height=me.viewport_size().height,
                display="flex",
                justify_content="center",
                align_items="center")
        ):
            # Pop-Up box for login and signup
            with me.box(style=me.Style(
                    background="black",
                    display="flex",
                    width=500,
                    height=200,
                    justify_content="center",
                    align_items="center",
                    flex_direction="column",
                    border_radius=20,
                    box_shadow="4px 4px 4px grey",
                    gap=20, )
            ):
                me.markdown("Login to access the classroom", style=me.Style(color="white", font_size=15))
                with me.box(style=me.Style(
                        # background="yellow",
                        display="flex",
                        flex_direction="row",
                        gap=20)
                ):
                    me.button("Login", type="raised", on_click=lambda event: me.navigate("/login"),
                              style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white"))
                    me.button("SignUp", type="raised", on_click=lambda event: me.navigate("/signup"),
                              style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white"))
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

