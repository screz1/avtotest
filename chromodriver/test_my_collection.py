from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest2@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest4@ukr.net'


def test_check_album_screen():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionAlbums')))
    album_tab = browser.find_element(By.ID, 'profileCollectionAlbums')
    album_tab.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")))
    album_mame = browser.find_elements(
        By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements(By.XPATH, "//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']")))
    collections_name = browser.find_element(By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name


def test_check_album_screen_item_screen():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionAlbums')))
    album_tab = browser.find_element(By.ID, 'profileCollectionAlbums')
    album_tab.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")))
    album_mame = browser.find_elements(
        By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements(By.XPATH, "//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']")))
    collections_name = browser.find_element(By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    item_name_on_screen = browser.find_elements(
        By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    item_name = item_name_on_screen[0].text
    item = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    item[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_header__3K45m']")))
    item_name_on_item_screen = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_header__3K45m']").text
    assert item_name == item_name_on_item_screen
    ip = browser.find_elements(By.XPATH, "//div[@class='DetailRow_value__vq2Oj']")
    ip_owner = ip[0].text
    assert ip_owner is not None
    fr = browser.find_elements(By.XPATH, "//div[@class='DetailRow_value__vq2Oj']")
    franchise = ip[1].text
    assert franchise is not None
    collection = browser.find_element(
        By.XPATH, "//a[@class='Button_btn__JyuE1 Button_link__x13mQ Button_withIcon__1TgpF']").text
    assert collection is not None
    collectible = ip[2].text
    assert collectible is not None
    rarity = ip[3].text
    assert rarity is not None
    your_unique_number = ip[4].text
    assert your_unique_number is not None
    link = browser.find_elements(By.XPATH, "//div[@class='DetailInfo_detailLink__LRPg9']")
    transaction_number = link[0].text
    assert transaction_number != 'Waiting for Token ID'
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='DetailInfo_detailLink__LRPg9']")))
    item_purchases = browser.find_element(By.XPATH, "//div[@class='DetailInfo_detailLink__LRPg9']").text
    assert item_purchases is not None
    item_type = ip[5].text
    assert item_type is not None


def test_check_album_screen_item_screen_view_listings_button():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionAlbums')))
    album_tab = browser.find_element(By.ID, 'profileCollectionAlbums')
    album_tab.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")))
    album_mame = browser.find_elements(
        By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements(By.XPATH, "//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']")))
    collections_name = browser.find_element(By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    item_name_on_screen = browser.find_elements(
        By.XPATH,
        "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    item_name = item_name_on_screen[0].text
    item = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    item[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    buttons = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    buttons[0].click()
    time.sleep(2)
    try:
        item_on_mp = browser.find_element(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
        if item_on_mp.is_displayed():
            item_on_mp.click()
            print("item")
    except NoSuchElementException:
        print("Item not Found")
        message = browser.find_element(By.XPATH, "//h3[@class='NotFoundItem_header__SXhtQ']").text
        assert message == 'You have no active listings yet'
        print(message)
    time.sleep(1)


def test_check_album_screen_item_screen_view_withdraw_button():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionAlbums')))
    album_tab = browser.find_element(By.ID, 'profileCollectionAlbums')
    album_tab.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")))
    album_mame = browser.find_elements(
        By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements(By.XPATH, "//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']")))
    collections_name = browser.find_element(By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    item_name_on_screen = browser.find_elements(
        By.XPATH,
        "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    item_name = item_name_on_screen[0].text
    item = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    item[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    buttons = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    buttons[1].click()
    time.sleep(2)
    try:
        pop_up = browser.find_element(By.XPATH, "//div[@class='DublicateItemModal_top__fx00z']")
        if pop_up.is_displayed():
            set_up_button = browser.find_element(By.ID, 'Verify_your_number_SET_UP')
            set_up_button.click()
            time.sleep(2)
            number_verify_page = browser.find_element(By.XPATH, "//div[@class='VerifyPhoneModal_header__2KkM7']").text
            assert number_verify_page == 'Verify phone number'
            print("Verify")
    except NoSuchElementException:
        print("Item not Found")
        message = browser.find_element(By.XPATH, "//h3[@class='NotFoundItem_header__SXhtQ']").text
        assert message == 'You have no active listings yet'
        print(message)
    time.sleep(1)


def test_check_album_screen_item_screen_view_market_button():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'profileCollectionAlbums')))
    album_tab = browser.find_element(By.ID, 'profileCollectionAlbums')
    album_tab.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")))
    album_mame = browser.find_elements(
        By.XPATH, "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements(By.XPATH, "//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']")))
    collections_name = browser.find_element(By.XPATH, "//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    item_name_on_screen = browser.find_elements(
        By.XPATH,
        "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    item_name = item_name_on_screen[0].text
    item = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    item[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    buttons = browser.find_elements(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    buttons[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='TradeStepsModal_desc__D1IJK']")))
    message = browser.find_element(By.XPATH, "//p[@class='TradeStepsModal_desc__D1IJK']").text
    assert message == 'Select a copy which you want to sell or trade'
    print(message)
    time.sleep(1)

