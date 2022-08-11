import time

import pytest
from test_conf import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys

EMAIL_FOR_REGISTRATION = 'chronicletest5@ukr.net'
URL = 'https://stage.xnl.zpoken.io/login'


def test_edit_display_name_valid_data():
    WIDTH = 412
    HEIGHT = 915
    PIXEL_RATIO = 3.0
    UA = 'Mozilla/5.0 (Linux; Android 9; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
    mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}

    options = webdriver.ChromeOptions()

    options.add_experimental_option('mobileEmulation', mobileEmulation)

    # options.add_argument('--window-size=412,915')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    check_box = browser.find_element(By.XPATH,
                                     "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(By.XPATH,
                                         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Mobile_hamburgerWrap__hd83L']")))
    menu = browser.find_element(By.XPATH, "//div[@class='Mobile_hamburgerWrap__hd83L']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Mobile_link__IN15P']")))
    setting = browser.find_elements(By.XPATH, "//div[@class='Mobile_link__IN15P']")
    personal_settings = setting[4].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")))
    edit_dis_name = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']").click()
