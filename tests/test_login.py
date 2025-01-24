import pytest
import time
from pages.login_page import LoginPage
from utils.browser_utils import setup_browser, teardown_browser
from data.test_data import LOGIN_TEST_DATA  # Import test data


class TestLogin:
    def setup_method(self):
        self.driver = setup_browser()
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        teardown_browser(self.driver)

    def test_login_valid_credentials(self):
        # Use valid data from test_data.py
        self.login_page.open_login_page()
        self.login_page.enter_email(LOGIN_TEST_DATA["valid_email"])
        self.login_page.enter_password(LOGIN_TEST_DATA["valid_password"])
        self.login_page.click_login_button()
        time.sleep(10)

        # Verify login success (e.g., checking for a logged-in element or page)
        assert self.login_page.is_logged_in()
        self.driver.save_screenshot("screenshots/valid_login_screenshot.png")

    def test_login_invalid_credentials(self):
        # Use invalid data from test_data.py
        self.login_page.open_login_page()
        self.login_page.enter_email(LOGIN_TEST_DATA["invalid_email"])
        self.login_page.enter_password(LOGIN_TEST_DATA["invalid_password"])
        self.login_page.click_login_button()
        time.sleep(10)

        # Verify login failure (e.g., checking for error message)
        # Assuming there's a method to check for failure
        assert self.login_page.is_login_failed()
        self.driver.save_screenshot("screenshots/invalid_login_screenshot.png")
