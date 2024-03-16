from behave import given, when, then
from scripts.script_login import LoginScript


@given('I open the login page')
def step_open_login_page(context):
    context.login_page = LoginScript(context.driver, "https://chatapppreview.hongduccodedao.io.vn/login")


@when('I enter the correct username "{username}" and password "{password}"')
def step_enter_correct_credentials(context, username, password):
    context.logged_in_state = context.login_page.login_positive(username, password)


@when('I enter the correct username "{username}" and incorrect password "{password}"')
def step_enter_incorrect_password(context, username, password):
    context.logged_in_state = context.login_page.login_negative(username, password)


@when('I enter a nonexistent username "{username}" and password "{password}"')
def step_enter_nonexistent_username(context, username, password):
    context.logged_in_state = context.login_page.login_negative(username, password)


@then('I should be logged in successfully')
def step_verify_login(context):
    assert context.logged_in_state["is_login_succeed"], "Login was not successful"


@then('I should not be logged in')
def step_verify_not_logged_in(context):
    assert not context.logged_in_state["is_login_succeed"], "Login was unexpectedly successful"


@then('I should see the message "{error_message}"')
def step_verify_error_message(context, error_message):
    actual_message = context.logged_in_state.get("error_message")
    logging_message = f"Expected error message: {error_message}. Actual error message: {actual_message}" if actual_message is not None else "No error message was found"
    assert actual_message == error_message, logging_message
