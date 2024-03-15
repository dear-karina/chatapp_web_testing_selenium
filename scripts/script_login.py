import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ultils.take_screenshot import take_screenshot


class LoginScript:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get(self.url)

    def login_positive(self, username, password):
        try:
            username_box = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_box.send_keys(username)

            password_box = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_box.send_keys(password)

            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
            login_button.click()

            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/section/button")))
            return {"is_login_succeed": True}
        except TimeoutException:
            self.logger.error("Timeout occurred while waiting for element")
            return {"is_login_succeed": False, "error_message": "Timeout occurred"}
        except NoSuchElementException as e:
            self.logger.error(f"Element not found: {e}")
            return {"is_login_succeed": False, "error_message": "Element not found"}

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

    def take_screenshot(self, filename):
        take_screenshot(self.driver, filename)
