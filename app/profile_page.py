import mesop as me
from app import global_state
from components.side_navigation_bar import side_navigation
from components.popupbox_page import popup_box

def profile():
    if not global_state.logged_status:
        popup_box(actions=["Log in to access your profile.", "Login", "/login", "Back to Home", "/"])

    else:
        # Background box styling
        with me.box(style=me.Style(
                    background="content-box linear-gradient(#0B0C10,#1F2833)",
                    width=me.viewport_size().width - 8,
                    height=me.viewport_size().height - 4,
                )
                    ):
            side_navigation()
            # Profile picture
            with me.box(style=me.Style(
                    # background="content-box radial-gradient(#0B0C10, #1F2833)",
                    padding=me.Padding.all(10),
                    width=me.viewport_size().width - 10,
                    height=me.viewport_size().height - 50,
                    display="flex",
                    justify_self="center",
                    justify_content="center",
                    align_items="center",
                    flex_direction="column",
                    flex_grow=1,
            )
            ):
                with me.box(style=me.Style(margin=me.Margin.all(0),
                                           background="black",
                                           width=500,
                                           height=550,
                                           display="flex",
                                           justify_self="center",
                                           justify_content="center",
                                           align_self="center",
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


