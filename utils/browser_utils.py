from selenium import webdriver


def setup_browser():
    # driver = webdriver.Chrome()
    driver = webdriver.Edge()

    driver.maximize_window()
    return driver


def teardown_browser(driver):
    driver.quit()
