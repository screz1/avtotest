from selenium import webdriver
#from seleniumwire import webdriver
from selenium.webdriver import Keys
import time
import random
from selenium.webdriver.chrome.options import Options #as chrome_options
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException


STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest2@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest4@ukr.net'






def test_first():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    browser.get('https://google.com')
    input_google = browser.find_element_by_xpath('//input[@name="q"]')
    input_google.send_keys("samsung")
    input_google.send_keys(Keys.RETURN)
    assert "samsung - Поиск в Google" in browser.title

    #input_google_one = browser.find_element_by_id()

    time.sleep(5)
    browser.close()


def test_second_sign_in_on_chronicle1():
    browser = webdriver.Chrome()
    browser.get('https://dev.xnl.zpoken.io/login')
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")
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
    time.sleep(5)
    browser.close()


def test_second_sign_in_on_chronicle2and3():
    browser = webdriver.Chrome()
    browser.get('https://dev.xnl.zpoken.io/login')
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(" ")

    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.click()
    login_error = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr']//div[@class='Input_tipError__CKiEf']")
    input_chronicle_password.send_keys("")
    time.sleep(1)

    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    password_error = browser.find_element_by_xpath("//label[@class='Input_label__CWIqo']//div[@class='Input_tipError__CKiEf']")
    check_box.click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath("//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(5)
    browser.close()


def test_second_sign_in_on_chronicle4():
    browser = webdriver.Chrome()
    browser.get('https://dev.xnl.zpoken.io/login')
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest999@gmail.com")
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    time.sleep(1)
    check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(5)
    login_error = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']")
    time.sleep(5)
    browser.close()


def test_second_sign_in_on_chronicle5():
    browser = webdriver.Chrome()
    browser.get('https://dev.xnl.zpoken.io/login')
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZZ")
    time.sleep(1)
    check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(5)
    login_error = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr']//div[@class='LoginForm_tipError__pmHEw']")
    time.sleep(5)
    browser.close()


def test_forgot_password_page():
    browser = webdriver.Chrome()
    browser.get('https://dev.xnl.zpoken.io/login')
    forgot_password_button = browser.find_element_by_xpath('//a[@class="Input_forgotLink__Fuh_N"]')
    forgot_password_button.click()
    time.sleep(1)
    enter_email_address_input = browser.find_element_by_class_name('Input_input__lvORT')
    enter_email_address_input.send_keys('chronicletest108@gmail.com')
    time.sleep(2)
    restore_password_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_password_button.click()
    time.sleep(5)
    browser.close()


def test_gmail_connection():
    option = webdriver.ChromeOptions()
    #option.set_preference('dom.webdriver.enabled', False)
    option.add_argument("--disable-blink-features=AutomationControlled")


    browser = webdriver.Chrome(options=option)
    browser.get('https://www.google.com/intl/ru/gmail/about/')
    time.sleep(1)
    sign_in_button = browser.find_element_by_xpath("//a [@data-action='sign in']")
    sign_in_button.click()
    time.sleep(5)
    login_input = browser.find_element_by_id("identifierId")
    login_input.send_keys('chronicletest108@gmail.com')
    time.sleep(1)
    next_button = browser.find_element_by_id('identifierNext')
    #next_button = browser.find_element_by_xpath("//div [@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']")
    next_button.click()
    time.sleep(5)

    #password_input =

def test_forgot_password_page_invalid_email():
    browser = webdriver.Chrome()
    browser.get('https://dev.xnl.zpoken.io/login')
    forgot_password_button = browser.find_element_by_xpath('//a[@class="Input_forgotLink__Fuh_N"]')
    forgot_password_button.click()
    time.sleep(1)
    enter_email_address_input = browser.find_element_by_class_name('Input_input__lvORT')
    enter_email_address_input.send_keys('chronicletest999@gmail.com')
    time.sleep(5)
    restore_password_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    restore_password_button.click()
    time.sleep(5)
    user_not_found = browser.find_element_by_class_name('RestoreAccessForm_tipError__k4ukD')
    time.sleep(5)
    browser.close()


def test_kyc_verification():
    options = webdriver.ChromeOptions()
    #options.add_argument("--incognito")
    options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
    })

    browser = webdriver.Chrome(options=options)
    browser.get('https://stage.xnl.zpoken.io/login')
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest5@ukr.net")
    time.sleep(2)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    time.sleep(2)
    check_box = browser.find_element_by_xpath(
        "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']").click()
    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']").click()

    time.sleep(5)
    pop_up_two_fa = browser.find_element_by_xpath("//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']").click()
    # browser.refresh()
    user_drop = browser.find_element_by_class_name('UserHeaderCard_dropdownBtn__eXCOo').click()
    time.sleep(2)
    manage_button = browser.find_element_by_xpath("//div[@class='Dropdown_wallet__U82jL']//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']").click()
    time.sleep(1)

    first_name_input = browser.find_element_by_xpath("//input[@name='first_name']")
    first_name_input.send_keys('Name')
    time.sleep(1)
    last_name_input = browser.find_element_by_xpath("//input[@name='last_name']")
    last_name_input.send_keys('Last')
    time.sleep(1)
    try:
        birthday_input = browser.find_element_by_xpath("//input[@placeholder='DD/MM/YYYY']")
        if birthday_input.is_displayed():
            birthday_input.send_keys('12121999')
            print("...")
    except NoSuchElementException:
        print("...")


    #birthday_input = browser.find_element_by_xpath("//input[@placeholder='DD/MM/YYYY']")
    #birthday_input.send_keys('12121999')
    time.sleep(1)
    last_name_input.click()
    time.sleep(1)
    country_drop = browser.find_element_by_xpath("//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']//h5[@class='CustomSelect_label__e7_op']").click()
    time.sleep(1)
    country = browser.find_elements_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    time.sleep(1)
    city_input = browser.find_element_by_xpath("//input[@name='city']")
    city_input.send_keys('City')
    time.sleep(1)
    address_line_one_input = browser.find_element_by_xpath("//input[@name='line1']")
    address_line_one_input.send_keys('address one')
    time.sleep(1)
    address_line_two_input = browser.find_element_by_xpath("//input[@name='line2']")
    address_line_two_input.send_keys('address two')
    time.sleep(1)
    province_input = browser.find_element_by_xpath("//input[@name='district']")
    province_input.send_keys('district')
    time.sleep(1)
    zip_code_input = browser.find_element_by_xpath("//input[@name='postalCode']")
    zip_code_input.send_keys('58000')
    time.sleep(1)
    button_countinue_to_verification = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()

    time.sleep(3)
    choose_document_button = browser.find_element_by_xpath("//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']").click()
    time.sleep(1)
    driver_license_button = browser.find_element_by_xpath("//button[@data-onfido-qa='driving_licence']").click()
    time.sleep(1)
    country_drop_down = browser.find_element_by_id('country-search')
    country_drop_down.send_keys('United States of America')
    country_drop_down.send_keys(Keys.DOWN)
    country_drop_down.send_keys(Keys.RETURN)
    time.sleep(1)
    submit_document_button = browser.find_element_by_xpath("//button[@data-onfido-qa='countrySelectorNextStep']").click()
    #upload_foto_button = browser.find_element_by_xpath("//button[@data-onfido-qa='uploaderButtonLink']").click()
    image_input = browser.find_element_by_xpath("//input[@type='file']")
    image_input.send_keys("C:/Users/WellDone/PycharmProjects/Selenium/sample_driving_licence (1).png")
    time.sleep(1)
    upload_button_front = browser.find_element_by_xpath("//button[@data-onfido-qa='confirm-action-btn']").click()
    time.sleep(5)
    image_input = browser.find_element_by_xpath("//input[@type='file']")
    image_input.send_keys("C:/Users/WellDone/PycharmProjects/Selenium/sample_driving_licence (1).png")
    time.sleep(5)
    upload_button_back = browser.find_element_by_xpath("//button[@data-onfido-qa='confirm-action-btn']").click()
    time.sleep(5)

    continue_button = browser.find_element_by_xpath("//button[@data-onfido-qa='selfie-continue-btn']").click()
    time.sleep(2)
    camera_button = browser.find_element_by_xpath("//button[@class='onfido-sdk-ui-Camera-btn']").click()
    time.sleep(2)
    upload_selfie_button = browser.find_element_by_xpath("//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-sm']").click()
    time.sleep(2)
    browser.close()


