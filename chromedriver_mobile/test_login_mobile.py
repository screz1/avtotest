import time

import pytest
from test_conf import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

EMAIL_FOR_REGISTRATION = 'chronicletest5@ukr.net'
URL = 'https://stage.xnl.zpoken.io/login'


def test_test_log_in_valid_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=412,915')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    login = wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    check_box = browser.find_element(By.XPATH, "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(1)


def test_log_in_email_field_empty():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=412,915')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    login = wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("")
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']")))
    login_error = browser.find_element(By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']").text
    assert login_error == 'Email seems to be invalid, please check...'
    input_chronicle_password.send_keys("213456qaZ")
    check_box = browser.find_element(By.XPATH, "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(1)


def test_log_in_email_not_registered():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=412,915')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)