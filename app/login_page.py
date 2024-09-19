import mesop as me
from services.authentication import authenticate_user
from app import global_state
from services.views import on_blur_email, on_blur_password
from components.popupbox_page import popup_box

def login():
    if not global_state.logged_status:
        # Background Box and styling
        with me.box(style=me.Style(background="content-box radial-gradient(#0B0C10, #1F2833)",
                                   height=me.viewport_size().height,
                                   width=me.viewport_size().width,
                                   display="flex",
                                   justify_content="center",
                                   align_items="center",
                                   )
                    ):

            # Login box and styling
            with me.box(
                    style=me.Style(
                        background="black",
                        height=470,
                        width=400,
                        margin=me.Margin.symmetric(vertical=20, horizontal=450),
                        border=me.Border.symmetric(
                            horizontal=me.BorderSide(width=2, color="white", style="solid"),
                            vertical=me.BorderSide(width='0.2em', color="white", style="inset"),
                        ),
                        border_radius=20,
                    )
            ):
                # Email box
                with me.box(
                        style=me.Style(
                            display="flex",
                            justify_content="center",
                            width=400,
                            height=100,
                            border_radius=30,
                        ),
                ):
                    me.icon("mail",
                            style=me.Style(margin=me.Margin.symmetric(vertical=50), color="white", display="flex"))
                    me.input(
                        label="Email",
                        type="email",
                        color="primary",
                        required=True,
                        on_blur=on_blur_email,
                        style=me.Style(
                            # font_weight="bold",
                            font_family="system-ui",
                            width=250,
                            margin=me.Margin.symmetric(vertical=40, horizontal=30),
                        ),)

                # password box
                with me.box(
                        style=me.Style(
                            display="flex",
                            justify_content="center",
                            width=400,
                            height=100,
                            border_radius=30,
                        ),
                ):
                    me.icon("lock",
                            style=me.Style(margin=me.Margin.symmetric(vertical=50), color="white", display="flex"))
                    me.input(
                        label="Password",
                        type="password",
                        color="primary",
                        required=True,
                        on_blur=on_blur_password,
                        style=me.Style(
                            # font_weight="bold",
                            font_family="system-ui",
                            width=250,
                            margin=me.Margin.symmetric(vertical=30, horizontal=30),

                        ),
                    )
                # login button Sign up button
                with me.box(
                        style=me.Style(
                            display="flex",
                            justify_content="center",
                            width=400,
                            height=200,
                            gap=5,
                            # background="lightblue",
                            flex_direction="column",
                            justify_self="center",
                            align_items="center",
                            margin=me.Margin.symmetric(vertical=30),

                        ),
                ):
                    me.button(
                        "Login",
                        color="primary",
                        type="raised",
                        on_click=authenticate_user,
                    )
                    me.text(
                        "Don't have an account?",
                        style=me.Style(
                            margin=me.Margin.symmetric(vertical=35),
                            color="white",
                            font_family="system-ui",
                            justify_content="center",
                        ),
                    )

                    me.button(
                        "Signup",
                        color="primary",
                        type="raised",
                        on_click=lambda event: me.navigate("/signup"),
                    )

    else:
        popup_box(["You are already logged in.", "Home", "/", "Classroom", "/dashboard"])