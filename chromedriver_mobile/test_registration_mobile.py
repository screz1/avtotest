import time

import pytest
from test_conf import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains

EMAIL_FOR_REGISTRATION = 'chronicletest5@ukr.net'
URL = 'https://stage.xnl.zpoken.io/login'

WIDTH = 412
HEIGHT = 915
PIXEL_RATIO = 3.0


def test_sign_up_valid_data():
    #UA = 'Mozilla/5.0 (Linux; Android 9; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
    #mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}

    options = webdriver.ChromeOptions()

    #options.add_experimental_option('mobileEmulation', mobileEmulation)

    options.add_argument('--window-size=412,915')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'LoginRightSide_linkRegister__ui57S')))
    sign_up = browser.find_element(By.CLASS_NAME, 'LoginRightSide_linkRegister__ui57S').click()
    time.sleep(5)

    time.sleep(5)
