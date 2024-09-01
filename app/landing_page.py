import mesop as me

def landing():
    with me.box(style=me.Style(
            background="black",
            flex_direction="row",
            display="flex",
            gap=6,
            justify_content="center",
            justify_self="center",
            align_items="center",
            width=me.viewport_size().width,
            height=60,

    )
    ):
        me.button("Home", style=me.Style(
            color="white",
            display="flex",
            font_size=15,
            font_family="monospace",

        )
                  )
        me.button("About", on_click=lambda event: me.navigate("/about"), style=me.Style(
            color="white",
            display="flex",
            font_size=15,
            font_family="monospace"))

        me.button("Classroom", on_click=lambda event: me.navigate("/dashboard"),
                  style=me.Style(color="white", display="flex", background="crimson", font_size=15, border_radius=12,
                                 height=37,
                                 font_family="monospace"))
    with me.box(
            style=me.Style(
                display="flex",
                background="content-box radial-gradient(gold,orange,purple,indigo,black)",
                height=me.viewport_size().height,
                width=me.viewport_size().width,
                justify_content="center",
                align_items="center",
                flex_direction="column",
            )
    ):
        me.markdown("Welcome to the Space_", style=me.Style(
            # color="white",
            color="white",
            display="flex",
            font_size=30,
            font_family="Jetbrains Mono",
            justify_self="center",
            align_items="center"))
