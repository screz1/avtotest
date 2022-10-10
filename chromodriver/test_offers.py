from selenium import webdriver
import time
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest2@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest4@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES = 'chronicletest3@ukr.net'


def test_create_new_offer_with_usdc():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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

    servise = browser.find_elements(By.XPATH, "//span[@class='USDC']")
    servise_fee = servise[0].text
    youll_receive = servise[1].text
    print(servise_fee)
    print(youll_receive)
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    of = browser.find_elements(
        By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name


def test_edit_item_usdc_offer_on_market_place_screen():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Trade']")))
    browser.find_element(By.XPATH, "//*[text() = 'Trade']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'manage']")))
    browser.find_element(By.XPATH, "//*[text() = 'manage']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Change listing']")))
    browser.find_element(By.XPATH, "//*[text() = 'Change listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'price_trade_edit')))
    price_input = browser.find_element(By.ID, 'price_trade_edit')
    price_input.clear()
    price_input.send_keys('18.88')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create listing']")))
    creat_listings = browser.find_element(By.XPATH, "//*[text() = 'Create listing']")
    creat_listings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")))
    listing_created = browser.find_element(
        By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")
    listing_created.is_displayed()


def test_edit_item_usdc_offer_on_listings_tab_screen():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionListings')))
    listings_tab = browser.find_element(By.ID, 'profileCollectionListings')
    listings_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Change listing']")))
    browser.find_element(By.XPATH, "//*[text() = 'Change listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'price_trade_edit')))
    price_input = browser.find_element(By.ID, 'price_trade_edit')
    price_input.clear()
    price_input.send_keys('15.22')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create listing']")))
    creat_listings = browser.find_element(By.XPATH, "//*[text() = 'Create listing']")
    creat_listings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")))
    listing_created = browser.find_element(
        By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")
    listing_created.is_displayed()


def test_delete_usdc_offer():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Market']")))
    browser.find_element(By.XPATH, "//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_usdc_min_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    price_input.send_keys('0.80')

    servise = browser.find_elements(By.XPATH, "//span[@class='USDC']")
    servise_fee = servise[0].text
    youll_receive = servise[1].text
    print(servise_fee)
    print(youll_receive)
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    of = browser.find_elements(
        By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    browser.find_element(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = '0.80']")))
    browser.find_element(By.XPATH, "//*[text() = '0.80']")
    browser.find_element(By.XPATH, "//*[text() = 'stop listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Delete_listing__delete_it')))
    browser.find_element(By.ID, 'Delete_listing__delete_it').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Market']")))
    browser.find_element(By.XPATH, "//*[text() = 'Market']")


def test_create_new_offer_with_usdc_max_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    price_input.send_keys('10000')

    servise = browser.find_elements(By.XPATH, "//span[@class='USDC']")
    servise_fee = servise[0].text
    youll_receive = servise[1].text
    print(servise_fee)
    print(youll_receive)
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    of = browser.find_elements(
        By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    browser.find_element(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = '10 000.00']")))
    browser.find_element(By.XPATH, "//*[text() = '10 000.00']")
    browser.find_element(By.XPATH, "//*[text() = 'stop listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Delete_listing__delete_it')))
    browser.find_element(By.ID, 'Delete_listing__delete_it').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Market']")))
    browser.find_element(By.XPATH, "//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_xnl():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('9.99')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    of = browser.find_elements(
        By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    time.sleep(1)


def test_edit_item_xnl_offer_on_market_place_screen():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Trade']")))
    browser.find_element(By.XPATH, "//*[text() = 'Trade']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'manage']")))
    browser.find_element(By.XPATH, "//*[text() = 'manage']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Change listing']")))
    browser.find_element(By.XPATH, "//*[text() = 'Change listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'price_trade_edit')))
    price_input = browser.find_element(By.ID, 'price_trade_edit')
    price_input.clear()
    price_input.send_keys('18.88')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create listing']")))
    creat_listings = browser.find_element(By.XPATH, "//*[text() = 'Create listing']")
    creat_listings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")))
    listing_created = browser.find_element(
        By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")
    listing_created.is_displayed()
    time.sleep(1)


def test_edit_item_xnl_offer_on_listings_tab_screen():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionListings')))
    listings_tab = browser.find_element(By.ID, 'profileCollectionListings')
    listings_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    offer = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    offer[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Change listing']")))
    browser.find_element(By.XPATH, "//*[text() = 'Change listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'price_trade_edit')))
    price_input = browser.find_element(By.ID, 'price_trade_edit')
    price_input.clear()
    price_input.send_keys('15.22')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create listing']")))
    creat_listings = browser.find_element(By.XPATH, "//*[text() = 'Create listing']")
    creat_listings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")))
    listing_created = browser.find_element(
        By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")
    listing_created.is_displayed()
    time.sleep(1)


def test_delete_xnl_offer():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Market']")))
    browser.find_element(By.XPATH, "//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_xnl_min_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('0.80')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    of = browser.find_elements(
        By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    browser.find_element(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = '0.80']")))
    browser.find_element(By.XPATH, "//*[text() = '0.80']")
    browser.find_element(By.XPATH, "//*[text() = 'stop listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Delete_listing__delete_it')))
    browser.find_element(By.ID, 'Delete_listing__delete_it').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Market']")))
    browser.find_element(By.XPATH, "//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_xnl_max_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('500000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    of = browser.find_elements(
        By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert item == offer_name
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    browser.find_element(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = '500 000.00']")))
    browser.find_element(By.XPATH, "//*[text() = '500 000.00']")
    browser.find_element(By.XPATH, "//*[text() = 'stop listing']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Delete_listing__delete_it')))
    browser.find_element(By.ID, 'Delete_listing__delete_it').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Market']")))
    browser.find_element(By.XPATH, "//*[text() = 'Market']")
    time.sleep(1)


def test_create_new_offer_with_usd_less_than_min_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    price_input.send_keys('0.79')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='PriceInput_message__qVg36']")))
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__qVg36']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_new_offer_with_usd_more_than_max_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    price_input.send_keys('10000.01')
    time.sleep(1)
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__qVg36']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_new_offer_with_usd_leave_price_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")))
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_new_offer_with_xnl_less_than_min_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('0.79')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='PriceInput_message__qVg36']")))
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__qVg36']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_new_offer_with_xnl_more_than_max_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES)

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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('500000.01')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='PriceInput_message__qVg36']")))
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__qVg36']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    create = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF Button_disable__0XBGJ']")
    create.click()
    time.sleep(1)


def test_create_usdc_offer_user_hasnt_kyc():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
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
    wait.until(ec.visibility_of_element_located((By.ID, 'price_steps_modal')))
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('50')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h4[@class='DublicateItemModal_title__diQ9H']")))
    error_pop = browser.find_element(By.XPATH, "//h4[@class='DublicateItemModal_title__diQ9H']").text
    assert error_pop == 'Pass KYC'
    text_pop = browser.find_element(By.XPATH, "//p[@class='DublicateItemModal_desc__dwoZM']").text
    assert text_pop == 'Sorry, you need to pass KYC to use following part of Chronicle'
    set_up_later_button = browser.find_element(By.ID, 'Pass_KYC_SET_UP_LATER')
    set_up_later_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Pass_KYC_SET_UP')))
    set_up_button = browser.find_element(By.ID, 'Pass_KYC_SET_UP')
    set_up_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h3[@class='WalletComponets_title__kw_3n']")))
    kyc_text = browser.find_element(By.XPATH, "//h3[@class='WalletComponets_title__kw_3n']").text
    assert kyc_text == 'PLEASE VERIFY YOUR IDENTITY'
    time.sleep(1)


def test_create_xnl_offer_user_hasnt_kyc():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    xnl = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    xnl.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'price_steps_modal')))
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('50')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h4[@class='DublicateItemModal_title__diQ9H']")))
    error_pop = browser.find_element(By.XPATH, "//h4[@class='DublicateItemModal_title__diQ9H']").text
    assert error_pop == 'Pass KYC'
    text_pop = browser.find_element(By.XPATH, "//p[@class='DublicateItemModal_desc__dwoZM']").text
    assert text_pop == 'Sorry, you need to pass KYC to use following part of Chronicle'
    set_up_later_button = browser.find_element(By.ID, 'Pass_KYC_SET_UP_LATER')
    set_up_later_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    create.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Pass_KYC_SET_UP')))
    set_up_button = browser.find_element(By.ID, 'Pass_KYC_SET_UP')
    set_up_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h3[@class='WalletComponets_title__kw_3n']")))
    kyc_text = browser.find_element(By.XPATH, "//h3[@class='WalletComponets_title__kw_3n']").text
    assert kyc_text == 'PLEASE VERIFY YOUR IDENTITY'
    time.sleep(1)