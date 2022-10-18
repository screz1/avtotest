from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest2@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest4@ukr.net'


def test_kyc_verification():
    options = webdriver.ChromeOptions()
    # options.add_argument("--incognito")
    options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
    })

    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys("chronicletest4@ukr.net")

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
    time.sleep(1)
    try:
        birthday_input = browser.find_element(By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
        if birthday_input.is_displayed():
            birthday_input.send_keys('12121999')
            print("...")
    except NoSuchElementException:
        print("...")

    last_name_input.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']//h5[@class='CustomSelect_label__e7_op']")))
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
    button_countinue_to_verification = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    button_countinue_to_verification.click()

    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']")))
    choose_document_button = browser.find_element(
        By.XPATH, "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']")
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
    submit_document_button = browser.find_element(By.XPATH, "//button[@data-onfido-qa='countrySelectorNextStep']")
    submit_document_button.click()

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
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-sm']")))
    upload_selfie_button = browser.find_element(
        By.XPATH, "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-sm']")
    upload_selfie_button.click()
    time.sleep(10)
    browser.close()