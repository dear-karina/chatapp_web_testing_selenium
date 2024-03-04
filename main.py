from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)


def login_successful(username, password):
    # Instantiate a browser driver (in this case, Chrome)
    try:
        # Maximize the window
        driver.maximize_window()

        # Navigate to the login page
        driver.get("https://chatapp.hongduccodedao.io.vn/login")

        # Find the username and password fields, and input credentials
        username_box = driver.find_element(By.ID, "username")
        username_box.send_keys(username)
        password_box = driver.find_element(By.ID, "password")
        password_box.send_keys(password)

        # Find the login button and click it
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

        try:
            # Wait for the logout button to be present
            logout_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/section/button"))
            )

            # Assert that the logout button is found
            assert logout_button is not None
            print(f"Login successful with username '{username}' and password '{password}'.")
            return True

        except AssertionError:
            print(
                f"Logout button not found after successful login with username '{username}' and password '{password}'. Test Failed.")
            return False

    finally:
        # Quit the browser
        driver.quit()


def login_fail(username, password):
    # Instantiate a browser driver (in this case, Chrome)
    try:
        # Maximize the window
        driver.maximize_window()

        # Navigate to the login page
        driver.get("https://chatapp.hongduccodedao.io.vn/login")

        # Find the username and password fields, and input credentials
        username_box = driver.find_element(By.ID, "username")
        username_box.send_keys(username)
        password_box = driver.find_element(By.ID, "password")
        password_box.send_keys(password)

        # Find the login button and click it
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

        try:
            # Wait for the logout button to be present (indicating successful login)
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/section/button"))
            )
            print(
                f"Unexpectedly found logout button after login failed with username '{username}' and password '{password}'. Test Failed.")
            return False

        except:
            print(f"Login failed as expected with username '{username}' and password '{password}'.")
            return True

    finally:
        # Quit the browser
        driver.quit()


if __name__ == "__main__":
    # Positive case: correct username and password
    login_successful("hongducdev", "123456")

    # Negative case: Incorrect password
    login_fail("hongducdev", "incorrectpassword")

    # Negative case: Username not existed
    login_fail("nonexistentusername", "123456")
