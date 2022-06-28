from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest2@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest102@gmail.com'


def test_purchase_with_usd_wallet_card():
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
    collections[3].click()
    time.sleep(2)
    items_for_purchase_usd = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    time.sleep(2)
    items_for_purchase_usd[2].click()
    time.sleep(2)
    buy_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
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
    pay_now_button = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now_button[2].click()
    time.sleep(10)
    congratulations = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    time.sleep(6)


def test_purchase_with_usd_wallet_card_invalid_user():
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
    time.sleep(2)
    browser.execute_script("window.scrollTo(0,1800)")
    time.sleep(2)
    collections = browser.find_elements_by_xpath("//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    time.sleep(2)
    collections[4].click()
    time.sleep(2)
    items_for_purchase_usd = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    time.sleep(2)
    items_for_purchase_usd[2].click()
    time.sleep(2)
    buy_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
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
    pay_now_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    time.sleep(1)
    set_up_button = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_link__x13mQ']")
    set_up_button[1].click()
    time.sleep(1)
    verify_text = browser.find_element_by_xpath("//h3[@class='WalletComponets_title__kw_3n']").text
    assert verify_text == 'PLEASE VERIFY YOUR IDENTITY'
    time.sleep(5)


def test_purchase_user_not_avtorize():
    browser = webdriver.Chrome()
    browser.get('https://dev.xnl.zpoken.io/store')
    time.sleep(2)
    browser.execute_script("window.scrollTo(0,1800)")
    time.sleep(2)
    collections = browser.find_elements_by_xpath("//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    time.sleep(2)
    collections[4].click()
    time.sleep(2)
    items_for_purchase_usd = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    time.sleep(2)
    items_for_purchase_usd[2].click()
    time.sleep(2)
    try:
        buy_anyway_button = browser.find_element_by_id('Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    time.sleep(1)
    back_to_store = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    back_to_store.click()
    time.sleep(5)


def test_purchase_with_usd_wallet_card_user_has_not_enough_usd():
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
    collections[4].click()
    time.sleep(2)
    items_for_purchase_usd = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    time.sleep(2)
    items_for_purchase_usd[0].click()
    time.sleep(2)
    buy_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
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
    pay_now_button = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now_button[0].click()
    time.sleep(2)
    never_mind_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    never_mind_button.click()
    time.sleep(2)



