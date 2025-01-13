import pytest
from pages.youtube_search_page import YouTubeSearchPage
from data.search_data import search_data


@pytest.mark.search
def test_youtube_search(setup_browser):
    driver = setup_browser
    driver.get("https://www.youtube.com")
    youtube_page = YouTubeSearchPage(driver)

    for query in search_data["youtube_search"]:
        youtube_page.search(query)
        # assert query.lower() in driver.page_source.lower()
        # driver.save_screenshot("screenshots/youtube_search_results.png")
