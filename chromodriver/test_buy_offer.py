from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
import re
from selenium.webdriver.support.color import Color
from driver import driver

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
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    time.sleep(1)
    #check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
    #time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    my_collection = browser.find_elements_by_xpath("//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    time.sleep(1)
    items_tab = browser.find_element_by_id('profileCollectionItems').click()
    time.sleep(3)
    items = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    items[0].click()
    time.sleep(2)
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
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    items_tab = browser.find_element_by_id('profileCollectionItems').click()
    time.sleep(3)
    items = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    items[1].click()
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
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('0.80')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)

    items_tab = browser.find_element_by_id('profileCollectionItems').click()
    time.sleep(3)
    items = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    items[2].click()
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
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('10000')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)

    items_tab = browser.find_element_by_id('profileCollectionItems').click()
    time.sleep(3)
    items = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    items[3].click()
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
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('50')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)

    items_tab = browser.find_element_by_id('profileCollectionItems').click()
    time.sleep(3)
    items = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    items[4].click()
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
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('0.80')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)

    items_tab = browser.find_element_by_id('profileCollectionItems').click()
    time.sleep(3)
    items = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    items[5].click()
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
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('500000')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)


def test_buy_offer_xnl_max_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    time.sleep(1)
    #check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
    #time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    balance_before = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[1].text
    trade = browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(3)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    time.sleep(2)
    price = browser.find_element_by_xpath("//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'XNL 500 000.00'
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
    bal2 = balance_after[1].text
    assert bal1 != bal2
    print(bal1)
    print(bal2)


def test_buy_offer_xnl_min_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    #time.sleep(1)
    #check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
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
    bal1 = balance_before[1].text
    trade = browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(3)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    time.sleep(2)
    price = browser.find_element_by_xpath("//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'XNL 0.80'
    buy_button = browser.find_element_by_xpath("//*[text() = 'buy']").click()
    time.sleep(1)
    try:
        buy_anyway_button = browser.find_element_by_id('Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    time.sleep(2)
    pop_buy = browser.find_element_by_id('Are_you_sure_you_want_to_make_a_purchase__Buy')
    pop_buy.click()
    time.sleep(10)
    congrat = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    time.sleep(1)
    browser.refresh()
    time.sleep(1)
    balance_after = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[1].text
    assert bal1 != bal2
    print(bal1)
    print(bal2)


def test_buy_offer_xnl_normal_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    #time.sleep(1)
    #check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
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
    bal1 = balance_before[1].text
    trade = browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(3)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    time.sleep(2)
    price = browser.find_element_by_xpath("//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'XNL 50.00'
    buy_button = browser.find_element_by_xpath("//*[text() = 'buy']").click()
    time.sleep(1)
    try:
        buy_anyway_button = browser.find_element_by_id('Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    time.sleep(2)
    pop_buy = browser.find_element_by_id('Are_you_sure_you_want_to_make_a_purchase__Buy')
    pop_buy.click()
    time.sleep(10)
    congrat = browser.find_element_by_xpath("//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    time.sleep(1)
    browser.refresh()
    time.sleep(1)
    balance_after = browser.find_elements_by_xpath("//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[1].text
    assert bal1 != bal2
    print(bal1)
    print(bal2)


def test_buy_offer_usdc_max_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    #time.sleep(1)
    #check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
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
    price = browser.find_element_by_xpath("//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'USDC 10 000.00'
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


def test_buy_offer_usdc_min_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    #time.sleep(1)
    #check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
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
    price = browser.find_element_by_xpath("//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'USDC 0.80'
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


def test_buy_offer_usdc_normal_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    #time.sleep(1)
    #check_box = browser.find_element_by_xpath("//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
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
    price = browser.find_element_by_xpath("//div[@class='HeaderItemCard_price__Ez0c7']").text
    assert price == 'USDC 9.99'
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


def test_create_offers_to_invalid_test():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
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
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('50')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    items_tab = browser.find_element_by_id('profileCollectionItems').click()
    time.sleep(3)
    items = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    items[1].click()
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
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('50')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)


def test_buy_usdc_offer_user_hasnt_kyc():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_VERIFICATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    trade = browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(3)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[1].click()
    time.sleep(1)
    buy_button = browser.find_element_by_xpath("//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    buy_button.click()
    time.sleep(1)
    error_message = browser.find_element_by_xpath("//div[@class='HeaderItemCard_tipError__A2roI']").text
    assert error_message == 'You need to top up your wallet to buy this nft'


def test_buy_xnl_offer_user_hasnt_kyc():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_VERIFICATION)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    trade = browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(3)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    time.sleep(1)
    buy_button = browser.find_element_by_xpath("//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    buy_button.click()
    time.sleep(1)
    error_message = browser.find_element_by_xpath("//div[@class='HeaderItemCard_tipError__A2roI']").text
    assert error_message == 'You need to top up your wallet to buy this nft'


def test_buy_usdc_offer_user_hasnt_money():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    trade = browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(3)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[1].click()
    time.sleep(1)
    buy_button = browser.find_element_by_xpath("//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    buy_button.click()
    time.sleep(1)
    error_message = browser.find_element_by_xpath("//div[@class='HeaderItemCard_tipError__A2roI']").text
    assert error_message == 'You need to top up your wallet to buy this nft'


def test_buy_xnl_offer_user_hasnt_money():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    trade = browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(3)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    time.sleep(1)
    buy_button = browser.find_element_by_xpath("//button[@class ='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    buy_button.click()
    time.sleep(1)
    error_message = browser.find_element_by_xpath("//div[@class='HeaderItemCard_tipError__A2roI']").text
    assert error_message == 'You need to top up your wallet to buy this nft'


def test_delete_test_offers():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS)
    time.sleep(1)
    input_chronicle_password = browser.find_element_by_xpath('//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    time.sleep(2)
    sign_in_button = browser.find_element_by_xpath(
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    my_collection = browser.find_elements_by_xpath("//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    time.sleep(1)
    listings_tab = browser.find_element_by_id('profileCollectionListings').click()
    time.sleep(1)
    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'stop listing']").click()
    time.sleep(1)
    browser.find_element_by_id('Delete_listing__delete_it').click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'view listings ']").click()
    time.sleep(2)

    offer = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'stop listing']").click()
    time.sleep(1)
    browser.find_element_by_id('Delete_listing__delete_it').click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'view listings ']")
    time.sleep(1)