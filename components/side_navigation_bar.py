import mesop as me
from components import on_sidenav_click, SideNavState


def side_navigation():
    state = me.state(SideNavState)
    # Side Navigation
    with me.sidenav(opened=state.sidenav_open,
                    style=me.Style(width=250,
                                   # background="yellow",
                                   )):
        # Navigation Box
        with me.box(style=me.Style(padding=me.Padding.all(10), background="Black", border_radius=5, height=me.viewport_size().height-1, width=250)):
            me.text("Dashboard", style=me.Style(
                margin=me.Margin.symmetric(vertical=20),
                color="white",
                font_weight="bold",
                font_family="system-ui",
                # align_self="center",
                justify_content="center",
                display="flex",
                font_size=20
            ))
            # P R O F I L E
            with me.box(
                    style=me.Style(
                        # margin=me.Margin.symmetric(vertical=20, horizontal=0),
                        display="flex",
                        justify_content="center",
                        align_items="center",
                        width=220,
                        height=80,
                        flex_direction="row",
                        # border_radius=30,
                        # background="lightblue"

                    ),
            ):
                me.icon("person", style=me.Style(margin=me.Margin.symmetric(vertical=30, horizontal=10), color="black",
                        display="flex", background="white", border_radius=25, width=40, height=40,
                        justify_content="center", align_items="center"))
                me.button("Profile",on_click=lambda event: me.navigate("/profile"), style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10),
                    height=40,
                    width=150,
                    color="Black",
                    background="white"))
            # S U B J E C T S
            with me.box(style=me.Style(
                display="flex",
                justify_content="center",
                align_items="center",
                height=80,
                width=220,
                # border_radius=20,
                # background="yellow",
                flex_direction="row"
                # margin=me.Margin.symmetric(vertical=20)
            )):
                me.icon("book", style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10), color="Black", display="flex",
                    background="white", border_radius=25, width=40, height=40, justify_content="center",
                    align_items="center"))
                me.button("Subjects",on_click=lambda event: me.navigate("/subjects"), style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10),
                    height=40, width=150,
                    color="Black",
                    background="white"))
            # A C C O U N T
            with me.box(style=me.Style(
                display="flex",
                justify_content="center",
                align_items="center",
                height=80,
                width=220,
                # border_radius=20,
                # background="violet",
                flex_direction="row"
                # margin=me.Margin.symmetric(vertical=20)
            )):
                me.icon("dashboard", style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10), color="Black", display="flex", background="white",
                    border_radius=25, width=40, height=40, justify_content="center",
                    align_items="center"))
                me.button("Account", style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10),
                    height=40, width=150, color="Black", background="white"))
            # C H A T W I T H  U S
            with me.box(style=me.Style(
                display="flex",
                justify_content="center",
                align_items="center",
                height=80,
                width=220,
                # border_radius=20,
                # background="lightgreen",
                flex_direction="row"
                # margin=me.Margin.symmetric(vertical=20)
            )):
                me.icon("chat", style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10), color="Black", display="flex", background="white",
                    border_radius=25, width=40, height=40, justify_content="center",
                    flex_direction="row", align_items="center"))
                me.button("Chat With Us", on_click=lambda event: me.navigate("/chatwithus"), style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10),
                    height=40, width=150, color="Black", background="white"))
            # L O G O U T
            with me.box(style=me.Style(
                display="flex",
                justify_content="center",
                align_items="center",
                height=80,
                width=220,
                # border_radius=20,
                # background="red",
                flex_direction="row"
                # margin=me.Margin.symmetric(vertical=20)
            )):
                me.icon("logout", style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10), color="Black", display="flex",
                    background="white", border_radius=25, width=40, height=40,
                    justify_content="center", align_items="center"))
                me.button("Log Out",on_click=lambda event: me.navigate("/logout"), style=me.Style(
                    margin=me.Margin.symmetric(vertical=30, horizontal=10),
                    height=40, width=150, color="Black", background="white"))

    # HamBurger Button
    with me.box(
            style=me.Style(
                margin=me.Margin(left=250 if state.sidenav_open else 0),
                width=70,
                height=45,
                display="flex",
                justify_content="center",
                justify_self="center",
                # background="red",
                align_items="center"
            ),
    ):
        with me.content_button(on_click=on_sidenav_click,
                               style=me.Style(
                                   color="black",
                                   display="flex",
                                   # background="lightgreen",
                                   # border_radius=20,
                                   width=40,
                                   height=45,
                                   justify_content="center",
                                   align_items="center",
                                   align_self="center"
                               )):
            me.icon("menu", style=me.Style(margin=me.Margin.symmetric(vertical=20, horizontal=2),
                                           color="black",
                                           display="flex",
                                           background="white",
                                           border_radius=50,
                                           width=35,
                                           height=35,
                                           justify_content="center",
                                           align_items="center",
                                           align_self="center"
                                           ))
