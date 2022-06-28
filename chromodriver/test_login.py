from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException

EMAIL_FOR_REGISTRATION = 'chronicletest5@ukr.net'

URL = 'https://stage.xnl.zpoken.io/login'
PROD_URL = 'https://app.chronicle.io/login'

def test_log_in_valid_data():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    time.sleep(1)
    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")

    pop_up_two_fa.click()
    time.sleep(1)


def test_log_in_email_field_empty():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("")

    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.click()
    login_error = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']").text
    assert login_error == 'Email seems to be invalid, please check...'
    input_chronicle_password.send_keys("213456qaZ")
    time.sleep(1)

    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(1)


def test_log_in_email_not_registered():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest999@gmail.com")

    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.click()

    input_chronicle_password.send_keys("213456qaZ")
    time.sleep(1)

    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(5)
    login_error = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']").text
    assert login_error == 'Oops...We struggle to find anyone registered with this Email...Please check your data or sign up.'
    time.sleep(1)


def test_log_in_email_not_verified():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest120@gmail.com")

    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.click()

    input_chronicle_password.send_keys("213456qaZ")
    time.sleep(1)

    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(5)
    confirm_email = browser.find_element_by_xpath("//div[@class='LoginRightSide_formContainer__A5A7J']//h2[@class='LoginRightSide_h2__BFRs8']").text
    assert confirm_email == 'Confirm Email'
    text = browser.find_element_by_xpath("//div[@class='LoginRightSide_formContainer__A5A7J']//p[@class='VerifyEmail_desc__nqNEF']").text
    assert text == "We've sent you a letter to with confirmation details. Please go to your Email service and follow the instructions to activate your account."
    time.sleep(1)


def test_log_in_password_field_empty():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")

    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("")
    time.sleep(1)

    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    password_error = browser.find_element_by_xpath("//div[@class='Input_container__FISB2 Input_error__5HqQS']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    time.sleep(2)


def test_log_in_password_field_invalid_data():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")

    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("213456qaZZ")
    time.sleep(1)

    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    password_error = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']").text
    assert password_error == 'Hmm... We remember you but the password seems to be wrong. Check your data or restore password.'
    time.sleep(2)


def test_log_in_password_field_low_register():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")

    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("213456qaz")
    time.sleep(1)

    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    check_box.click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    password_error = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    time.sleep(2)


def test_log_in_password_field_high_register():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")

    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.click()
    input_chronicle_password.send_keys("213456QAZ")
    time.sleep(1)

    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    check_box.click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    password_error = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']").text
    assert password_error == 'Password needs to be at least 8 characters long and must include a symbol and capital'
    time.sleep(2)


def test_check_reset_password_proces_valid_data():
    browser = webdriver.Chrome()
    browser.get(PROD_URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(3)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    time.sleep(1)
    restore_pass_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()
    time.sleep(1)
    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_class_name('msglist__row_href')
    mail[0].click()
    time.sleep(2)
    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(3)

    check_ukr = browser.find_element_by_name('whitelist').click()
    time.sleep(2)
    conf_zpok = browser.find_element_by_xpath("//form[@method='GET']//button[@type='submit']").click()
    time.sleep(2)
    new_pass_input = browser.find_element_by_name('password')
    new_pass_input.send_keys('213456qaZ')
    submit_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    submit_button.click()
    time.sleep(2)
    try:
        pop_up_two_fa = browser.find_element_by_xpath(
            "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
        if pop_up_two_fa.is_displayed():
            pop_up_two_fa.click()
            print("...")
    except NoSuchElementException:
        print("!!!")
    time.sleep(2)


def test_check_reset_password_proces_invalid_email_user_not_found():
    browser = webdriver.Chrome()
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys('test999@gmail.com')
    time.sleep(1)

    restore_pass_button = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='RestoreAccessForm_tipError__k4ukD']").text
    assert error == 'User not found'
    time.sleep(1)


def test_check_reset_password_proces_invalid_email_leave_field_empty():
    browser = webdriver.Chrome()
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys('')
    time.sleep(1)
    browser.find_element_by_class_name('Input_descContainer__D39tx').click()
    restore_pass_button = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    restore_pass_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Please enter your email address'
    time.sleep(1)


def test_check_reset_password_proces_invalid_data_password_field_empty():
    browser = webdriver.Chrome()
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    time.sleep(1)
    restore_pass_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_class_name('msglist__row_href')
    mail[0].click()
    time.sleep(2)
    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    new_pass_input = browser.find_element_by_name('password')
    new_pass_input.send_keys('')
    time.sleep(2)
    browser.find_element_by_xpath("//h2[@class='LoginRightSide_h2__BFRs8']").click()
    time.sleep(1)
    submit_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_7_symbols():
    browser = webdriver.Chrome()
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    time.sleep(1)
    restore_pass_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_class_name('msglist__row_href')
    mail[0].click()
    time.sleep(2)
    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    new_pass_input = browser.find_element_by_name('password')
    new_pass_input.send_keys('2134qaZ')
    time.sleep(2)
    browser.find_element_by_xpath("//h2[@class='LoginRightSide_h2__BFRs8']").click()
    time.sleep(1)
    submit_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_only_digits():
    browser = webdriver.Chrome()
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    time.sleep(1)
    restore_pass_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_class_name('msglist__row_href')
    mail[0].click()
    time.sleep(2)
    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    new_pass_input = browser.find_element_by_name('password')
    new_pass_input.send_keys('213456789')
    time.sleep(2)
    browser.find_element_by_xpath("//h2[@class='LoginRightSide_h2__BFRs8']").click()
    time.sleep(1)
    submit_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_only_symbols():
    browser = webdriver.Chrome()
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    time.sleep(1)
    restore_pass_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_class_name('msglist__row_href')
    mail[0].click()
    time.sleep(2)
    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    new_pass_input = browser.find_element_by_name('password')
    new_pass_input.send_keys('QwErTyUiOpAsD')
    time.sleep(2)
    browser.find_element_by_xpath("//h2[@class='LoginRightSide_h2__BFRs8']").click()
    time.sleep(1)
    submit_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_low_register():
    browser = webdriver.Chrome()
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    time.sleep(1)
    restore_pass_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_class_name('msglist__row_href')
    mail[0].click()
    time.sleep(2)
    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    new_pass_input = browser.find_element_by_name('password')
    new_pass_input.send_keys('213456qaz')
    time.sleep(2)
    browser.find_element_by_xpath("//h2[@class='LoginRightSide_h2__BFRs8']").click()
    time.sleep(1)
    submit_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'


def test_check_reset_password_proces_invalid_data_password_field_high_register():
    browser = webdriver.Chrome()
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION)
    time.sleep(1)
    restore_pass_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION)
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_class_name('msglist__row_href')
    mail[0].click()
    time.sleep(2)
    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    new_pass_input = browser.find_element_by_name('password')
    new_pass_input.send_keys('213456QAZ')
    time.sleep(2)
    browser.find_element_by_xpath("//h2[@class='LoginRightSide_h2__BFRs8']").click()
    time.sleep(1)
    submit_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    submit_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Password needs to be at least 8 characters long and must include a symbol and capital'