import mesop as me
from app import global_state

def profile():
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
                me.markdown("Log in to access your profile.", style=me.Style(color="white", font_size=15))
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
        # TO-DO : ADD SIDENAV UI

        # Background box styling
        with me.box(style=me.Style(padding=me.Padding.all(0),
                                   width=me.viewport_size().width,
                                   height=me.viewport_size().height,
                                   background="content-box radial-gradient(#0B0C10, #1F2833)",
                                   display="flex",
                                   justify_content="center",
                                   align_items="center",
                                   flex_direction="column", )
                    ):
            # Profile picture
            with me.box(style=me.Style(margin=me.Margin.all(0),
                                       background="black",
                                       width=500,
                                       height=550,
                                       display="flex",
                                       justify_self="center",
                                       # justify_content="center",
                                       align_items="center",
                                       border_radius=50,
                                       box_shadow="4px 4px 4px grey",
                                       flex_direction="column",
                                       gap=5,
                                       )
                        ):
                me.icon("person", style=me.Style(
                    margin=me.Margin.symmetric(vertical=65),
                    color="black",
                    background="white",
                    border_radius=25,
                    width=40,
                    height=40,
                    display="flex",
                    justify_content="center",
                    align_items="center",
                ))
                with me.box(style=me.Style(
                        # background="white",
                        width=500,
                        height=100,
                        display="flex",
                        justify_self="center",
                        justify_content="center",
                        align_items="center",
                        flex_direction="row",
                        gap=30,
                        border_radius=50,
                )
                ):
                    # TO-DO:FETCH USERNAME FROM DATABASE

                    me.markdown("Name : ", style=me.Style(
                        font_family="Arial",
                        color="white",
                    ))
                    me.text(f"{global_state.user_name}", style=me.Style(
                        font_size=20,
                        color="white",
                        font_family="monospace",
                    ))

                with me.box(style=me.Style(
                        # background="white",
                        width=500,
                        height=100,
                        display="flex",
                        justify_self="center",
                        justify_content="center",
                        align_items="center",
                        flex_direction="row",
                        gap=30,
                        border_radius=50,
                )
                ):
                    me.markdown("Email ID : ", style=me.Style(
                        color="white",
                        font_family="Arial",
                    ))
                    me.text(f"{global_state.user_email}", style=me.Style(
                        font_size=20,
                        font_family="monospace",
                        color="white",
                    ))



