def open_url(driver, url: str):
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    driver.implicitly_wait(10)
    driver.get(url)

    assert driver, "WebDriver is not initialized"
    assert driver.current_url == url, f"Not on the right page: {url}"

    return driver
