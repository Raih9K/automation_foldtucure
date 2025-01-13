from selenium.webdriver.common.by import By


class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.search_button = (By.NAME, "btnK")

    def search(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)
        self.driver.find_element(*self.search_button).click()