def test_check_trade_screen():
    browser = webdriver.Chrome()
    browser.get('https://dev.xnl.zpoken.io/login')
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest102@gmail.com")
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
    time.sleep(10)
    pop_up_two_fa = browser.find_element_by_xpath("//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")


    pop_up_two_fa.click()
    #browser.refresh()



    time.sleep(5)
    browser.close()


def test_www():
    useragent = UserAgent()
    option = webdriver.ChromeOptions()
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_argument(f"user-agent={useragent.random}")
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument('--disable-extensions')
    option.add_argument("--incognito")
    option.add_argument("--disable-plugins-discovery")
    #option.add_argument("--start-maximized")

    browser = webdriver.Chrome(f"./chromedriver", options=option)
    browser.get('https://bot.sannysoft.com/')
    time.sleep(2)


    #browser.get('https://www.google.com/intl/ru/gmail/about/')
    #time.sleep(1)
    #sign_in_button = browser.find_element_by_xpath("//a [@data-action='sign in']")
    #sign_in_button.click()
    #time.sleep(2)
    #login_input = browser.find_element_by_id("identifierId")
    #login_input.send_keys('chronicletest108@gmail.com')
    #time.sleep(1)
    #next_button = browser.find_element_by_id('identifierNext')
    # next_button = browser.find_element_by_xpath("//div [@class='VfPpkd-dgl2Hf-ppHlrf-sM5MNb']")
    #next_button.click()
    #time.sleep(5)


