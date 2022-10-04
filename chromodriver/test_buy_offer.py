from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException
import re
from selenium.webdriver.support.color import Color
from driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest2@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'
USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS = 'chronicletest3@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest4@ukr.net'


def test_create_offers_to_valid_test():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS)

    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
       By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
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
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionItems')))
    items_tab = browser.find_element(By.ID, 'profileCollectionItems')
    items_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    items = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    items[1].click()
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
    price_input.send_keys('0.80')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionItems')))

    items_tab = browser.find_element(By.ID, 'profileCollectionItems')
    items_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    items = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    items[2].click()
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
    price_input.send_keys('10000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionItems')))

    items_tab = browser.find_element(By.ID, 'profileCollectionItems')
    items_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    items = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    items[3].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    market_button = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    next = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")))
    carency_drop = browser.find_element(By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('50')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionItems')))

    items_tab = browser.find_element(By.ID, 'profileCollectionItems')
    items_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    items = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    items[4].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    market_button = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    next = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")))
    carency_drop = browser.find_element(By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('0.80')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionItems')))

    items_tab = browser.find_element(By.ID, 'profileCollectionItems')
    items_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    items = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    items[5].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    market_button = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    next = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")))
    carency_drop = browser.find_element(By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('500000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)


def test_buy_offer_xnl_max_price():
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
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
       By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[1].text
    trade = browser.find_element(By.XPATH, "//*[text() = 'Trade']")
    trade.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']")))
    price = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'XNL 500 000.00'

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
    time.sleep(1)
    balance_after = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[1].text
    assert bal1 != bal2
    print(bal1)
    print(bal2)


def test_buy_offer_xnl_min_price():
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
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[1].text
    trade = browser.find_element(By.XPATH, "//*[text() = 'Trade']")
    trade.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']")))
    price = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'XNL 0.80'
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
    bal2 = balance_after[1].text
    assert bal1 != bal2
    print(bal1)
    print(bal2)


def test_buy_offer_xnl_normal_price():
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
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[1].text
    trade = browser.find_element(By.XPATH, "//*[text() = 'Trade']")
    trade.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']")))
    price = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'XNL 50.00'
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
    bal2 = balance_after[1].text
    assert bal1 != bal2
    print(bal1)
    print(bal2)


def test_buy_offer_usdc_max_price():
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
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']")))
    price = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'USDC 10 000.00'
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


def test_buy_offer_usdc_min_price():
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
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']")))
    price = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'USDC 0.80'
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


def test_buy_offer_usdc_normal_price():
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
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']")))
    price = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'USDC 9.99'
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


def test_create_offers_to_invalid_test():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS)

    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
       By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
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
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    next = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")))
    carency_drop = browser.find_element(By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")))
    usdc = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")
    usdc.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('50')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()

    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionItems')))
    items_tab = browser.find_element(By.ID, 'profileCollectionItems')
    items_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    items = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    items[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    market_button = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    next = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")))
    carency_drop = browser.find_element(By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('50')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
       By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)


def test_buy_usdc_offer_user_hasnt_kyc():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_VERIFICATION)

    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
       By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Trade']")))
    trade = browser.find_element(By.XPATH, "//*[text() = 'Trade']")
    trade.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    buy_button = browser.find_element(
        By.XPATH,
        "//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    buy_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_tipError__A2roI']")))
    error_message = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_tipError__A2roI']").text
    assert error_message == 'You need to top up your wallet to buy this nft'


def test_buy_xnl_offer_user_hasnt_kyc():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_VERIFICATION)

    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
       By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Trade']")))
    trade = browser.find_element(By.XPATH, "//*[text() = 'Trade']")
    trade.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    buy_button = browser.find_element(
        By.XPATH,
        "//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    buy_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_tipError__A2roI']")))
    error_message = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_tipError__A2roI']").text
    assert error_message == 'You need to top up your wallet to buy this nft'


def test_buy_usdc_offer_user_hasnt_money():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY)

    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Trade']")))
    trade = browser.find_element(By.XPATH, "//*[text() = 'Trade']")
    trade.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    buy_button = browser.find_element(
        By.XPATH,
        "//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    buy_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_tipError__A2roI']")))
    error_message = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_tipError__A2roI']").text
    assert error_message == 'You need to top up your wallet to buy this nft'


def test_buy_xnl_offer_user_hasnt_money():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY)

    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Trade']")))
    trade = browser.find_element(By.XPATH, "//*[text() = 'Trade']")
    trade.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    buy_button = browser.find_element(
        By.XPATH,
        "//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    buy_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_tipError__A2roI']")))
    error_message = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_tipError__A2roI']").text
    assert error_message == 'You need to top up your wallet to buy this nft'


def test_delete_test_offers():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS)

    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located((
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionListings')))
    listings_tab = browser.find_element(By.ID, 'profileCollectionListings')
    listings_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'stop listing']")))
    browser.find_element(By.XPATH, "//*[text() = 'stop listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Delete_listing__delete_it')))
    browser.find_element(By.ID, 'Delete_listing__delete_it').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'view listings ']")))
    browser.find_element(By.XPATH, "//*[text() = 'view listings ']").click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'stop listing']")))
    browser.find_element(By.XPATH, "//*[text() = 'stop listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Delete_listing__delete_it')))
    browser.find_element(By.ID, 'Delete_listing__delete_it').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'view listings ']")))
    browser.find_element(By.XPATH, "//*[text() = 'view listings ']")
    time.sleep(1)