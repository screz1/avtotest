from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
import re
from selenium.webdriver.support.color import Color
from driver import driver

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest110@gmail.com'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest3@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest1@ukr.net'


def test_create_new_offer_with_usdc():
    browser = driver
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
    market_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    time.sleep(1)
    next = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
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
    create = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    of = browser.find_elements_by_xpath(
        "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    time.sleep(1)


def test_edit_item_usdc_offer_on_market_place_screen():
    browser = driver
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
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[text() = 'manage']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'Change listing']").click()
    time.sleep(1)
    price_input = browser.find_element_by_id('price_trade_edit')
    price_input.clear()
    price_input.send_keys('18.88')
    time.sleep(1)
    creat_listings = browser.find_element_by_xpath("//*[text() = 'Create listing']").click()
    time.sleep(1)
    listing_created = browser.find_element_by_xpath("//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")
    time.sleep(1)


def test_edit_item_usdc_offer_on_listings_tab_screen():
    browser = driver
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
    browser.find_element_by_xpath("//*[text() = 'Change listing']").click()
    time.sleep(1)
    price_input = browser.find_element_by_id('price_trade_edit')
    price_input.clear()
    price_input.send_keys('15.22')
    time.sleep(1)
    creat_listings = browser.find_element_by_xpath("//*[text() = 'Create listing']").click()
    time.sleep(1)
    listing_created = browser.find_element_by_xpath("//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")
    time.sleep(1)


