import mesop as me
from app import global_state
from app.views import on_blur_email, on_blur_password, on_blur_name
from services.authentication import create_user
from components.popupbox_page import popup_box

def signup():
    if global_state.logged_status:
        popup_box(actions=["You are already logged in.", "Home", "/", "Classroom", "/dashboard"])

    else:
        # Background Box and styling
        with me.box(style=me.Style(background="content-box radial-gradient(#0B0C10, #1F2833)",
                                   padding=me.Padding.all(0),
                                   height=me.viewport_size().height,
                                   width=me.viewport_size().width,
                                   display="flex",
                                   justify_content="center",
                                   align_items="center",
                                   )
                    ):
            # Signup box and styling
            with me.box(
                    style=me.Style(
                        background="black",
                        height=500,
                        width=400,
                        margin=me.Margin.symmetric(vertical=20, horizontal=450),
                        border=me.Border.symmetric(
                            horizontal=me.BorderSide(width=1, color="white", style="solid"),
                            vertical=me.BorderSide(width=1, color="white", style="solid"),
                        ),
                        border_radius=20,
                    )
            ):
                # username box
                with me.box(
                        style=me.Style(
                            # margin=me.Margin.symmetric(vertical=20, horizontal=100),
                            display="flex",
                            justify_content="center",
                            width=400,
                            height=100,
                            border_radius=30
                        ),
                ):
                    me.icon("person", style=me.Style(margin=me.Margin.symmetric(vertical=50),
                                                     color="white",
                                                     display="flex",

                                                     ))
                    me.input(label="Username", type="text", color="primary", required=True,
                             style=me.Style(
                                            font_family="Jetbrains Mono",
                                            # font_style="italic",
                                            width=250,
                                            margin=me.Margin.symmetric(vertical=40, horizontal=30)
                                            ), on_blur=on_blur_name
                             )
                #  mail box
                with me.box(
                        style=me.Style(
                            # margin=me.Margin.symmetric(vertical=20, horizontal=100),
                            display="flex",
                            justify_content="center",
                            width=400,
                            height=100,
                            border_radius=30
                        ),
                ):
                    me.icon("mail", style=me.Style(margin=me.Margin.symmetric(vertical=50),
                                                   color="white",
                                                   display="flex",

                                                   ))
                    me.input(label="Email Id", float_label="auto", type="email", color="primary", required=True,
                             style=me.Style(margin=me.Margin.symmetric(vertical=40, horizontal=30),
                                            font_family="Jetbrains Mono",
                                            width=250, ), on_blur=on_blur_email
                             )
                # password box
                with me.box(
                        style=me.Style(
                            display="flex",
                            justify_content="center",
                            width=400,
                            height=100,
                            border_radius=30
                        ),
                ):
                    me.icon("lock", style=me.Style(margin=me.Margin.symmetric(vertical=50),
                                                   color="white",
                                                   display="flex",
                                                   ))
                    me.input(label="Password", type="password", color="primary", required=True,
                             style=me.Style(margin=me.Margin.symmetric(vertical=40, horizontal=30),
                                            font_family="Jetbrains Mono",
                                            width=250, ), on_blur=on_blur_password
                             )

                # TO-DO : Add a password confirmation box
                # TO-DO : Add verification check for non-empty fields

                # Signup and Login buttons
                with me.box(style=me.Style(margin=me.Margin.symmetric(vertical=20, horizontal=140),
                                           display="flex",
                                           justify_content="center",
                                           align_items="center",
                                           # background="lightblue",
                                           flex_direction="column",
                                           gap=10,
                                           )
                            ):
                    me.button("Sign Up", type="raised", on_click=create_user)
                    me.button("Login", type="raised", on_click=lambda event: me.navigate("/login"))

