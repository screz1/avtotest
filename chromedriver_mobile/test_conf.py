import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_options():
    options = Options()
    options.add_argument('chrome')
    options.add_argument('--window-size=412,915')
    return options


@pytest.fixture
def get_webdriver(get_options):
    options = get_options
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    return browser


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    browser = get_webdriver
    url = 'https://stage.xnl.zpoken.io/login'
    if request.cls is not None:
        request.cls.browser = browser
    browser.get(url)
    yield browser
    browser.close()

