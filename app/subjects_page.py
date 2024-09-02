import mesop as me
from app import global_state
from components.side_navigation_bar import side_navigation


def subjects():
    # Check if user is logged in
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
        # Background Box and Style
        with me.box(
                style=me.Style(
                    background="content-box linear-gradient(#0B0C10,#1F2833)",
                    width=me.viewport_size().width - 8,
                    height=me.viewport_size().height - 4,
                )
        ):
            side_navigation()
            # Main Content Box
            with me.box(
                style=me.Style(
                    # background="content-box linear-gradient(crimson,black)",
                    padding=me.Padding.all(10),
                    width=me.viewport_size().width-10,
                    height=me.viewport_size().height-50,
                    display="flex",
                    justify_self="center",
                    justify_content="center",
                    align_items="center",
                    flex_direction="row",
                    flex_grow=1,
                    gap=10,
                )
            ):
                # Main Content
                with me.box(style=me.Style(
                        background="white",
                        width=310,
                        height=300,
                        display="flex",
                        border_radius=20,
                        align_items="center",
                        justify_content="space-around",
                        flex_direction="column",
                )):
                    me.image(
                        src="https://img.freepik.com/free-photo/programming-background-with-person-working-with-codes-computer_23-2150010125.jpg",
                        alt="Random Image",
                        style=me.Style(
                            width=310,
                            height=220,
                            border_radius=20,

                        ),
                    )
                    me.button("Programming", style=me.Style(font_weight="bold",
                                                       font_family="Jetbrains Mono",
                                                       font_size=20), )
                with me.box(style=me.Style(
                        background="white",
                        width=310,
                        height=300,
                        display="flex",
                        border_radius=20,
                        align_items="center",
                        justify_content="space-around",
                        flex_direction="column",
                )):
                    me.image(
                        src="https://img.freepik.com/free-vector/internal-structure-stem-diagram_1308-128158.jpg",
                        alt="Random Image",
                        style=me.Style(
                            width=310,
                            height=220,
                            border_radius=20,

                        ),
                    )
                    me.button("Biology", style=me.Style(font_weight="bold",
                                                        font_family="Jetbrains Mono",
                                                        font_size=20),)
                with me.box(style=me.Style(
                        background="white",
                        width=310,
                        height=300,
                        display="flex",
                        border_radius=20,
                        align_items="center",
                        justify_content="space-around",
                        flex_direction="column",
                )):
                    me.image(
                        src="https://img.freepik.com/free-vector/maths-chalkboard_23-2148178219.jpg",
                        alt="Random Image",
                        style=me.Style(
                            width=310,
                            height=220,
                            border_radius=20,

                        ),
                    )
                    me.button("Mathematics", style=me.Style(font_weight="bold",
                                                                 font_family="Jetbrains Mono",
                                                                 font_size=20
                                                                 ), )
                with me.box(style=me.Style(
                        background="white",
                        width=310,
                        height=300,
                        display="flex",
                        border_radius=20,
                        align_items="center",
                        justify_content="space-around",
                        flex_direction="column",
                )):
                    me.image(
                        src="https://img.freepik.com/free-photo/full-shot-astronauts-wearing-equipment_23-2151075886.jpg"
                        , style=me.Style(
                            width=310,
                            height=220,
                            border_radius=20,

                        ),
                        )
                    me.button("Astro Physics", style=me.Style(font_weight="bold",
                                                           font_family="Jetbrains Mono",
                                                           font_size=20)
                              )