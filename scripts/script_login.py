import logging
from typing import Optional
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ultils.take_screenshot import take_screenshot


class LoginScript:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 5)
        self.login_button: Optional[WebElement] = None
        self.password_box: Optional[WebElement] = None
        self.username_box: Optional[WebElement] = None

    def verify_ui(self):
        try:
            self.username_box = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            self.password_box = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            self.login_button = self.wait.until(EC.element_to_be_clickable((By.ID, "login")))
            return None
        except TimeoutException:
            error_message = "Timeout occurred"
            if not self.username_box:
                error_message += " - Username box not found"
            if not self.password_box:
                error_message += " - Password box not found"
            if not self.login_button:
                error_message += " - Login button not found"
            return error_message

    def enter_username(self, username):
        self.username_box.send_keys(username)

    def enter_password(self, password):
        self.password_box.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def verify_login_successfully(self):
        try:
            self.wait.until(EC.url_contains("home"))
            return None
        except TimeoutException:
            return f"Timeout occurred - Not directed to Home Page, the current URL is {self.driver.current_url}"

    def login_negative(self, username, password):
        try:
            username_box = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_box.send_keys(username)

            password_box = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_box.send_keys(password)

            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
            login_button.click()

            status_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='status']")))
            error_message = status_element.text
            return {"is_login_succeed": False, "error_message": error_message}
        except TimeoutException:
            self.logger.error("Timeout occurred while waiting for element")
            return {"is_login_succeed": False, "error_message": "Timeout occurred"}
        except NoSuchElementException as e:
            self.logger.error(f"Element not found: {e}")
            return {"is_login_succeed": False, "error_message": "Element not found"}
        finally:
            self.driver.quit()
