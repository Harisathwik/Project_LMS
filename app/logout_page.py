from app import global_state
from app.views import logout_click
import mesop as me

def logout():
    if not global_state.logged_status:
        # Background box styling
        with me.box(style=me.Style(
                background="content-box radial-gradient(#0B0C10, #1F2833)",
                width=me.viewport_size().width,
                height=me.viewport_size().height,
                display="flex",
                justify_content="center",
                align_items="center")
        ):
            # Confirm Logout box and styling
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
                me.markdown("You haven't logged in.", style=me.Style(color="white", font_size=15))
                with me.box(style=me.Style(
                        # background="yellow",
                        display="flex",
                        flex_direction="row",
                        gap=20)
                ):
                    me.button("Login", type="raised", on_click=lambda event: me.navigate("/login"),
                              style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white"))
                    me.button("Back to Home", type="raised", on_click=lambda event: me.navigate("/"),
                              style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white"))
    else:
        # Background box styling
        with me.box(style=me.Style(
                background="content-box radial-gradient(#0B0C10, #1F2833)",
                width=me.viewport_size().width,
                height=me.viewport_size().height,
                display="flex",
                justify_content="center",
                align_items="center")
        ):
            # Confirm Logout box and styling
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
                me.markdown("Are you sure you want to Logout?", style=me.Style(color="white", font_size=15))
                with me.box(style=me.Style(
                        # background="yellow",
                        display="flex",
                        flex_direction="row",
                        gap=20)
                ):
                    me.button("Yes", type="raised", on_click=logout_click,
                              style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white"))
                    me.button("No", type="raised", on_click=lambda event: me.navigate("/"),
                              style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white"))

