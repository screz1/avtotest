from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

EMAIL_FOR_REGISTRATION = 'chronicletest5'
URL_DEV = 'https://dev.xnl.zpoken.io/sign_up'
URL_STAGE = 'https://stage.xnl.zpoken.io/sign_up'
URL = 'https://stage.xnl.zpoken.io/sign_up'


def test_sign_up_valid_data():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION+'@ukr.net')

    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    password_input = browser.find_element(By.NAME, 'password')
    password_input.send_keys('213456qaZ')

    wait.until(ec.visibility_of_element_located((By.NAME, 'checkbox')))
    check_box = browser.find_element(By.NAME, 'checkbox')
    check_box.click()

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    next_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    next_button.click()

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginRightSide_formContainer__A5A7J']//h2[@class='LoginRightSide_h2__BFRs8']")))

    confirm_email = browser.find_element(
       By.XPATH, "//div[@class='LoginRightSide_formContainer__A5A7J']//h2[@class='LoginRightSide_h2__BFRs8']").text
    assert confirm_email == 'Confirm Email'
    text = browser.find_element(
       By.XPATH, "//div[@class='LoginRightSide_formContainer__A5A7J']//p[@class='VerifyEmail_desc__nqNEF']").text
    assert text == "We've sent you a letter with confirmation details. Please go to your Email service and follow the instructions to activate your account."
    time.sleep(2)


def test_email_verification():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys(EMAIL_FOR_REGISTRATION+'@ukr.net')

    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")))

    mail = browser.find_elements(By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()

    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'xfmc10')))
    confirm_email = browser.find_element(By.CLASS_NAME, 'xfmc10')
    confirm_email.click()
    time.sleep(2)

    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)


def test_sign_up_invalid_data_email_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('')
    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    password_input = browser.find_element(By.NAME, 'password')
    password_input.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.NAME, 'checkbox')))
    check_box = browser.find_element(By.NAME, 'checkbox')
    check_box.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']")))
    email_error = browser.find_element(
        By.XPATH, "//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']").text
    assert email_error == 'Email seems to be invalid, please check...'

    next_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    #next_button.click()


def test_sign_up_invalid_data_password_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('chronicletest210@gmail.com')
    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    password_input = browser.find_element(By.NAME, 'password')
    password_input.send_keys('')
    wait.until(ec.visibility_of_element_located((By.NAME, 'checkbox')))
    check_box = browser.find_element(By.NAME, 'checkbox')
    check_box.click()
    wait.until(ec.visibility_of_element_located((
        By.XPATH, "//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']")))
    password_error = browser.find_element(
        By.XPATH, "//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    next_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    #next_button.click()
    time.sleep(1)


def test_sign_up_invalid_data_password_not_correct_7_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('chronicletest210@gmail.com')
    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    password_input = browser.find_element(By.NAME, 'password')
    password_input.send_keys('2134qaZ')
    wait.until(ec.visibility_of_element_located((By.NAME, 'checkbox')))
    check_box = browser.find_element(By.NAME, 'checkbox')
    check_box.click()
    password_error = browser.find_element(
        By.XPATH, "//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    next_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    # next_button.click()
    time.sleep(1)


def test_sign_up_invalid_data_password_not_correct_all_symbols_in_low_register():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('chronicletest210@gmail.com')
    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    password_input = browser.find_element(By.NAME, 'password')
    password_input.send_keys('213456qaz')
    wait.until(ec.visibility_of_element_located((By.NAME, 'checkbox')))
    check_box = browser.find_element(By.NAME, 'checkbox')
    check_box.click()
    password_error = browser.find_element(
        By.XPATH, "//div[@class='RegistrationForm_input___OhVe']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    next_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    # next_button.click()
    time.sleep(1)


def test_sign_up_invalid_data_already_registered_email():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('chronicletest102@gmail.com')
    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    password_input = browser.find_element(By.NAME, 'password')
    password_input.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.NAME, 'checkbox')))
    check_box = browser.find_element(By.NAME, 'checkbox')
    check_box.click()
    wait.until(ec.visibility_of_element_located((
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    next_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    next_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='RegistrationForm_tipError__LxCu7']")))
    email_error = browser.find_element(By.XPATH, "//div[@class='RegistrationForm_tipError__LxCu7']").text
    assert email_error == 'Oops, this email seems to be already taken...'
    time.sleep(1)
    browser.close()


