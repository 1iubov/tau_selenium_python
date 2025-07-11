# This module contains Page Object for Result page

from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    # Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        # list of titles
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        # value string
        value = search_input.get_attribute('value')
        return value

    def title(self):
        # value string
        return self.browser.title