import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from drivers.chrome_driver import initialize_driver as initialize_chrome_driver


class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = initialize_chrome_driver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_correct_credentials(self):
        self.assertTrue(login(self.driver, "hongducdev", "123456"))

    def test_incorrect_password(self):
        self.assertFalse(login(self.driver, "hongducdev", "incorrectpassword"))

    def test_nonexistent_username(self):
        self.assertFalse(login(self.driver, "nonexistentusername", "123456"))


def login(driver, username, password):
    try:
        driver.maximize_window()
        driver.set_page_load_timeout(60)  # Set page load timeout to 60 seconds
        driver.implicitly_wait(10)  # Set implicit wait to 10 seconds
        driver.get("https://chatapp.hongduccodedao.io.vn/login")
        username_box = driver.find_element(By.ID, "username")
        username_box.send_keys(username)
        password_box = driver.find_element(By.ID, "password")
        password_box.send_keys(password)
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

        logout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/section/button"))
        )

        assert logout_button is not None
        print(f"Login successful with username '{username}' and password '{password}'.")
        return True

    except Exception as e:
        print(f"Error: {e.msg if hasattr(e, 'msg') else e}")
        print(f"Login failed with username '{username}' and password '{password}'.")
        return False


if __name__ == "__main__":
    unittest.main()
