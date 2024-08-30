import mesop as me

def about():
    # Background Box and Style
    with me.box(
            style=me.Style(
                background="content-box linear-gradient(#0B0C10,black)",
                flex_direction="row",
                display="flex",
                gap=10,
                # justify_content="center",
                justify_self="center",
                # align_items="center",
                width=me.viewport_size().width,
                height=me.viewport_size().height - 4,
            )

    ):
        # About section
        with me.box(style=me.Style(
                # background="lightblue",
                padding=me.Padding.all(25),
                width=me.viewport_size().width // 2 + 110,
                height=me.viewport_size().height - 4,
                flex_direction="column",
                display="flex",
                justify_content="center",
                align_items="start",
        )
        ):
            me.markdown("#ProjectLMS", style=me.Style(color="white", font_size=30, font_family="monospace"))
            me.markdown(
                "Learning Management System is a platform that helps students to learn and grow in their respective fields. This is a student friendly application aims to help students in their learning process.",
                style=me.Style(color="white", font_family="montserrat", ))
        # Meet Team Section
        with me.box(style=me.Style(
                background="content-box linear-gradient(#0B0C10,black)",
                # background="content-box linear-gradient(#f69d3c, #3f87a6)",
                # background="content-box linear-gradient(#0B0C10,black)",
                # background="content-box linear-gradient(135deg, #00C9A7 0%, #0052D4 100%)",
                # background="content-box linear-gradient(135deg, #00F260 0%, #0575E6 100%)",
                # background="content-box  linear-gradient(135deg, #8A2387 0%, #E94057 50%, #F27121 100%)",
                # background="content-box linear-gradient(crimson,black)",
                # padding=me.Padding.all(10),
                width=me.viewport_size().width // 2 - 110,
                height=me.viewport_size().height - 4,
                display="flex",
                # justify_content="center",
                align_items="center",
                flex_direction="column",
                border=me.Border.symmetric(
                    horizontal=me.BorderSide(width=1, color="white", style="solid"),
                    # vertical=me.BorderSide(width='0.5em', color="white", style="inset"),
                ),
                border_radius=25,
                box_shadow="-0.25em 0 .4em white",
        )
        ):
            me.markdown("##Meet the Team", style=me.Style(color="white", font_size=30, font_family="monospace"))
            me.markdown("The Minds Behind ProjectLMS",
                        style=me.Style(color="white", font_size=15, font_family="montserrat"))
            with me.box(style=me.Style(
                    # background="white",
                    width=600,
                    height=500,
                    flex_direction="column",
                    display="flex",
                    justify_content="center",
                    align_items="center",
            )):
                me.image(src="https://cdn.jsdelivr.net/gh/alohe/avatars/png/vibrent_26.png",
                         style=me.Style(width=100, height=100, border_radius=50))
                with me.box(
                        style=me.Style(
                            # background="yellow",
                            width=250,
                            height=100,
                            justify_content="center",
                            justify_self="center",
                            align_items="center",
                            display="flex",
                            flex_direction="row",
                            gap=10,
                        )
                ):
                    me.image(src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
                             style=me.Style(width=40, height=40))
                    me.link(text="Nithya", open_in_new_tab=True,
                            url="https://www.linkedin.com/in/harinithyaveerla/",
                            style=me.Style(color="white", font_family="monospace"))

                me.image(src="https://cdn.jsdelivr.net/gh/alohe/avatars/png/upstream_13.png",
                         style=me.Style(width=100, height=100, border_radius=50))
                with me.box(
                        style=me.Style(
                            margin=me.Margin.all(10),
                            # background="yellow",
                            width=250,
                            height=100,
                            justify_content="center",
                            justify_self="center",
                            align_items="center",
                            display="flex",
                            flex_direction="row",
                            gap=10,
                        )
                ):
                    me.image(src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
                             style=me.Style(width=40, height=40))
                    me.link(text="Sathwik", open_in_new_tab=True,
                            url="https://www.linkedin.com/in/harisathwik-veerla/",
                            style=me.Style(color="white", font_family="monospace"))