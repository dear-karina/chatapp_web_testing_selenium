from behave import given
from ultils.initialize_driver import initialize_driver


@given(u'I open the {browser} browser')
def open_browser(context, browser):
    try:
        if browser.lower() == 'chrome':
            context.driver = initialize_driver("chrome")
        assert context.driver, "WebDriver is not initialized"
    except AssertionError as e:
        context.is_ready = False
    else:
        context.is_ready = True
