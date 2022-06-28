from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
CARD = '4242 4242 4242 4242 12 24 123 58000'
INVALID_CARD = '  4200 0000 0000 0000  12 24  123  58000 '
MM_YY = '12 24'
CVC = '123'
POST = '58000'




USER_WITH_EMAIL_VERIFICATION = 'chronicletest3@ukr.net'





def test_purchase_with_credit_card():
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
    tab_pay_with_card = browser.find_element_by_id('confirmBoughtpay with card').click()
    time.sleep(3)
    card_number_input = browser.find_element_by_xpath('//input[@class="__PrivateStripeElement-input"]')
    card_number_input.send_keys(CARD)
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='portal']/div/div/div[2]/div[3]/button[2]").click()
    #pay_now_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    #pay_now_button.click()
    time.sleep(6)
    congratulations = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    time.sleep(6)


def test_purchase_with_saved_credit_card():
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
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0,1800)")
    time.sleep(4)
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
    time.sleep(1)
    tab_pay_saved_with_card = browser.find_element_by_id('confirmBoughtmy saved cards').click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[@id='portal']/div/div/div[2]/div[3]/button[2]").click()
    #pay_now_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    time.sleep(6)
    congratulations = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    time.sleep(6)


def test_purchase_with_credit_card_invalid_card():
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
    collections[3].click()
    time.sleep(2)
    items_for_purchase_usd = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    time.sleep(2)
    items_for_purchase_usd[1].click()
    time.sleep(3)
    buy_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(2)
    try:
        buy_anyway_button = browser.find_element_by_id('Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    tab_pay_with_card = browser.find_element_by_id('confirmBoughtpay with card').click()
    time.sleep(3)
    card_number_input = browser.find_element_by_xpath('//input[@class="__PrivateStripeElement-input"]')

    card_number_input.send_keys(INVALID_CARD)

    time.sleep(2)

    pay_now_button = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now_button[1].click()

    time.sleep(7)

    congratulations = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    time.sleep(6)