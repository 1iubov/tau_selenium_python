# This module contains Page Object for Result page

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class DuckDuckGoResultPage:

    # Locators
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    """def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        # list of titles
        titles = [link.text for link in links]
        return titles
    """

    def result_link_titles(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(self.RESULT_LINKS)
        )
        links = self.browser.find_elements(*self.RESULT_LINKS)
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