from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest101@gmail.com'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest1@ukr.net'


CARD = '  4242 4242 4242 4242  12 24  123  58000 '
INVALID_CARD = '  4200 0000 0000 0000  12 24  123  58000 '


def test_buy_usdc_mystery_box_with_wallet():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(1)
    balance_before = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[0].text
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    time.sleep(1)
    price = browser.find_element_by_xpath("//div[@class='MysteryBoxPrice_value__Mg8SM']").text

    time.sleep(1)
    try_your_luck = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    wallet_tab = browser.find_element_by_id('confirmBoughtwallet')
    time.sleep(1)

    pay_now = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now[1].click()
    time.sleep(10)
    congrat = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    time.sleep(1)
    balance_after = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    assert bal1 != bal2



def test_buy_usdc_mystery_box_with_stripe():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    time.sleep(1)
    try_your_luck = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    card_tab = browser.find_element_by_id('confirmBoughtpay with card').click()
    time.sleep(1)
    card_number_input = browser.find_element_by_xpath('//input[@class="__PrivateStripeElement-input"]')
    card_number_input.send_keys(CARD)
    time.sleep(1)
    save_card = browser.find_element_by_name('Save for future payments').click()
    time.sleep(1)
    pay_now = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now[0].click()
    time.sleep(10)
    congrat = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    time.sleep(1)


def test_buy_usdc_mystery_box_with_stripe_saved_card():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    time.sleep(1)
    try_your_luck = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    saved_card_tab = browser.find_element_by_id('confirmBoughtmy saved cards').click()
    time.sleep(1)

    pay_now = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now[0].click()
    time.sleep(10)
    congrat = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    time.sleep(1)


def test_buy_xnl_mystery_box_with_wallet():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[0].click()
    time.sleep(1)
    try_your_luck = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    wallet_tab = browser.find_element_by_id('confirmBoughtwallet')
    time.sleep(2)
    pay_now = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")

    pay_now[1].click()

    time.sleep(10)
    congrat = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    time.sleep(1)


def test_buy_usdc_mystery_box_with_wallet_user_have_not_money():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY)
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
    time.sleep(3)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    time.sleep(1)
    try_your_luck = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    wallet_tab = browser.find_element_by_id('confirmBoughtwallet')
    time.sleep(1)
    pay_now = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now[0].click()
    time.sleep(1)
    nevermind = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    nevermind.click()
    time.sleep(1)


def test_buy_xnl_mystery_box_with_wallet_user_have_not_money():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY)
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
    time.sleep(3)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[0].click()
    time.sleep(1)
    try_your_luck = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    wallet_tab = browser.find_element_by_id('confirmBoughtwallet')
    time.sleep(1)
    pay_now = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now[0].click()
    time.sleep(1)
    nevermind = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    nevermind.click()
    time.sleep(1)


def test_buy_usdc_mystery_box_with_wallet_user_not_avtorise_sign_in_button():
    browser = webdriver.Chrome()
    browser.get(URL)
    time.sleep(1)
    browser.find_element_by_class_name('Logo_min__TBvKP').click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    time.sleep(5)
    try_your_luck = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    sign_in = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    sign_in[1].click()
    time.sleep(1)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]').is_displayed()
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]').is_displayed()
    time.sleep(1)


def test_buy_usdc_mystery_box_with_wallet_user_not_avtorise_register_button():
    browser = webdriver.Chrome()
    browser.get(URL)
    time.sleep(1)
    browser.find_element_by_class_name('Logo_min__TBvKP').click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    time.sleep(5)
    try_your_luck = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    register = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    register.click()
    time.sleep(2)
    birth_input = browser.find_element_by_xpath("//input[@placeholder='DD/MM/YYYY']").is_displayed()


def test_buy_usdc_mystery_box_with_wallet_user_have_not_kyc():
    browser = webdriver.Chrome()
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_VERIFICATION)
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
    time.sleep(3)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(1)
    browser.execute_script("window.scrollTo(0,1000)")
    time.sleep(2)
    details = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    time.sleep(1)
    try_your_luck = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    time.sleep(2)
    wallet_tab = browser.find_element_by_id('confirmBoughtwallet')
    time.sleep(1)
    pay_now = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now[0].click()
    set_up_wallet = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_link__x13mQ']")
    set_up_wallet.click()
    time.sleep(1)
    first_name_input = browser.find_element_by_xpath("//input[@name='first_name']")
    last_name_input = browser.find_element_by_xpath("//input[@name='last_name']")
    try:
        birthday_input = browser.find_element_by_xpath("//input[@placeholder='DD/MM/YYYY']")
        if birthday_input.is_displayed():
            print("...")
    except NoSuchElementException:
        print("...")
    country_drop = browser.find_element_by_xpath(
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']//h5[@class='CustomSelect_label__e7_op']").click()
    city_input = browser.find_element_by_xpath("//input[@name='city']")
    address_line_one_input = browser.find_element_by_xpath("//input[@name='line1']")
    address_line_two_input = browser.find_element_by_xpath("//input[@name='line2']")
    province_input = browser.find_element_by_xpath("//input[@name='district']")
    zip_code_input = browser.find_element_by_xpath("//input[@name='postalCode']")
    time.sleep(1)

