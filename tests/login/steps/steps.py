# Step definitions for login.feature
from behave import given, when, then
from scripts.script_login import login
from scripts.script_open_url import open_url


@given('I open the login page')
def step_open_login_page(context):
    context.driver = open_url(
        context.driver, "https://chatapp.hongduccodedao.io.vn/login")


@when('I enter the correct username "{username}" and password "{password}"')
def step_enter_correct_credentials(context, username, password):
    logged_in = login(context.driver, username, password)
    context.logged_in = logged_in  # Store login status for later steps


@when('I enter the correct username "{username}" and incorrect password "{password}"')
def step_enter_incorrect_password(context, username, password):
    logged_in = login(context.driver, username, password)
    context.logged_in = logged_in  # Store login status for later steps


@when('I enter a nonexistent username "{username}" and password "{password}"')
def step_enter_nonexistent_username(context, username, password):
    logged_in = login(context.driver, username, password)
    context.logged_in = logged_in  # Store login status for later steps


@then('I should be logged in successfully')
def step_verify_login(context):
    assert context.logged_in, "Login was not successful"


@then('I should not be logged in')
def step_verify_not_logged_in(context):
    assert not context.logged_in, "Expected to see an error message, but logged in successfully"
