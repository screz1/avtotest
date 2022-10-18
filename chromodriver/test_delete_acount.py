from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

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
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION + '@ukr.net')
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
       By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")))
    remove_account_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")
    remove_account_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Delete_account_delete')))
    delete_button = browser.find_element(By.ID, 'Delete_account_delete')
    delete_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    get_url = browser.current_url
    assert get_url == URL
    print(get_url)

    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION + '@ukr.net')

    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']")))
    login_error = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']").text
    assert login_error == 'Oops...We struggle to find anyone registered with this Email...Please check your data or sign up.'
    time.sleep(1)


def test_check_reset_password_proces_if_user_was_deleted():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")))
    forgot_pass_button = browser.find_element(By.XPATH, "//a[@class='Input_forgotLink__Fuh_N']")
    forgot_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION + '@ukr.net')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    restore_pass_button = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_pass_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='RestoreAccessForm_tipError__k4ukD']")))
    error = browser.find_element(By.XPATH, "//div[@class='RestoreAccessForm_tipError__k4ukD']").text
    assert error == 'User not found'
    time.sleep(1)


def test_sign_up_after_deleted():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign up']")))
    browser.find_element(By.XPATH, "//*[text() = 'Sign up']").click()

    wait.until(ec.visibility_of_element_located((By.NAME, 'email')))
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(EMAIL_FOR_REGISTRATION+'@ukr.net')

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
    time.sleep(5)
    confirm_email = browser.find_element(
       By.XPATH, "//div[@class='LoginRightSide_formContainer__A5A7J']//h2[@class='LoginRightSide_h2__BFRs8']").text
    assert confirm_email == 'Confirm Email'
    text = browser.find_element(
        By.XPATH, "//div[@class='LoginRightSide_formContainer__A5A7J']//p[@class='VerifyEmail_desc__nqNEF']").text
    assert text == "We've sent you a letter with confirmation details. Please go to your Email service and follow the instructions to activate your account."
    time.sleep(2)

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys(EMAIL_FOR_REGISTRATION + '@ukr.net')

    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
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