def test_download_image():
    browser = webdriver.Chrome()
    browser.get('https://www.websiteplanet.com/ru/webtools/dummy-images-generator/')
    time.sleep(5)
    long_field_input = browser.find_element_by_id('imgW')
    long_field_input.clear()
    long_field_input.send_keys('600')
    high_field_input = browser.find_element_by_id('imgH')
    high_field_input.clear()
    high_field_input.send_keys('600')
    save_button = browser.find_element_by_id('dummy-save')
    for i in range(5000):
        save_button.click()
        time.sleep(0.1)
    time.sleep(5)


def test_registration_with_10minute_email():
    #options = webdriver.ChromeOptions()

    browser = webdriver.Chrome()

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys('chronicletest101')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)

    #continue_button = browser.find_element_by_xpath("//button[@class='Ol0-ktls jY4tHruE _2Qy_WiMj']//div[@class='_tkoBLTr']").click()
    time.sleep(5)

def test_one():
    a = "3"
    b = "1"
    c = int(a) - int(b)
    print(c)


def test_two():
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
    time.sleep(2)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    manage_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']").click()
    time.sleep(1)
    balance_before = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[0].text
    print(bal1)

    usdc_drop = browser.find_element_by_id('USDC').click()
    time.sleep(1)
    fiat = browser.find_element_by_id('Top_up_with_fiat').click()
    time.sleep(1)
    sum = 100
    amount = browser.find_element_by_xpath("//input[@name='amount']")
    amount.send_keys(sum)
    card_holder = browser.find_element_by_xpath("//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element_by_xpath("//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element_by_xpath("//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element_by_xpath("//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element_by_xpath(
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    time.sleep(1)
    country = browser.find_elements_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element_by_xpath("//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element_by_xpath("//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element_by_xpath("//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element_by_xpath("//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element_by_xpath("//input[@name='postalCode']")
    postal.send_keys('58000')
    time.sleep(1)
    deposit_funds = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    deposit_funds.click()
    time.sleep(1)
    top_up = browser.find_element_by_id('Are_you_sure_you_want_to_make_a_top_up__top_up')
    top_up.click()
    time.sleep(10)
    cong = browser.find_element_by_xpath("//p[@class='__3dsecure_smallText__V9LrF']").text
    assert cong == 'Your transaction was successful'
    back_to_store = browser.find_element_by_xpath(
        "//a[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    back_to_store.click()
    time.sleep(5)
    balance_after = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    #bal3 = int(bal2) - sum
    print(bal1)
    assert float(bal1) == float(bal2) - sum
    time.sleep(5)