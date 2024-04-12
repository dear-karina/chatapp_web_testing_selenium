from behave import when, then


@then('All of the UI elements should align with the Login Page design')
def step_verify_ui(context):
    if context.state["is_ready"]:
        error_message = context.script.verify_ui()
        if error_message is not None:
            context.state = {
                "is_ready": False,
                "error": error_message,
                "message": None,
            }
    else:
        print(context.state["error"])
        return


@when('I enter the username {username} (already registered)')
def step_enter_already_registered_username(context, username):
    if context.state["is_ready"]:
        context.script.enter_username(username)
    else:
        return


@when('I enter the password {password} (matched)')
def step_enter_matched_password(context, password):
    if context.state["is_ready"]:
        context.script.enter_password(password)
    else:
        return


@then('I should be logged in successfully')
def step_verify_login_successfully(context):
    if context.state["is_ready"]:
        error_message = context.script.verify_login_successfully()
        if error_message is not None:
            context.state = {
                "is_ready": False,
                "error": error_message,
                "message": None,
            }
    else:
        return
