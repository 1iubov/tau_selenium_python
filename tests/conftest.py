#THIS MODULE contains shared fixtures

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable - проверки, что значения в json норм
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

@pytest.fixture
def browser(config):

    #Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options = opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    #Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])
    #b.implicitly_wait(9.1)

    #Return the webdriver instance for the setup
    yield b

    #Quit the webdriver instance for clean up
    b.quit()