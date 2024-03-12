from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from ultils.take_screenshot import take_screenshot


def login(driver: WebDriver, username, password):
    try:
        username_box = driver.find_element(By.ID, "username")
        assert username_box is not None
        username_box.send_keys(username)
        password_box = driver.find_element(By.ID, "password")
        assert password_box is not None
        password_box.send_keys(password)
        login_button = driver.find_element(
            By.XPATH, "//button[text()='Login']")

        login_button.click()
        assert login_button is not None
        logout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='root']/div[1]/div/section/button"))
        )

        assert logout_button is not None
        print(
            f"Login successful with username '{username}' and password '{password}'.")
        # take_screenshot(
        #     driver, "tests/login/sceenshots/login_successfully.png")
        return True

    except Exception as e:
        print(f"Error: {e.msg if hasattr(e, 'msg') else e}")
        print(
            f"Login failed with username '{username}' and password '{password}'.")
        return False
    finally:
        driver.quit()
