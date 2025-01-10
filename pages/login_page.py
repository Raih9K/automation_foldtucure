from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://admin.dev.myqbits.com/login")

    def enter_email(self, email):
        email_field = self.driver.find_element(
            By.CSS_SELECTOR, "[placeholder='Enter your email or phone number']")
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(
            By.CSS_SELECTOR, "[placeholder='Enter your password']")
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(
            By.CSS_SELECTOR, ".bg-blue-700")
        login_button.click()

    def is_logged_in(self):
        time.sleep(2)
        # Check if "Total Marketplace Orders" link is displayed after login
        page_data = self.driver.page_source  # Get the page source
        assert "Qbits Admin" in page_data, \
            "'Qbits Admin' not found. Login might have failed."

    def is_login_failed(self):
        time.sleep(2)
        # Check if "Log in" link is displayed in case of failed login
        page_data = self.driver.page_source  # Get the page source
        assert "Qbits Admin" in page_data, "'Qbits Admin' link not found. Login might have succeeded."
