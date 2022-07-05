from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
import pickle
from test_z_users_create_cookie import *

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL_ADMIN = 'https://stage-admin.xnl.zpoken.io/'
URL = 'https://stage.xnl.zpoken.io/login'


def test_email_notif_kyc_rejected():
    browser = webdriver.Chrome()
    browser.get(URL_ADMIN)
    time.sleep(5)
    admin_login = browser.find_element_by_id('login').send_keys('savchukura888@gmail.com')
    time.sleep(1)
    admin_password = browser.find_element_by_id('password').send_keys('213456qaZ')
    time.sleep(1)
    sign_in_button = browser.find_element_by_xpath("//*[text() = 'Sign in']")
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
    drop_user[4].click()
    time.sleep(2)
    confirm = browser.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'
    time.sleep(2)

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys('chronicletest5@ukr.net')
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_xpath("//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    time.sleep(2)
    message = browser.find_element_by_xpath("//h3[@class='readmsg__subject']").text
    assert message == 'KYC rejected'
    print(message)
    browser.close()


def test_email_notif_kyc_approwed():
    browser = webdriver.Chrome()
    browser.get(URL_ADMIN)
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
    time.sleep(20)

    opt_button = browser.find_element_by_xpath("//button[@class='UsersTable_more__mxMkE UsersTable_icon__6yCHI']")
    opt_button.click()
    time.sleep(3)
    drop_user = browser.find_elements_by_xpath("//button[@class='UsersTable_dropDown__MKRiP']")
    drop_user[2].click()
    time.sleep(2)
    confirm = browser.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'
    time.sleep(2)

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys('chronicletest5@ukr.net')
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_xpath("//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    time.sleep(2)
    message = browser.find_element_by_xpath("//h3[@class='readmsg__subject']").text
    assert message == 'KYC approved'
    print(message)
    browser.close()


def test_email_notification_top_up():
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
    browser.refresh()
    time.sleep(5)
    balance_after = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    # bal3 = int(bal2) - sum
    print(bal1)
    assert bal1 != bal2
    time.sleep(5)

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys('chronicletest5@ukr.net')
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_xpath("//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    time.sleep(2)
    message = browser.find_element_by_xpath("//h3[@class='readmsg__subject']").text
    assert message == 'Top up'
    print(message)
    browser.close()


def test_email_notification_item_purchase():
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
    browser.execute_script("window.scrollTo(0,1800)")
    time.sleep(2)
    collections = browser.find_elements_by_xpath("//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    time.sleep(2)
    collections[6].click()
    time.sleep(2)
    items_for_purchase_usd = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    time.sleep(2)
    items_for_purchase_usd[0].click()
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

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    time.sleep(2)
    login = browser.find_element_by_name('login')
    login.send_keys('chronicletest5@ukr.net')
    # login.send_keys('chronicletest1@ukr.net')
    password = browser.find_element_by_name('password')
    password.send_keys('213456qaZ')
    password.click()
    time.sleep(2)
    password.send_keys(Keys.RETURN)
    time.sleep(2)
    mail = browser.find_elements_by_xpath("//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    time.sleep(2)
    message = browser.find_element_by_xpath("//h3[@class='readmsg__subject']").text
    assert message == 'Purchase success'
    print(message)
    browser.close()