import mesop as me
from app import global_state

def error():
    if global_state.logged_status:
        me.text(global_state.error_message)
        me.button("Home", on_click=lambda event: me.navigate("/"))
    else:
        # me.text(global_state.error_message)


        #  UI for error page
        #  This page is displayed when an error occurs in the application
        with me.box(
                style=me.Style(
                    width="100%",
                    height="100%",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    flex_direction="row",
                    gap=20,
                    background="white",
                    # background="no-repeat center url(https://images.squarespace-cdn.com/content/58faa30ee6f2e151cda11af0/1552078400403-IVME47NBHX648T9IFHKK/3PP_24+Roadblocks.jpg?format=1500w&content-type=image%2Fjpeg)",
                    )
        ):


            me.image(src="https://images.squarespace-cdn.com/content/58faa30ee6f2e151cda11af0/1552078400403-IVME47NBHX648T9IFHKK/3PP_24+Roadblocks.jpg?format=1500w&content-type=image%2Fjpeg",
                     style=me.Style(
                            width=600,
                            height=600,
                            display="flex",
                            justify_self="center",
                            # position="absolute"
                     )
                     )
            with me.box(
                style=me.Style(
                    # background="rgba(0, 0, 0, 0.4)",
                    width=600,
                    height=200,
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    flex_direction="column",
                    border_radius=20,
                    gap=15,

                )
            ):
                me.markdown("###Oops! You are out of track. Let's get back you on track",
                            style=me.Style(color="#1A1A1A", font_size=15,font_family="monospace")
                            )
                me.button("Login", on_click=lambda event: me.navigate("/login"),
                          style=me.Style(background="radial-gradient(#0B0C10, #1F2833)", color="white",font_size=20,font_family="monospace"))


   
