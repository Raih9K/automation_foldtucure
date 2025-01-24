import pytest

@pytest.fixture(scope="session")
def browser():
    # Setup and teardown for the browser session
    driver = setup_browser()
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # driver = webdriver.Chrome(options=options)

    yield driver
    teardown_browser(driver)
