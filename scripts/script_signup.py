import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from ultils.take_screenshot import take_screenshot


class SignupScript:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get(self.url)

    def signup_positive(self, fullname, username, password, password_retype, gender: str):
        try:
            fullname_box = self.wait.until(EC.presence_of_element_located((By.ID, "fullName")))
            fullname_box.send_keys(fullname)

            username_box = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_box.send_keys(username)

            password_box = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_box.send_keys(password)

            confirm_password_box = self.wait.until(EC.presence_of_element_located((By.ID, "confirmPassword")))
            confirm_password_box.send_keys(password_retype)

            male_radio_box = self.wait.until(EC.presence_of_element_located((By.ID, "male")))
            female_radio_box = self.wait.until(EC.presence_of_element_located((By.ID, "female")))
            if gender.lower() == "male":
                male_radio_box.click()
            elif gender.lower() == "female":
                female_radio_box.click()

            signup_button = self.wait.until(EC.element_to_be_clickable((By.ID, "signup")))
            signup_button.click()

            self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/section/button")))
            return {"is_signup_succeed": True}
        except TimeoutException:
            self.logger.error("Timeout occurred while waiting for element")
            return {"is_signup_succeed": False, "error_message": "Timeout occurred"}
        except NoSuchElementException as e:
            self.logger.error(f"Element not found: {e}")
            return {"is_signup_succeed": False, "error_message": "Element not found"}

    def signup_negative(self, fullname, username, password, password_retype, gender: str):
        try:
            fullname_box = self.wait.until(EC.presence_of_element_located((By.ID, "fullName")))
            fullname_box.send_keys(fullname)

            username_box = self.wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_box.send_keys(username)

            password_box = self.wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_box.send_keys(password)

            confirm_password_box = self.wait.until(EC.presence_of_element_located((By.ID, "confirmPassword")))
            confirm_password_box.send_keys(password_retype)

            male_radio_box = self.wait.until(EC.presence_of_element_located((By.ID, "male")))
            female_radio_box = self.wait.until(EC.presence_of_element_located((By.ID, "female")))
            if gender.lower() == "male":
                male_radio_box.click()
            elif gender.lower() == "female":
                female_radio_box.click()

            signup_button = self.wait.until(EC.element_to_be_clickable((By.ID, "signup")))
            signup_button.click()

            status_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='status']")))
            error_message = status_element.text
            return {"is_signup_succeed": False, "error_message": error_message}
        except TimeoutException:
            self.logger.error("Timeout occurred while waiting for element")
            return {"is_signup_succeed": False, "error_message": "Timeout occurred"}
        except NoSuchElementException as e:
            self.logger.error(f"Element not found: {e}")
            return {"is_signup_succeed": False, "error_message": "Element not found"}
