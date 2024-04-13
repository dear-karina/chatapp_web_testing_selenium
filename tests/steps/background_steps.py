from behave import given
from ultils.initialize_driver import initialize_driver


@given(u'I open the {browser} browser')
def open_page_in_browser(context, browser):
    try:
        if browser.lower() == 'chrome':
            context.driver = initialize_driver("chrome")
        assert context.driver, "Driver not initialized"
        context.is_ready = True
    except AssertionError:
        context.is_ready = False
