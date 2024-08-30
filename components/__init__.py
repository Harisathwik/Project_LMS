import mesop as me

@me.stateclass
class SideNavState:
    sidenav_open: bool

def on_sidenav_click(e: me.ClickEvent):
    s = me.state(SideNavState)
    s.sidenav_open = not s.sidenav_open
