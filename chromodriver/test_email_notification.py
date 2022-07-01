from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
import pickle
from test_z_users_create_cookie import *

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://dev.xnl.zpoken.io/store'


def test_clean_onfido_before():
    browser = webdriver.Chrome()
    browser.get('https://dev-admin.xnl.zpoken.io/')
    time.sleep(5)
    admin_login = browser.find_element_by_id('login').send_keys('savchukura888@gmail.com')
    time.sleep(1)
    admin_password = browser.find_element_by_id('password').send_keys('213456qaZ')
    time.sleep(1)
    sign_in_button = browser.find_element_by_xpath(
        "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")
    sign_in_button.click()
    time.sleep(3)
    browser.find_element_by_xpath("//*[text() = 'Users Information']").click()
    time.sleep(3)
    search = browser.find_element_by_id('search')
    search.send_keys('chronicletest5')
    search.send_keys(Keys.RETURN)
    time.sleep(18)
    opt_button = browser.find_element_by_xpath("//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    time.sleep(3)
    drop_user = browser.find_elements_by_xpath("//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[4].click()
    time.sleep(2)
    confirm = browser.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'
    time.sleep(2)

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys('chronicletest5@ukr.net')
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_xpath("//tr[@class='msglist__row unread icon0  ui-draggable']")
    mail[0].click()
    time.sleep(2)
    message = browser.find_element_by_xpath("//h3[@class='readmsg__subject']").text
    assert message == 'KYC rejected'
    browser.close()


def test_email_notif_kyc_approwed():
    browser = webdriver.Chrome()
    browser.get('https://dev-admin.xnl.zpoken.io/')
    time.sleep(5)
    admin_login = browser.find_element_by_id('login').send_keys('savchukura888@gmail.com')
    time.sleep(1)
    admin_password = browser.find_element_by_id('password').send_keys('213456qaZ')
    time.sleep(1)
    sign_in_button = browser.find_element_by_xpath(
        "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")
    sign_in_button.click()
    time.sleep(3)
    browser.find_element_by_xpath("//*[text() = 'Users Information']").click()
    time.sleep(3)
    search = browser.find_element_by_id('search')
    search.send_keys('chronicletest5')
    search.send_keys(Keys.RETURN)
    time.sleep(18)
    opt_button = browser.find_element_by_xpath("//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    time.sleep(3)
    drop_user = browser.find_elements_by_xpath("//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[4].click()
    time.sleep(2)
    confirm = browser.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'
    time.sleep(2)

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys('chronicletest5@ukr.net')
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_xpath("//tr[@class='msglist__row unread icon0  ui-draggable']")
    mail[0].click()
    time.sleep(2)
    message = browser.find_element_by_xpath("//h3[@class='readmsg__subject']").text
    assert message == 'KYC rejected'
    browser.close()