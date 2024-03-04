from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("enable-automation")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.binary_location = '/usr/bin/google-chrome'

    # Add the additional option for timeout
    desired_timeout = 60  # Set to 60 seconds for example, you can adjust as needed
    chrome_options.add_argument(f"--timeout={desired_timeout * 1000}")

    return webdriver.Chrome(options=chrome_options)

def login(driver, username, password):
    try:
        driver.maximize_window()
        driver.get("https://chatapp.hongduccodedao.io.vn/login")
        username_box = driver.find_element(By.ID, "username")
        username_box.send_keys(username)
        password_box = driver.find_element(By.ID, "password")
        password_box.send_keys(password)
        login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
        login_button.click()

        logout_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div/section/button"))
        )

        assert logout_button is not None
        print(f"Login successful with username '{username}' and password '{password}'.")
        return True

    except Exception as e:
        print(f"Error: {e}")
        print(f"Login failed with username '{username}' and password '{password}'.")
        return False

    finally:
        driver.quit()

if __name__ == "__main__":
    driver = initialize_driver()

    # Positive case: correct username and password
    login(driver, "hongducdev", "123456")

    # Negative case: Incorrect password
    login(driver, "hongducdev", "incorrectpassword")

    # Negative case: Username not existed
    login(driver, "nonexistentusername", "123456")
