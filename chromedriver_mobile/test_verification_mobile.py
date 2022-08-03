import time

import pytest
from test_conf import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains

EMAIL_FOR_REGISTRATION = 'chronicletest5@ukr.net'
URL = 'https://stage.xnl.zpoken.io/login'

WIDTH = 412
HEIGHT = 915
PIXEL_RATIO = 3.0


def test_kyc_verification():
    UA = 'Mozilla/5.0 (Linux; Android 9; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
    mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
    })

    options.add_experimental_option('mobileEmulation', mobileEmulation)

    # options.add_argument('--window-size=412,915')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    check_box = browser.find_element(By.XPATH,
                                     "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(By.XPATH,
                                         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Mobile_hamburgerWrap__hd83L']")))
    menu = browser.find_element(By.XPATH, "//div[@class='Mobile_hamburgerWrap__hd83L']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='first_name']")))
    first_name_input = browser.find_element(By.XPATH, "//input[@name='first_name']")
    first_name_input.send_keys('Name')

    last_name_input = browser.find_element(By.XPATH, "//input[@name='last_name']")
    last_name_input.send_keys('Last')

    try:
        birthday_input = browser.find_element_by_xpath("//input[@placeholder='DD/MM/YYYY']")
        if birthday_input.is_displayed():
            birthday_input.send_keys('12121999')
            print("...")
    except NoSuchElementException:
        print("...")


    last_name_input.click()

    country_drop = browser.find_element(By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']//h5[@class='CustomSelect_label__e7_op']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()

    city_input = browser.find_element(By.XPATH, "//input[@name='city']")
    city_input.send_keys('City')

    address_line_one_input = browser.find_element(By.XPATH, "//input[@name='line1']")
    address_line_one_input.send_keys('address one')

    address_line_two_input = browser.find_element(By.XPATH, "//input[@name='line2']")
    address_line_two_input.send_keys('address two')
    browser.execute_script("window.scrollTo(0,1000)")
    province_input = browser.find_element(By.XPATH, "//input[@name='district']")
    province_input.send_keys('district')

    zip_code_input = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    zip_code_input.send_keys('58000')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    button_countinue_to_verification = browser.find_element(By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']")))
    choose_document = browser.find_element(By.XPATH, "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-centered onfido-sdk-ui-Theme-button-lg']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='driving_licence']")))
    driver_license_button = browser.find_element(By.XPATH, "//button[@data-onfido-qa='driving_licence']").click()

    wait.until(ec.visibility_of_element_located((By.ID, 'country-search')))

    country_drop_down = browser.find_element(By.ID, 'country-search')
    country_drop_down.send_keys('United States of America')
    country_drop_down.send_keys(Keys.DOWN)
    country_drop_down.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='countrySelectorNextStep']")))
    submit_document_button = browser.find_element(By.XPATH, "//button[@data-onfido-qa='countrySelectorNextStep']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
    image_input = browser.find_element(By.XPATH, "//input[@type='file']")

    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")))
    upload_button_front = browser.find_element(By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))

    image_input = browser.find_element(By.XPATH, "//input[@type='file']")
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']")))
    upload_button_back = browser.find_element(By.XPATH, "//button[@data-onfido-qa='confirm-action-btn']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@data-onfido-qa='selfie-continue-btn']")))

    continue_button = browser.find_element(By.XPATH, "//button[@data-onfido-qa='selfie-continue-btn']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='onfido-sdk-ui-Camera-btn']")))

    camera_button = browser.find_element(By.XPATH, "//button[@class='onfido-sdk-ui-Camera-btn']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-sm']")))

    upload_selfie_button = browser.find_element(By.XPATH,
        "//button[@class='ods-button -action--primary onfido-sdk-ui-Theme-button-sm']").click()
    time.sleep(2)
    browser.close()


