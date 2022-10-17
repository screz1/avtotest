from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://dev.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest110@gmail.com'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'
USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS = 'chronicletest1@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest3@ukr.net'


def test_clean_onfido_before():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get('https://dev-admin.xnl.zpoken.io/')
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login')
    admin_login.send_keys('savchukura888@gmail.com')
    admin_password = browser.find_element(By.ID, 'password')
    admin_password.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Users Information']")))
    browser.find_element(By.XPATH, "//*[text() = 'Users Information']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'search')))
    search = browser.find_element(By.ID, 'search')
    search.send_keys('chronicletest5')
    search.send_keys(Keys.RETURN)
    time.sleep(20)
    opt_button = browser.find_element(By.XPATH, "//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")))
    drop_user = browser.find_elements(By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[3].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-body']")))
    confirm = browser.find_element(By.XPATH, "//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'
    browser.close()


def test_notifications_kyc_rejected():
    options = webdriver.ChromeOptions()
    # options.add_argument("--incognito")
    options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
    })
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get('https://dev.xnl.zpoken.io/login')
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest5@ukr.net")
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'UserHeaderCard_dropdownBtn__eXCOo')))
    user_drop = browser.find_element(By.CLASS_NAME, 'UserHeaderCard_dropdownBtn__eXCOo')
    user_drop.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Dropdown_wallet__U82jL']//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(
        By.XPATH, "//div[@class='Dropdown_wallet__U82jL']//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='first_name']")))
    first_name_input = browser.find_element(By.XPATH, "//input[@name='first_name']")
    first_name_input.send_keys('Name')

    last_name_input = browser.find_element(By.XPATH, "//input[@name='last_name']")
    last_name_input.send_keys('Last')
    try:
        birthday_input = browser.find_element(By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
        if birthday_input.is_displayed():
            birthday_input.send_keys('12121999')
            print("...")
    except NoSuchElementException:
        print("...")

    last_name_input.click()
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']//h5[@class='CustomSelect_label__e7_op']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='city']")))
    city_input = browser.find_element(By.XPATH, "//input[@name='city']")
    city_input.send_keys('City')
    address_line_one_input = browser.find_element(By.XPATH, "//input[@name='line1']")
    address_line_one_input.send_keys('address one')
    address_line_two_input = browser.find_element(By.XPATH, "//input[@name='line2']")
    address_line_two_input.send_keys('address two')
    province_input = browser.find_element(By.XPATH, "//input[@name='district']")
    province_input.send_keys('district')

    zip_code_input = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    zip_code_input.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    button_continue_to_verification = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    button_continue_to_verification.click()

    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']")))
    choose_document_button = browser.find_element(
        By.XPATH,
        "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']")
    choose_document_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='driving_licence']")))
    driver_license_button = browser.find_element(By.XPATH, "//button[@data-onfido-qa='driving_licence']")
    driver_license_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'country-search')))
    country_drop_down = browser.find_element(By.ID, 'country-search')
    country_drop_down.send_keys('United States of America')
    country_drop_down.send_keys(Keys.DOWN)
    country_drop_down.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='countrySelectorNextStep']")))
    submit_document_button = browser.find_element(
        By.XPATH, "//button[@data-onfido-qa='countrySelectorNextStep']")
    submit_document_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
    image_input = browser.find_element(By.XPATH, "//input[@type='file']")
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")))
    upload_button_front = browser.find_element(By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")
    upload_button_front.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
    image_input = browser.find_element(By.XPATH, "//input[@type='file']")
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")))
    upload_button_back = browser.find_element(By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")
    upload_button_back.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='selfie-continue-btn']")))
    continue_button = browser.find_element(By.XPATH, "//button[@data-onfido-qa='selfie-continue-btn']")
    continue_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='onfido-sdk-ui-Camera-btn']")))
    camera_button = browser.find_element(By.XPATH, "//button[@class='onfido-sdk-ui-Camera-btn']")
    camera_button.click()
    time.sleep(2)
    upload_selfie_button = browser.find_element(
        By.XPATH, "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-sm']")
    upload_selfie_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'About']")))

    browser.find_element(By.XPATH, "//*[text() = 'About']").click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    browser.get('https://dev-admin.xnl.zpoken.io/')
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login')
    admin_login.send_keys('savchukura888@gmail.com')
    admin_password = browser.find_element(By.ID, 'password')
    admin_password.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Users Information']")))
    browser.find_element(By.XPATH, "//*[text() = 'Users Information']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'search')))
    browser.find_element(By.ID, 'search').send_keys('chronicletest5')
    time.sleep(18)
    opt_button = browser.find_element(By.XPATH, "//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")))
    drop_user = browser.find_elements(By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[4].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-body']")))
    confirm = browser.find_element(By.XPATH, "//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'

    browser.switch_to.window(browser.window_handles[0])
    browser.refresh()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")))
    notification_drop = browser.find_element(By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Notifications_desc__PHz3Z']")))
    reject_notif = browser.find_element(By.XPATH, "//div[@class='Notifications_desc__PHz3Z']").text
    assert reject_notif == ('Your KYC was rejected.\n'
                            'Unfortunately your KYC was rejected. Please try again.\n'
                            'a few seconds ago')
    time.sleep(1)
    browser.close()


def test_clean_onfido_after():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get('https://dev-admin.xnl.zpoken.io/')
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login')
    admin_login.send_keys('savchukura888@gmail.com')
    admin_password = browser.find_element(By.ID, 'password')
    admin_password.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Users Information']")))
    browser.find_element(By.XPATH, "//*[text() = 'Users Information']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'search')))
    search = browser.find_element(By.ID, 'search')
    search.send_keys('chronicletest5')
    search.send_keys(Keys.RETURN)
    time.sleep(18)
    opt_button = browser.find_element(By.XPATH, "//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")))
    drop_user = browser.find_elements(By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[3].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-body']")))
    confirm = browser.find_element(By.XPATH, "//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'
    browser.close()


def test_notifications_kyc_accepted():
    options = webdriver.ChromeOptions()
    # options.add_argument("--incognito")
    options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
    })

    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get('https://dev.xnl.zpoken.io/login')
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest5@ukr.net")
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'UserHeaderCard_dropdownBtn__eXCOo')))
    user_drop = browser.find_element(By.CLASS_NAME, 'UserHeaderCard_dropdownBtn__eXCOo')
    user_drop.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Dropdown_wallet__U82jL']//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(
        By.XPATH, "//div[@class='Dropdown_wallet__U82jL']//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='first_name']")))
    first_name_input = browser.find_element(By.XPATH, "//input[@name='first_name']")
    first_name_input.send_keys('Name')

    last_name_input = browser.find_element(By.XPATH, "//input[@name='last_name']")
    last_name_input.send_keys('Last')
    try:
        birthday_input = browser.find_element(By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
        if birthday_input.is_displayed():
            birthday_input.send_keys('12121999')
            print("...")
    except NoSuchElementException:
        print("...")

    last_name_input.click()
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']//h5[@class='CustomSelect_label__e7_op']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='city']")))
    city_input = browser.find_element(By.XPATH, "//input[@name='city']")
    city_input.send_keys('City')
    address_line_one_input = browser.find_element(By.XPATH, "//input[@name='line1']")
    address_line_one_input.send_keys('address one')
    address_line_two_input = browser.find_element(By.XPATH, "//input[@name='line2']")
    address_line_two_input.send_keys('address two')
    province_input = browser.find_element(By.XPATH, "//input[@name='district']")
    province_input.send_keys('district')

    zip_code_input = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    zip_code_input.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    button_continue_to_verification = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    button_continue_to_verification.click()

    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']")))
    choose_document_button = browser.find_element(
        By.XPATH,
        "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']")
    choose_document_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='driving_licence']")))
    driver_license_button = browser.find_element(By.XPATH, "//button[@data-onfido-qa='driving_licence']")
    driver_license_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'country-search')))
    country_drop_down = browser.find_element(By.ID, 'country-search')
    country_drop_down.send_keys('United States of America')
    country_drop_down.send_keys(Keys.DOWN)
    country_drop_down.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='countrySelectorNextStep']")))
    submit_document_button = browser.find_element(
        By.XPATH, "//button[@data-onfido-qa='countrySelectorNextStep']")
    submit_document_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
    image_input = browser.find_element(By.XPATH, "//input[@type='file']")
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")))
    upload_button_front = browser.find_element(By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")
    upload_button_front.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
    image_input = browser.find_element(By.XPATH, "//input[@type='file']")
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")))
    upload_button_back = browser.find_element(By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")
    upload_button_back.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='selfie-continue-btn']")))
    continue_button = browser.find_element(By.XPATH, "//button[@data-onfido-qa='selfie-continue-btn']")
    continue_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='onfido-sdk-ui-Camera-btn']")))
    camera_button = browser.find_element(By.XPATH, "//button[@class='onfido-sdk-ui-Camera-btn']")
    camera_button.click()
    time.sleep(2)
    upload_selfie_button = browser.find_element(
        By.XPATH, "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-sm']")
    upload_selfie_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'About']")))

    browser.find_element(By.XPATH, "//*[text() = 'About']").click()
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    browser.get('https://dev-admin.xnl.zpoken.io/')
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login')
    admin_login.send_keys('savchukura888@gmail.com')
    admin_password = browser.find_element(By.ID, 'password')
    admin_password.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Users Information']")))
    browser.find_element(By.XPATH, "//*[text() = 'Users Information']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'search')))
    browser.find_element(By.ID, 'search').send_keys('chronicletest5')
    time.sleep(18)
    opt_button = browser.find_element(By.XPATH, "//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")))
    drop_user = browser.find_elements(By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[2].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-body']")))
    confirm = browser.find_element(By.XPATH, "//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'

    browser.switch_to.window(browser.window_handles[0])
    browser.refresh()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")))
    notification_drop = browser.find_element(By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Notifications_desc__PHz3Z']")))
    reject_notif = browser.find_element(By.XPATH, "//div[@class='Notifications_desc__PHz3Z']").text
    assert reject_notif == ('Your KYC was approved.\n'
                            'Congratulations, your identity has been successfully verified.\n'
                            'a few seconds ago')
    time.sleep(1)
    browser.close()


def test_notifications_top_up_usdc():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[0].text
    print(bal1)

    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    sum = 100
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys(sum)
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='city']")))
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    deposit_funds.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')))
    top_up = browser.find_element(By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')
    top_up.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']")))
    cong = browser.find_element(By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']").text
    assert cong == 'Your transaction was successful'
    back_to_store = browser.find_element(
        By.XPATH, "//a[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    back_to_store.click()
    browser.refresh()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_after = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text

    print(bal1)
    assert float(bal1) == float(bal2) - sum
    time.sleep(20)
    notification_drop = browser.find_element(By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Notifications_desc__PHz3Z']")))
    top_up_notif = browser.find_element(By.XPATH, "//div[@class='Notifications_desc__PHz3Z']").text
    assert top_up_notif == ('Deposit received.\n'
                            'Amount: USDC 100 Balance: USDC 100\n'
                            'a few seconds ago')
    time.sleep(1)
    browser.close()


def test_notification_item_purchase():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[1].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")))
    items_for_purchase_usd = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    items_for_purchase_usd[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    buy_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    buy_button.click()
    time.sleep(2)
    try:
        buy_anyway_button = browser.find_element(By.ID, 'Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    tab_wallet = browser.find_element(By.ID, 'confirmBoughtwallet')
    tab_wallet.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    pay_now_button = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now_button[2].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    browser.refresh()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")))
    notification_drop = browser.find_element(By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Notifications_desc__PHz3Z']")))
    top_up_notif = browser.find_element(By.XPATH, "//div[@class='Notifications_desc__PHz3Z']").text
    assert top_up_notif == ('Item purchase\n'
                            'Your purchase of item usdc three for USDC 7.76 was successful\n'
                            'a few seconds ago')
    time.sleep(1)
    browser.close()


def test_notification_offer_purchase():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys('chronicletest3@ukr.net')
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionItems')))
    items_tab = browser.find_element(By.ID, 'profileCollectionItems')
    items_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    items = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    items[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_name__5EP5t']")))
    item = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_name__5EP5t']").text
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    market_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    next = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")))
    carency_drop = browser.find_element(By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")))
    usdc = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")
    usdc.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('9.99')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='USDC']")))
    servise = browser.find_elements(By.XPATH, "//span[@class='USDC']")
    servise_fee = servise[0].text
    youll_receive = servise[1].text
    print(servise_fee)
    print(youll_receive)
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    of = browser.find_elements(
        By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, "Dropdown_Log_out")))
    log_out = browser.find_element(By.ID, "Dropdown_Log_out")
    log_out.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")))
    browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[0].text
    trade = browser.find_element(By.XPATH, "//*[text() = 'Trade']")
    trade.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'buy']")))
    buy_button = browser.find_element(By.XPATH, "//*[text() = 'buy']")
    buy_button.click()
    time.sleep(1)
    try:
        buy_anyway_button = browser.find_element(By.ID, 'Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    wait.until(ec.visibility_of_element_located((By.ID, 'Are_you_sure_you_want_to_make_a_purchase__Buy')))
    pop_buy = browser.find_element(By.ID, 'Are_you_sure_you_want_to_make_a_purchase__Buy')
    pop_buy.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congrat = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    browser.refresh()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_after = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    assert bal1 != bal2
    print(bal1)
    print(bal2)

    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    wait.until(ec.visibility_of_element_located((By.ID, "Dropdown_Log_out")))
    log_out = browser.find_element(By.ID, "Dropdown_Log_out")
    log_out.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")))
    browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys('chronicletest3@ukr.net')
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")))

    notification_drop = browser.find_element(By.XPATH, "//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    time.sleep(1)
    top_up_notif = browser.find_element(By.XPATH, "//div[@class='Notifications_desc__PHz3Z']").text
    assert top_up_notif == ('Your item sold on the marketplace\n'
                            'Your purchase of item usdc three for USDC 7.76 was successful\n'
                            'a few seconds ago')
    time.sleep(1)
    browser.close()
