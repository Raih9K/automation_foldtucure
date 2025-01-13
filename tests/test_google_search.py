import pytest
from pages.google_search_page import GoogleSearchPage
from data.search_data import search_data


@pytest.mark.search
def test_google_search(setup_browser):
    driver = setup_browser
    driver.get("https://www.google.com")
    google_page = GoogleSearchPage(driver)

    for query in search_data["google_search"]:
        google_page.search(query)
        # assert query.lower() in driver.page_source.lower()
        # driver.save_screenshot("screenshots/google_search_results.png")
