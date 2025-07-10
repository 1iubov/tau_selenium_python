#This Module contains the Page Object for search page

from selenium.webdriver.common.by import By

class DuckDuckGoSearchPage:

    SEARCH_INPUT = (By.ID, 'searchbox_input')

    def __init__(self, browser):
        #instance variable initialization
        self.browser = browser

    def load(self):
        #TODO
        pass
    def search(self, phase):
        #TODO
        pass