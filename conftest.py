import pytest

@pytest.fixture(scope="session")
def browser():
    # Setup and teardown for the browser session
    driver = setup_browser()
    yield driver
    teardown_browser(driver)
