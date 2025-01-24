from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):
        self.driver.get("https://admin.dev.myqbits.com/login")

    def enter_email(self, email):
        email_field = self.driver.find_element(
            By.CSS_SELECTOR, "[placeholder='Enter your email or phone number']"
        )
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(
            By.CSS_SELECTOR, "[placeholder='Enter your password']"
        )
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-700")
        login_button.click()

    def is_logged_in(self):
        try:
            # Check if the 'Customer' element is visible
            element = self.driver.find_element(By.XPATH, "//h4[.='Customer']")
            if element.is_displayed():
                print("Login successful. 'Customer' element found.")
                return True
            else:
                print("Login failed. 'Customer' element not visible.")
                return False
        except Exception as e:
            print(f"Error: {str(e)}. Login might have failed.")
            return False

    def is_login_failed(self):
        try:
            # Check if the 'Email or Phone' label is visible
            element = self.driver.find_element(By.XPATH, "//label[.='Email or Phone']")
            if element.is_displayed():
                print("Login failed. 'Email or Phone' label visible.")
                return True
            else:
                print("Login successful. 'Email or Phone' label not visible.")
                return False
        except Exception as e:
            print(f"Error: {str(e)}. Could not find 'Email or Phone' label.")
            return False
