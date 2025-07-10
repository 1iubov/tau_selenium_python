# This module contains Page Object for Result page

from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        #TODO
        #list of titles
        return[]

    def search_input_value(self):
        #TODO
        #value string
        return ""

    def title(self):
        #TODO
        #value string
        return ""