import os
from selenium.webdriver.chrome.webdriver import WebDriver


def take_screenshot(driver: WebDriver, screenshot_path):
    driver.implicitly_wait(5)
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    driver.save_screenshot(screenshot_path)
