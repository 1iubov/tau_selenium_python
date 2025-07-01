#THIS MODULE contains shared fixtures

import pytest
import selenium.webdriver

@pytest.fixture
def browser():

    #Initialize the ChromeDriver instance
    b = selenium.webdriver.Chrome()

    #Make its calls wait up to 10 seconds for elements to appear
    b.implicity_wait(10)

    #Return the webdriver instance for the setup
    yield b

    #Quit the webdriver instance for clean up
    b.quit()