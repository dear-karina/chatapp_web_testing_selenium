from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    driver = webdriver.Chrome()

    url = "https://chatapppreview.hongduccodedao.io.vn/login"

    driver.get(url)

    # Get the title of the webpage
    title = driver.title
    print("Title of the webpage:", title)
    username_box = driver.find_element(By.ID, "username")
    username_box.send_keys("hongducdev")
    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys("1234")
    login_button = driver.find_element(
        By.XPATH, "//button[text()='Login']")

    login_button.click()
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[role='status']"))
    )
    print(element.text)
    driver.quit()
