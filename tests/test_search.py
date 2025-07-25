#Test cover DuckDuckGo home page is displayed
#These tests cover DuckDuckGo searches
import time

from selenium.webdriver.ie.webdriver import WebDriver

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest
import selenium.webdriver



def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "панда"

    # Given the DuckDuckGo home page is displayed
    search_page.load()


    # When the user searches for "panda"
    search_page.search(PHRASE)

    #time.sleep(5)
    # Then the search result title contains "panda"
    #assert PHRASE in result_page.title()

    # Then the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result contains "panda"

    # (Putting this assertion last guarantees that the page title will be ready)
    assert PHRASE in result_page.title()

