from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
import random
from driver import driver

EMAIL_FOR_REGISTRATION = 'chronicletest5'
URL_DEV = 'https://dev.xnl.zpoken.io/sign_up'
URL_STAGE = 'https://stage.xnl.zpoken.io/sign_up'
URL = 'https://stage.xnl.zpoken.io/sign_up'


def test_sign_up_valid_data():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)

    time.sleep(1)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION+'@ukr.net')
    time.sleep(1)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys('213456qaZ')
    time.sleep(1)
    check_box = browser.find_element_by_name('checkbox').click()
    time.sleep(1)
    next_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    next_button.click()
    time.sleep(5)
    confirm_email = browser.find_element_by_xpath(
        "//div[@class='LoginRightSide_formContainer__A5A7J']//h2[@class='LoginRightSide_h2__BFRs8']").text
    assert confirm_email == 'Confirm Email'
    text = browser.find_element_by_xpath(
        "//div[@class='LoginRightSide_formContainer__A5A7J']//p[@class='VerifyEmail_desc__nqNEF']").text
    assert text == "We've sent you a letter with confirmation details. Please go to your Email service and follow the instructions to activate your account."
    time.sleep(2)


def test_email_verification():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION+'@ukr.net')

    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)

    mail = browser.find_elements_by_xpath("//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    time.sleep(2)

    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)

    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)


def test_sign_up_invalid_data_email_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)

    time.sleep(1)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys('')
    time.sleep(1)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys('213456qaZ')
    time.sleep(1)
    check_box = browser.find_element_by_name('checkbox').click()
    time.sleep(1)
    email_error = browser.find_element_by_xpath("//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']").text
    assert email_error == 'Email seems to be invalid, please check...'
    #password_error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']")
    next_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    #next_button.click()
    time.sleep(5)


def test_sign_up_invalid_data_password_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)

    time.sleep(1)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys('chronicletest210@gmail.com')
    time.sleep(1)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys('')
    time.sleep(1)
    check_box = browser.find_element_by_name('checkbox').click()
    time.sleep(1)
    password_error = browser.find_element_by_xpath("//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    next_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    #next_button.click()
    time.sleep(5)


def test_sign_up_invalid_data_password_not_correct_7_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)

    time.sleep(1)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys('chronicletest210@gmail.com')
    time.sleep(1)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys('2134qaZ')
    time.sleep(1)
    check_box = browser.find_element_by_name('checkbox').click()
    time.sleep(1)
    password_error = browser.find_element_by_xpath("//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    next_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    #next_button.click()
    time.sleep(5)


def test_sign_up_invalid_data_password_not_correct_all_symbols_in_low_register():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)

    time.sleep(1)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys('chronicletest210@gmail.com')
    time.sleep(1)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys('213456qaz')
    time.sleep(1)
    check_box = browser.find_element_by_name('checkbox').click()
    time.sleep(1)
    password_error = browser.find_element_by_xpath("//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    next_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    #next_button.click()
    time.sleep(5)


def test_sign_up_invalid_data_already_registered_email():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)

    time.sleep(1)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys('chronicletest102@gmail.com')
    time.sleep(1)
    password_input = browser.find_element_by_name('password')
    password_input.send_keys('213456qaZ')
    time.sleep(1)
    check_box = browser.find_element_by_name('checkbox').click()
    time.sleep(1)
    next_button = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(1)
    email_error = browser.find_element_by_xpath("//div[@class='RegistrationForm_tipError__LxCu7']").text
    assert email_error == 'Oops, this email seems to be already taken...'
    time.sleep(5)
    browser.close()


