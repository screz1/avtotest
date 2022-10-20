import time
from configurate import *
from pages.login_page import LoginPage
from urls.urls import *


class TestAnomaly:

    def test_log_in(self, browser):
        login_page = LoginPage(browser, URL)
        login_page.open()
