from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
import pickle
from test_z_users_create_cookie import *
from driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL_ADMIN = 'https://dev-admin.xnl.zpoken.io/'
URL = 'https://dev.xnl.zpoken.io/login'


def test_email_notif_kyc_rejected():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login')
    admin_login.send_keys('savchukura888@gmail.com')
    admin_password = browser.find_element(By.ID, 'password')
    admin_password.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
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
    drop_user[4].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-body']")))
    confirm = browser.find_element(By.XPATH, "//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys('chronicletest5@ukr.net')
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()
    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")))
    mail = browser.find_elements(By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h3[@class='readmsg__subject']")))
    message = browser.find_element(By.XPATH, "//h3[@class='readmsg__subject']").text
    assert message == 'KYC rejected'
    print(message)
    browser.close()


def test_email_notif_kyc_approwed():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login')
    admin_login.send_keys('savchukura888@gmail.com')
    admin_password = browser.find_element(By.ID, 'password')
    admin_password.send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
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
    drop_user[2].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='UsersTable_dropDown__MKRiP']")))
    confirm = browser.find_element(By.XPATH, "//div[@class='Toastify__toast-body']").text
    assert confirm == 'EDIT SUCCESSFUL'

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys('chronicletest5@ukr.net')
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()
    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")))
    mail = browser.find_elements(By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h3[@class='readmsg__subject']")))
    message = browser.find_element(By.XPATH, "//h3[@class='readmsg__subject']").text
    assert message == 'KYC approved'
    print(message)
    browser.close()


def test_email_notification_top_up():
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
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    browser.refresh()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_after = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    # bal3 = int(bal2) - sum
    print(bal1)
    assert bal1 != bal2

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys('chronicletest5@ukr.net')

    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()
    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")))
    mail = browser.find_elements(By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h3[@class='readmsg__subject']")))
    message = browser.find_element(By.XPATH, "//h3[@class='readmsg__subject']").text
    assert message == 'Top up'
    print(message)
    browser.close()


def test_email_notification_item_purchase():
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
    items_for_purchase_usd[0].click()
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

    browser.get('https://accounts.ukr.net/login?client_id=9GLooZH9KjbBlWnuLkVX&drop_reason=logout')
    wait.until(ec.visibility_of_element_located((By.NAME, 'login')))
    login = browser.find_element(By.NAME, 'login')
    login.send_keys('chronicletest5@ukr.net')
    password = browser.find_element(By.NAME, 'password')
    password.send_keys('213456qaZ')
    password.click()
    password.send_keys(Keys.RETURN)
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")))
    mail = browser.find_elements(By.XPATH, "//tr[@class='msglist__row unread unseen icon0  ui-draggable']")
    mail[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h3[@class='readmsg__subject']")))
    message = browser.find_element(By.XPATH, "//h3[@class='readmsg__subject']").text
    assert message == 'Purchase success'
    print(message)
    browser.close()
