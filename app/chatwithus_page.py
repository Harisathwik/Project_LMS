import random
import time

import mesop as me
import mesop.labs as mel
from app import global_state
from components.side_navigation_bar import side_navigation


LINES = [
    "Mesop is a Python-based UI framework designed to simplify web UI development for engineers without frontend experience.",
    "It leverages the power of the Angular web framework and Angular Material components, allowing rapid construction of web demos and internal tools.",
    "With Mesop, developers can enjoy a fast build-edit-refresh loop thanks to its hot reload feature, making UI tweaks and component integration seamless.",
    "Deployment is straightforward, utilizing standard HTTP technologies.",
    "Mesop's component library aims for comprehensive Angular Material component coverage, enhancing UI flexibility and composability.",
    "It supports custom components for specific use cases, ensuring developers can extend its capabilities to fit their unique requirements.",
    "Mesop's roadmap includes expanding its component library and simplifying the onboarding processs.",
  ]


def transform(input: str, history: list[mel.ChatMessage]):
    for line in random.sample(LINES, random.randint(3, len(LINES) - 1)):
        time.sleep(0.3)
        yield line + " "


def chat_with_us():
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
                me.markdown("Login to chat with us", style=me.Style(color="white", font_size=15))
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
        side_navigation()
        mel.chat(transform, title="Mesop Demo Chat", bot_user="Mesop Bot")
