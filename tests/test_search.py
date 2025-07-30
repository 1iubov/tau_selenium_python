#Test cover DuckDuckGo home page is displayed
#These tests cover DuckDuckGo searches
import time

from selenium.webdriver.ie.webdriver import WebDriver

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest
import selenium.webdriver


@pytest.mark.parametrize('phrase', ['панда', 'питон', 'медведь'])
#@pytest.mark.parametrize('phrase', ['панда'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    # PHRASE = "панда"

    # Given the DuckDuckGo home page is displayed
    search_page.load()


    # When the user searches for "panda"
    search_page.search(phrase)


    #ищу ошибку
    browser.save_screenshot(f"screenshot_{phrase}.png")

    #time.sleep(5)
    # Then the search result title contains "panda"
    #assert PHRASE in result_page.title()

    # Then the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to the phrase
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result contains "panda"

    # (Putting this assertion last guarantees that the page title will be ready)
    assert phrase in result_page.title()

