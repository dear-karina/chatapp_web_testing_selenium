from behave import given
from ultils.initialize_driver import initialize_driver


@given(u'I open the {browser} browser')
def open_page_in_browser(context, browser):
    if browser.lower() == 'chrome':
        context.driver = initialize_driver("chrome")
    elif browser.lower() == 'firefox':
        context.driver = initialize_driver("firefox")
    else:
        raise ValueError("Invalid browser specified")
