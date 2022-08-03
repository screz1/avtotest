from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from driver import driver

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
    time.sleep(5)
    admin_login = browser.find_element_by_id('login').send_keys('savchukura888@gmail.com')
    time.sleep(1)
    admin_password = browser.find_element_by_id('password').send_keys('213456qaZ')
    time.sleep(1)
    sign_in_button = browser.find_element_by_xpath("//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")
    sign_in_button.click()
    time.sleep(3)
    browser.find_element_by_xpath("//*[text() = 'Users Information']").click()
    time.sleep(3)
    search = browser.find_element_by_id('search')
    search.send_keys('chronicletest5')
    search.send_keys(Keys.RETURN)
    time.sleep(20)
    opt_button = browser.find_element_by_xpath("//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    time.sleep(3)
    drop_user = browser.find_elements_by_xpath("//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[3].click()
    time.sleep(2)
    confirm = browser.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
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
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
    time.sleep(1)
    upload_button_front = browser.find_element_by_xpath("//button[@data-onfido-qa='confirm-action-btn']").click()
    time.sleep(5)
    image_input = browser.find_element_by_xpath("//input[@type='file']")
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
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
    browser.refresh()
    time.sleep(2)
    notification_drop = browser.find_element_by_xpath("//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    time.sleep(1)
    reject_notif = browser.find_element_by_xpath("//div[@class='Notifications_desc__PHz3Z']").text
    assert reject_notif == ('Your KYC was rejected.\n'
 'Unfortunately your KYC was rejected. Please try again.\n'
 'a few seconds ago')
    time.sleep(1)
    browser.close()


def test_clean_onfido_after():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get('https://dev-admin.xnl.zpoken.io/')
    time.sleep(5)
    admin_login = browser.find_element_by_id('login').send_keys('savchukura888@gmail.com')
    time.sleep(1)
    admin_password = browser.find_element_by_id('password').send_keys('213456qaZ')
    time.sleep(1)
    sign_in_button = browser.find_element_by_xpath("//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX CustomButton_withIcon__hyuiZ']")
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
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
    time.sleep(1)
    upload_button_front = browser.find_element_by_xpath("//button[@data-onfido-qa='confirm-action-btn']").click()
    time.sleep(5)
    image_input = browser.find_element_by_xpath("//input[@type='file']")
    image_input.send_keys("/home/user/PycharmProjects/avtotest/sample_driving_licence (1).png")
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
    drop_user[2].click()
    time.sleep(2)
    confirm = browser.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)
    browser.refresh()
    time.sleep(2)
    notification_drop = browser.find_element_by_xpath("//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    time.sleep(1)
    reject_notif = browser.find_element_by_xpath("//div[@class='Notifications_desc__PHz3Z']").text
    assert reject_notif == ('Your KYC was approved.\n'
 'Congratulations, your identity has been successfully verified.\n'
 'a few seconds ago')
    time.sleep(1)
    browser.close()


def test_notifications_top_up_usdc():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
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
    browser.refresh()
    time.sleep(5)
    balance_after = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    # bal3 = int(bal2) - sum
    print(bal1)
    assert float(bal1) == float(bal2) - sum
    time.sleep(20)
    notification_drop = browser.find_element_by_xpath("//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    time.sleep(1)
    top_up_notif = browser.find_element_by_xpath("//div[@class='Notifications_desc__PHz3Z']").text
    assert top_up_notif == ('Deposit received.\n'
                            'Amount: USDC 100 Balance: USDC 100\n'
                            'a few seconds ago')
    time.sleep(1)
    browser.close()


def test_notification_item_purchase():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
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
    browser.execute_script("window.scrollTo(0,1800)")
    time.sleep(2)
    collections = browser.find_elements_by_xpath("//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    time.sleep(2)
    collections[4].click()
    time.sleep(2)
    items_for_purchase_usd = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    time.sleep(2)
    items_for_purchase_usd[1].click()
    time.sleep(2)
    buy_button = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(2)
    try:
        buy_anyway_button = browser.find_element_by_id('Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    tab_wallet = browser.find_element_by_id('confirmBoughtwallet').click()
    time.sleep(1)
    pay_now_button = browser.find_elements_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now_button[2].click()
    time.sleep(10)
    congratulations = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    time.sleep(6)
    browser.refresh()
    time.sleep(5)
    notification_drop = browser.find_element_by_xpath("//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    time.sleep(1)
    top_up_notif = browser.find_element_by_xpath("//div[@class='Notifications_desc__PHz3Z']").text
    assert top_up_notif == ('Item purchase\n'
                            'Your purchase of item usdc three for USDC 7.76 was successful\n'
                            'a few seconds ago')
    time.sleep(1)
    browser.close()


def test_notification_offer_purchase():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys('chronicletest1@ukr.net')
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
    time.sleep(2)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    time.sleep(1)
    my_collection = browser.find_elements_by_xpath("//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    time.sleep(1)
    items_tab = browser.find_element_by_id('profileCollectionItems').click()
    time.sleep(3)
    items = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    items[0].click()
    time.sleep(1)
    item = browser.find_element_by_xpath("//div[@class='HeaderItemCard_name__5EP5t']").text
    time.sleep(3)
    market_button = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    time.sleep(1)
    next = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    time.sleep(3)
    carency_drop = browser.find_element_by_xpath("//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    time.sleep(1)
    usdc = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")
    usdc.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('9.99')
    time.sleep(1)
    servise = browser.find_elements_by_xpath("//span[@class='USDC']")
    servise_fee = servise[0].text
    youll_receive = servise[1].text
    print(servise_fee)
    print(youll_receive)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    of = browser.find_elements_by_xpath(
        "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    time.sleep(1)
    user_drop.click()
    time.sleep(1)
    #my_collection[2].click()
    time.sleep(1)
    log_out = browser.find_element_by_id("Dropdown_Log_out")
    log_out.click()
    time.sleep(1)
    browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']").click()
    time.sleep(3)

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
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    balance_before = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[0].text
    trade = browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(3)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    time.sleep(1)

    buy_button = browser.find_element_by_xpath("//*[text() = 'buy']").click()
    time.sleep(1)
    try:
        buy_anyway_button = browser.find_element_by_id('Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    time.sleep(1)
    pop_buy = browser.find_element_by_id('Are_you_sure_you_want_to_make_a_purchase__Buy')
    pop_buy.click()
    time.sleep(10)
    congrat = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    time.sleep(1)
    browser.refresh()
    time.sleep(1)
    balance_after = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    assert bal1 != bal2
    print(bal1)
    print(bal2)

    time.sleep(3)
    browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    #user_drop.click()
    time.sleep(1)
    #my_collection[1].click()
    time.sleep(1)
    log_out = browser.find_element_by_id("Dropdown_Log_out")
    log_out.click()
    time.sleep(1)
    browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']").click()
    time.sleep(3)

    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys('chronicletest1@ukr.net')
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
    time.sleep(2)

    notification_drop = browser.find_element_by_xpath("//div[@class='Notifications_dropbtn__iJw44']")
    notification_drop.click()
    time.sleep(1)
    top_up_notif = browser.find_element_by_xpath("//div[@class='Notifications_desc__PHz3Z']").text
    assert top_up_notif == ('Your item sold on the marketplace\n'
                            'Your purchase of item usdc three for USDC 7.76 was successful\n'
                            'a few seconds ago')
    time.sleep(1)
    browser.close()