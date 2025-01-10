import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Or any other driver you prefer
    driver.maximize_window()
    yield driver
    driver.quit()