def test_delete_usdc_offer():
    browser = driver
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
    browser.find_element_by_xpath("//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_usdc_min_price():
    browser = driver
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
    market_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    time.sleep(1)
    next = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    time.sleep(3)
    carency_drop = browser.find_element_by_xpath("//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    time.sleep(1)
    usdc = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")
    usdc.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('0.80')
    time.sleep(1)
    servise = browser.find_elements_by_xpath("//span[@class='USDC']")
    servise_fee = servise[0].text
    youll_receive = servise[1].text
    print(servise_fee)
    print(youll_receive)
    create = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    of = browser.find_elements_by_xpath(
        "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    time.sleep(1)
    browser.find_element_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = '0.80']")
    browser.find_element_by_xpath("//*[text() = 'stop listing']").click()
    time.sleep(1)
    browser.find_element_by_id('Delete_listing__delete_it').click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_usdc_max_price():
    browser = driver
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
    market_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    time.sleep(1)
    next = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    time.sleep(3)
    carency_drop = browser.find_element_by_xpath("//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    time.sleep(1)
    usdc = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")
    usdc.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('10000')
    time.sleep(1)
    servise = browser.find_elements_by_xpath("//span[@class='USDC']")
    servise_fee = servise[0].text
    youll_receive = servise[1].text
    print(servise_fee)
    print(youll_receive)
    create = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    of = browser.find_elements_by_xpath(
        "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    time.sleep(1)
    browser.find_element_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = '10 000.00']")
    browser.find_element_by_xpath("//*[text() = 'stop listing']").click()
    time.sleep(1)
    browser.find_element_by_id('Delete_listing__delete_it').click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_xnl():
    browser = driver
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
    time.sleep(3)
    item = browser.find_element_by_xpath("//div[@class='HeaderItemCard_name__5EP5t']").text
    market_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    time.sleep(1)
    next = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    time.sleep(3)
    carency_drop = browser.find_element_by_xpath("//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    time.sleep(1)
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('9.99')
    time.sleep(1)
    create = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    of = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    time.sleep(1)


def test_edit_item_xnl_offer_on_market_place_screen():
    browser = driver
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
    time.sleep(2)
    pop_up_two_fa = browser.find_element_by_xpath(
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[text() = 'Trade']").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[text() = 'manage']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'Change listing']").click()
    time.sleep(1)
    price_input = browser.find_element_by_id('price_trade_edit')
    price_input.clear()
    price_input.send_keys('18.88')
    time.sleep(1)
    creat_listings = browser.find_element_by_xpath("//*[text() = 'Create listing']").click()
    time.sleep(1)
    listing_created = browser.find_element_by_xpath("//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")
    time.sleep(1)


def test_edit_item_xnl_offer_on_listings_tab_screen():
    browser = driver
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
    browser.find_element_by_xpath("//*[text() = 'Change listing']").click()
    time.sleep(1)
    price_input = browser.find_element_by_id('price_trade_edit')
    price_input.clear()
    price_input.send_keys('15.22')
    time.sleep(1)
    creat_listings = browser.find_element_by_xpath("//*[text() = 'Create listing']").click()
    time.sleep(1)
    listing_created = browser.find_element_by_xpath("//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")
    time.sleep(1)


def test_delete_xnl_offer():
    browser = driver
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
    browser.find_element_by_xpath("//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_xnl_min_price():
    browser = driver
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
    time.sleep(3)
    item = browser.find_element_by_xpath("//div[@class='HeaderItemCard_name__5EP5t']").text
    market_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    time.sleep(1)
    next = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    time.sleep(3)
    carency_drop = browser.find_element_by_xpath("//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    time.sleep(1)
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('0.80')
    time.sleep(1)
    create = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    of = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    time.sleep(1)
    browser.find_element_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = '0.80']")
    browser.find_element_by_xpath("//*[text() = 'stop listing']").click()
    time.sleep(1)
    browser.find_element_by_id('Delete_listing__delete_it').click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_xnl_max_price():
    browser = driver
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
    time.sleep(3)
    item = browser.find_element_by_xpath("//div[@class='HeaderItemCard_name__5EP5t']").text
    market_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    market_button.click()
    time.sleep(1)
    next = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next.click()
    time.sleep(3)
    carency_drop = browser.find_element_by_xpath("//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    time.sleep(1)
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('500000')
    time.sleep(1)
    create = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    of = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    time.sleep(1)
    browser.find_element_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = '500 000.00']")
    browser.find_element_by_xpath("//*[text() = 'stop listing']").click()
    time.sleep(1)
    browser.find_element_by_id('Delete_listing__delete_it').click()
    time.sleep(1)
    browser.find_element_by_xpath("//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_usd_less_than_min_price():
    browser = driver
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
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('0.79')
    time.sleep(1)
    rgb = browser.find_element_by_xpath("//span[@class='PriceInput_message__qVg36']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_new_offer_with_usd_more_than_max_price():
    browser = driver
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
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('10000.01')
    time.sleep(1)
    rgb = browser.find_element_by_xpath("//span[@class='PriceInput_message__qVg36']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_new_offer_with_usd_leave_price_field_empty():
    browser = driver
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
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_new_offer_with_xnl_less_than_min_price():
    browser = driver
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
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('0.79')
    time.sleep(1)
    rgb = browser.find_element_by_xpath("//span[@class='PriceInput_message__qVg36']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_new_offer_with_xnl_more_than_max_price():
    browser = driver
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
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('500000.01')
    time.sleep(1)
    rgb = browser.find_element_by_xpath("//span[@class='PriceInput_message__qVg36']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_usdc_offer_user_hasnt_kyc():
    browser = driver
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
    time.sleep(1)
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('50')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    error_pop = browser.find_element_by_xpath("//h4[@class='DublicateItemModal_title__diQ9H']").text
    assert error_pop == 'Pass KYC'
    text_pop = browser.find_element_by_xpath("//p[@class='DublicateItemModal_desc__dwoZM']").text
    assert text_pop == 'Sorry, you need to pass KYC to use following part of Chronicle'
    set_up_later_button = browser.find_element_by_id('Pass_KYC_SET_UP_LATER').click()
    time.sleep(1)
    create.click()
    time.sleep(1)
    set_up_button = browser.find_element_by_id('Pass_KYC_SET_UP').click()
    time.sleep(1)
    kyc_text = browser.find_element_by_xpath("//h3[@class='WalletComponets_title__kw_3n']").text
    assert kyc_text == 'PLEASE VERIFY YOUR IDENTITY'
    time.sleep(1)


def test_create_xnl_offer_user_hasnt_kyc():
    browser = driver
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
    xnl = browser.find_element_by_xpath("//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    time.sleep(1)
    price_input = browser.find_element_by_id('price_steps_modal').send_keys('50')
    time.sleep(1)
    create = browser.find_element_by_xpath(
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    time.sleep(1)
    error_pop = browser.find_element_by_xpath("//h4[@class='DublicateItemModal_title__diQ9H']").text
    assert error_pop == 'Pass KYC'
    text_pop = browser.find_element_by_xpath("//p[@class='DublicateItemModal_desc__dwoZM']").text
    assert text_pop == 'Sorry, you need to pass KYC to use following part of Chronicle'
    set_up_later_button = browser.find_element_by_id('Pass_KYC_SET_UP_LATER').click()
    time.sleep(1)
    create.click()
    time.sleep(1)
    set_up_button = browser.find_element_by_id('Pass_KYC_SET_UP').click()
    time.sleep(1)
    kyc_text = browser.find_element_by_xpath("//h3[@class='WalletComponets_title__kw_3n']").text
    assert kyc_text == 'PLEASE VERIFY YOUR IDENTITY'
    time.sleep(1)