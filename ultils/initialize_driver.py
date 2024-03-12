from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def initialize_driver(driver: str):
    if driver.lower() == "chrome":
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
    elif driver.lower() == "firefox":
        options = Options()
        options.headless = True  # Enable headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--enable-automation")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")

        # Set the path to the Firefox binary if necessary
        # firefox_binary_path = r'/path/to/firefox/binary'
        # options.binary_location = firefox_binary_path

        # Specify the path to the geckodriver executable
        driver_path = r'/usr/local/bin/geckodriver'

        # Create a service object for geckodriver
        service = Service(driver_path)

        # Initialize the Firefox driver with the specified options and service
        driver = webdriver.Firefox(options=options, service=service)

        return driver
    else:
        print("Unsupported driver")
        return None
