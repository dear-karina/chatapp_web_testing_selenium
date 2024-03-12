from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, username, password):
    try:
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
