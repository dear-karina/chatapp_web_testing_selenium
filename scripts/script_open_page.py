from selenium.webdriver.chrome.webdriver import WebDriver


def open_page(driver: WebDriver, url: str):
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(10)
    driver.get(url)
    return driver
