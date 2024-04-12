from behave import given
from ultils.initialize_driver import initialize_driver
from commons.page_urls import PAGE_URLS
from scripts.script_open_page import open_page
from scripts.script_login import LoginScript


@given(u'I open the {page} Page')
def open_page(context, page):
    try:
        context.driver = initialize_driver("chrome")
        assert context.driver, "WebDriver is not initialized"
        url = PAGE_URLS[page]
        context.driver = open_page(context.driver, url)
        assert context.driver.current_url == url, f"Not on the right page: {context.driver.current_url}"
    except AssertionError as e:
        context.state = {
            "is_ready": False,
            "error": str(e),
            "message": None
        }
    else:
        context.state = {
            "is_ready": True,
            "error": None,
            "message": None,
        }
        if page == "Log In":
            context.script = LoginScript(context.driver)
