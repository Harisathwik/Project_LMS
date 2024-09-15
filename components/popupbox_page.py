import mesop as me

def popup_box(actions: list):
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
            me.markdown(actions[0], style=me.Style(color="white", font_size=15))
            with me.box(style=me.Style(
                    # background="yellow",
                    display="flex",
                    flex_direction="row",
                    gap=20)
            ):
                me.button(actions[1], type="raised", on_click=lambda event: me.navigate(actions[2]),
                          style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white"))
                me.button(actions[3], type="raised", on_click=lambda event: me.navigate(actions[4]),
                          style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white"))
