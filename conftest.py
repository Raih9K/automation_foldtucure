# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup_browser():
    """Fixture to set up and tear down the browser."""
    # Initialize Chrome WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    # Yield the driver instance for tests
    yield driver

    # Quit the driver after the test
    driver.quit()
