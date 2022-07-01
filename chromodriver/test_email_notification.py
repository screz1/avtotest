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
    drop_user[3].click()
    time.sleep(2)
    confirm = browser.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'
    browser.close()


def test_email_notifications_kyc_rejected():
    options = webdriver.ChromeOptions()
    # options.add_argument("--incognito")
    options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
    })
    browser = webdriver.Chrome(options=options)
    browser.get('https://dev.xnl.zpoken.io/login')
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
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']").click()
    # browser.refresh()
    user_drop = browser.find_element_by_class_name('UserHeaderCard_dropdownBtn__eXCOo').click()
    time.sleep(2)
    manage_button = browser.find_element_by_xpath(
        "//div[@class='Dropdown_wallet__U82jL']//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']").click()
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
    time.sleep(1)
    last_name_input.click()
    time.sleep(1)
    country_drop = browser.find_element_by_xpath(
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']//h5[@class='CustomSelect_label__e7_op']").click()
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
    button_countinue_to_verification = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()

    time.sleep(3)
    choose_document_button = browser.find_element_by_xpath(
        "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']").click()
    time.sleep(1)
    driver_license_button = browser.find_element_by_xpath("//button[@data-onfido-qa='driving_licence']").click()
    time.sleep(1)
    country_drop_down = browser.find_element_by_id('country-search')
    country_drop_down.send_keys('United States of America')
    country_drop_down.send_keys(Keys.DOWN)
    country_drop_down.send_keys(Keys.RETURN)
    time.sleep(1)
    submit_document_button = browser.find_element_by_xpath(
        "//button[@data-onfido-qa='countrySelectorNextStep']").click()
    # upload_foto_button = browser.find_element_by_xpath("//button[@data-onfido-qa='uploaderButtonLink']").click()
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
    upload_selfie_button = browser.find_element_by_xpath(
        "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-sm']").click()
    time.sleep(5)
    #browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL FeaturesCardList_btn__UvK8v']").send_keys(Keys.CONTROL + 't')
    browser.find_element_by_xpath("//*[text() = 'About']").click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
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
    browser.find_element_by_id('search').send_keys('chronicletest5')
    time.sleep(18)
    opt_button = browser.find_element_by_xpath("//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    time.sleep(3)
    drop_user = browser.find_elements_by_xpath("//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[4].click()
    time.sleep(2)
    confirm = browser.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys('chronicletest5')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_element_by_class_name('noselect').click()
    time.sleep(2)
    message = browser.find_element_by_xpath("//h3[@class='readmsg__subject']").text
    assert message == 'KYC rejected'
