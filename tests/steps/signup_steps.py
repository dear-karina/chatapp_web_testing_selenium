from behave import given, when, then
from scripts.script_signup import SignupScript
from ultils.data_generator import DataGenerator


@given('I open the signup page')
def step_open_signup_page(context):
    context.signup_script = SignupScript(
        context.driver, "https://chatapppreview.hongduccodedao.io.vn/signup")


@when('I enter an unique fullname and an unique username and an unique password and retype it correctly')
def step_enter_valid_credentials(context):
    fullname = DataGenerator.generate_fullname()
    username = DataGenerator.generate_username()
    password = DataGenerator.generate_password(8)
    gender = DataGenerator.choose_random(("male", "female"))
    context.positive_data = (fullname, username, password, password, gender)
    context.signup_state = context.signup_script.signup_positive(fullname, username, password, password, gender)


@when('I enter an unique fullname and an unique username and an unique password and retype it incorrectly')
def step_enter_mismatching_password(context):
    fullname = DataGenerator.generate_fullname()
    username = DataGenerator.generate_username()
    password = DataGenerator.generate_password(8)
    gender = DataGenerator.choose_random(("male", "female"))
    context.negative_data = (fullname, username, password, "12345678", gender)
    context.signup_state = context.signup_script.signup_negative(fullname, username, password, "12345678", gender)


@when('I enter an unique fullname and an existed username and an unique password and retype it correctly')
def step_enter_existing_username(context):
    fullname = "hongducdev"
    username = DataGenerator.generate_username()
    password = DataGenerator.generate_password(8)
    gender = DataGenerator.choose_random(("male", "female"))
    context.negative_data = (fullname, username, password, password, gender)
    context.signup_state = context.signup_script.signup_negative(fullname, username, password, password, gender)


@then('I should be signed up successfully')
def step_verify_signup_success(context):
    assert context.signup_state[
               "is_signup_succeed"] is True, f"Signup was not successful. Input data: {context.positive_data}"


@then('I should not be signed up')
def step_verify_signup_failure(context):
    assert context.signup_state["is_signup_succeed"] is False, f"Signup was unexpectedly successful."


@then('I should see the signup message "{message}"')
def step_verify_error_message(context, message):
    actual_message = context.signup_state.get("error_message")
    logging_message = f"Expected error message: {message}. Actual error message: {actual_message}" if actual_message is not None else "No error message was found"
    logging_message += f"\nInput data: {context.negative_data}"
    assert actual_message == message, logging_message
