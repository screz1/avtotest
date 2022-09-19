from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from driver import driver

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest101@gmail.com'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest3@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest1@ukr.net'
EMAIL_FOR_REGISTRATION = 'chronicletest5'


def test_delete_account():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION + '@ukr.net')
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(3)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    remove_account_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")
    remove_account_button.click()
    time.sleep(1)
    delete_button = browser.find_element_by_id('Delete_account_delete')
    delete_button.click()
    time.sleep(1)
    get_url = browser.current_url
    assert get_url == URL
    print(get_url)

    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION + '@ukr.net')
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
    login_error = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']").text
    assert login_error == 'Oops...We struggle to find anyone registered with this Email...Please check your data or sign up.'
    time.sleep(1)


def test_check_reset_password_proces_if_user_was_deleted():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    forgot_pass_button = browser.find_element_by_xpath("//a[@class='Input_forgotLink__Fuh_N']").click()
    time.sleep(2)
    email_input = browser.find_element_by_name('email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION + '@ukr.net')
    time.sleep(1)

    restore_pass_button = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()
    time.sleep(2)
    error = browser.find_element_by_xpath("//div[@class='RestoreAccessForm_tipError__k4ukD']").text
    assert error == 'User not found'
    time.sleep(1)


def test_sign_up_after_deleted():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    browser.find_element_by_xpath("//*[text() = 'Sign up']").click()
    time.sleep(2)

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
    time.sleep(3)
    #confirm_email = browser.find_element_by_xpath("//div[@class='LoginRightSide_formContainer__A5A7J']//h2[@class='LoginRightSide_h2__BFRs8']").text
    #assert confirm_email == 'Confirm Email'
    #text = browser.find_element_by_xpath("//div[@class='LoginRightSide_formContainer__A5A7J']//p[@class='VerifyEmail_desc__nqNEF']").text
    #assert text == "We've sent you a letter to with confirmation details. Please go to your Email service and follow the instructions to activate your account."
    #time.sleep(2)

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys(EMAIL_FOR_REGISTRATION + '@ukr.net')
    #login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    #mail = browser.find_element_by_class_name('noselect').click()
    mail = browser.find_elements_by_xpath("//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    time.sleep(2)
    confirm_email = browser.find_element_by_class_name('xfmc10').click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(5)