import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    """
    This fixture sets up the browser before each test and quits it after the test.
    """
    driver = webdriver.Chrome()  # Use the browser of your choice
    driver.maximize_window()
    yield driver  # Provides the driver instance to the test
    driver.quit()
