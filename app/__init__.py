import mesop as me

@me.stateclass
class State:
    logged_status: bool = False  # Initialize the state variable
    user_id: str = ""
    user_name: str = ""  # Initialize the state variable
    user_email: str = ""  # Initialize the state variable
    user_role: str = ""
    enrolled_subjects: list[str]
    subjects: list[str]
    error_message: str = "Page Not Found"  # Initialize the state variable


global_state = State()
temp_state = State()