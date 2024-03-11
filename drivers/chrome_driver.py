from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def initialize_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("enable-automation")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")

    chrome_binary_path = r'/usr/local/bin/chrome-linux64/chrome'
    options.binary_location = chrome_binary_path
    driver_path = r'/usr/local/bin/chromedriver'
    service = Service(driver_path)
    cdriver = webdriver.Chrome(options=options, service=service)
    cdriver = webdriver.Chrome(options=options)
    return cdriver
