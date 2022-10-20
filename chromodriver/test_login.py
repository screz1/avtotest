from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

EMAIL_FOR_REGISTRATION = 'chronicletest5@ukr.net'

URL = 'https://stage.xnl.zpoken.io/login'
PROD_URL = 'https://app.chronicle.io/login'


def test_log_in_valid_data():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_button__tiE3C']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
       By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    time.sleep(1)
    browser.quit()


def test_log_in_email_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("")

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']")))
    login_error = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']").text
    assert login_error == 'Email seems to be invalid, please check...'
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(1)


def test_log_in_email_not_registered():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest999@gmail.com")

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located((
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']")))
    login_error = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']").text
    assert login_error == 'Oops...We struggle to find anyone registered with this Email...Please check your data or sign up.'

    time.sleep(1)


def test_log_in_email_not_verified():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest120@gmail.com")

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginRightSide_formContainer__A5A7J']//h2[@class='LoginRightSide_h2__BFRs8']")))
    confirm_email = browser.find_element(
        By.XPATH, "//div[@class='LoginRightSide_formContainer__A5A7J']//h2[@class='LoginRightSide_h2__BFRs8']").text
    assert confirm_email == 'Confirm Email'
    text = browser.find_element(
        By.XPATH, "//div[@class='LoginRightSide_formContainer__A5A7J']//p[@class='VerifyEmail_desc__nqNEF']").text
    assert text == "We've sent you a letter to with confirmation details. Please go to your Email service and follow the instructions to activate your account."
    time.sleep(1)


def test_log_in_password_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("")
    input_chronicle_login.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    #sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Input_container__FISB2 Input_error__5HqQS']//div[@class='Input_tipError__CKiEf']")))
    password_error = browser.find_element(
        By.XPATH, "//div[@class='Input_container__FISB2 Input_error__5HqQS']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    time.sleep(2)


def test_log_in_password_field_invalid_data():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("213456qaZZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']")))
    password_error = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']").text
    assert password_error == 'Hmm... We remember you but the password seems to be wrong. Check your data or restore password.'
    time.sleep(2)


def test_log_in_password_field_low_register():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("213456qaz")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']")))
    password_error = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    time.sleep(2)


def test_log_in_password_field_high_register():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("213456QAZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']")))
    password_error = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    time.sleep(2)


def test_check_reset_password_proces_valid_data():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()
    time.sleep(1)
    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()

    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'msglist__row_href')))
    mail = browser.find_elements(By.CLASS_NAME, 'msglist__row_href')
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'xfmc10')))
    confirm_email = browser.find_element(By.CLASS_NAME, 'xfmc10')
    confirm_email.click()

    browser.switch_to.window(browser.window_handles[1])

    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    new_pass_input = browser.find_element(By.NAME, 'password')
    new_pass_input.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    submit_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    submit_button.click()
    time.sleep(2)
    try:
        pop_up_two_fa = browser.find_element(
           By.XPATH,
            "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
        if pop_up_two_fa.is_displayed():
            time.sleep(2)
            pop_up_two_fa.click()
            print("...")
    except NoSuchElementException:
        print("!!!")
    time.sleep(2)


def test_check_message_after_user_sent_email_reset_password_proces_valid_data():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()
    time.sleep(4)
    message = browser.find_element(By.CLASS_NAME, "RestoreAccessForm_info__xFNRF").text

    assert message == "Check your email : chronicletest5@ukr.net"


def test_check_reset_password_proces_invalid_email_user_not_found():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('test999@gmail.com')

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='RestoreAccessForm_tipError__k4ukD']")))
    error = browser.find_element(By.XPATH, "//div[@class='RestoreAccessForm_tipError__k4ukD']").text
    assert error == 'User not found'


def test_check_reset_password_proces_invalid_email_leave_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('')
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'Input_descContainer__D39tx')))
    browser.find_element(By.CLASS_NAME, 'Input_descContainer__D39tx').click()
    restore_pass_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    restore_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Please enter your email address'


def test_check_reset_password_proces_invalid_data_password_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()

    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'msglist__row_href')))
    mail = browser.find_elements(By.CLASS_NAME, 'msglist__row_href')
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'xfmc10')))
    confirm_email = browser.find_element(By.CLASS_NAME, 'xfmc10')
    confirm_email.click()

    browser.switch_to.window(browser.window_handles[1])

    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    new_pass_input = browser.find_element(By.NAME, 'password')
    new_pass_input.send_keys('')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']")))
    browser.find_element(By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']").click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    submit_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_only_digits():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()

    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'msglist__row_href')))
    mail = browser.find_elements(By.CLASS_NAME, 'msglist__row_href')
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'xfmc10')))
    confirm_email = browser.find_element(By.CLASS_NAME, 'xfmc10')
    confirm_email.click()

    browser.switch_to.window(browser.window_handles[1])

    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    new_pass_input = browser.find_element(By.NAME, 'password')
    new_pass_input.send_keys('213456789')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']")))
    browser.find_element(By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']").click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    submit_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_only_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()

    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'msglist__row_href')))
    mail = browser.find_elements(By.CLASS_NAME, 'msglist__row_href')
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'xfmc10')))
    confirm_email = browser.find_element(By.CLASS_NAME, 'xfmc10')
    confirm_email.click()

    browser.switch_to.window(browser.window_handles[1])

    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    new_pass_input = browser.find_element(By.NAME, 'password')
    new_pass_input.send_keys('QwErTyUiOpAsD')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']")))
    browser.find_element(By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']").click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    submit_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_low_register():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()

    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'msglist__row_href')))
    mail = browser.find_elements(By.CLASS_NAME, 'msglist__row_href')
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'xfmc10')))
    confirm_email = browser.find_element(By.CLASS_NAME, 'xfmc10')
    confirm_email.click()

    browser.switch_to.window(browser.window_handles[1])

    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    new_pass_input = browser.find_element(By.NAME, 'password')
    new_pass_input.send_keys('213456qaz')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']")))
    browser.find_element(By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']").click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    submit_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_high_register():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()

    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'msglist__row_href')))
    mail = browser.find_elements(By.CLASS_NAME, 'msglist__row_href')
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'xfmc10')))
    confirm_email = browser.find_element(By.CLASS_NAME, 'xfmc10')
    confirm_email.click()

    browser.switch_to.window(browser.window_handles[1])

    wait.until(ec.visibility_of_element_located((By.NAME, 'password')))
    new_pass_input = browser.find_element(By.NAME, 'password')
    new_pass_input.send_keys('213456QAZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']")))
    browser.find_element(By.XPATH, "//h2[@class='LoginRightSide_h2__BFRs8']").click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    submit_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
