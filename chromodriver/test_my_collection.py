from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from driver import driver

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest2@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest4@ukr.net'


def test_check_album_screen():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    my_collection = browser.find_elements_by_xpath("//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    time.sleep(1)
    album_tab = browser.find_element_by_id('profileCollectionAlbums').click()
    time.sleep(1)
    album_mame = browser.find_elements_by_xpath("//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements_by_xpath("//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    time.sleep(3)
    collections_name = browser.find_element_by_xpath("//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name


def test_check_album_screen_item_screen():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    my_collection = browser.find_elements_by_xpath("//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    time.sleep(1)
    album_tab = browser.find_element_by_id('profileCollectionAlbums').click()
    time.sleep(1)
    album_mame = browser.find_elements_by_xpath(
        "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements_by_xpath("//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    time.sleep(3)
    collections_name = browser.find_element_by_xpath("//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name
    time.sleep(2)
    item_name_on_screen = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    item_name = item_name_on_screen[0].text
    item = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    item[0].click()
    time.sleep(2)
    item_name_on_item_screen = browser.find_element_by_xpath("//div[@class='HeaderItemCard_header__3K45m']").text
    assert item_name == item_name_on_item_screen
    ip = browser.find_elements_by_xpath("//div[@class='DetailRow_value__vq2Oj']")
    ip_owner = ip[0].text
    assert ip_owner != None
    fr = browser.find_elements_by_xpath("//div[@class='DetailRow_value__vq2Oj']")
    franchise = ip[1].text
    assert franchise != None
    collection = browser.find_element_by_xpath("//a[@class='Button_btn__JyuE1 Button_link__x13mQ Button_withIcon__1TgpF']").text
    assert collection != None
    collectible = ip[2].text
    assert collectible != None
    rarity = ip[3].text
    assert rarity != None
    your_unique_number = ip[4].text
    assert your_unique_number != None
    link = browser.find_elements_by_xpath("//div[@class='DetailInfo_detailLink__LRPg9']")
    transaction_number = link[0].text
    assert transaction_number != 'Waiting for Token ID'
    item_purchases = link[1].text
    assert item_purchases != None
    item_type = ip[5].text
    assert item_type != None


def test_check_album_screen_item_screen_view_listings_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    my_collection = browser.find_elements_by_xpath("//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    time.sleep(1)
    album_tab = browser.find_element_by_id('profileCollectionAlbums').click()
    time.sleep(1)
    album_mame = browser.find_elements_by_xpath(
        "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements_by_xpath("//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    time.sleep(3)
    collections_name = browser.find_element_by_xpath("//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name
    time.sleep(2)
    item_name_on_screen = browser.find_elements_by_xpath(
        "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    item_name = item_name_on_screen[0].text
    item = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    item[0].click()
    time.sleep(2)
    buttons = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    buttons[0].click()
    time.sleep(2)
    try:
        item_on_mp = browser.find_element_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
        if item_on_mp.is_displayed():
            item_on_mp.click()
            print("item")
    except NoSuchElementException:
        print("Item not Found")
        message = browser.find_element_by_xpath("//h3[@class='NotFoundItem_header__SXhtQ']").text
        assert message == 'You have no active listings yet'
        print(message)
    time.sleep(1)


def test_check_album_screen_item_screen_view_withdraw_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    my_collection = browser.find_elements_by_xpath("//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    time.sleep(1)
    album_tab = browser.find_element_by_id('profileCollectionAlbums').click()
    time.sleep(1)
    album_mame = browser.find_elements_by_xpath(
        "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements_by_xpath("//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    time.sleep(3)
    collections_name = browser.find_element_by_xpath("//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name
    time.sleep(2)
    item_name_on_screen = browser.find_elements_by_xpath(
        "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    item_name = item_name_on_screen[0].text
    item = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    item[0].click()
    time.sleep(2)
    buttons = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    buttons[1].click()
    time.sleep(2)
    try:
        pop_up = browser.find_element_by_xpath("//div[@class='DublicateItemModal_top__fx00z']")
        if pop_up.is_displayed():
            set_up_button = browser.find_element_by_id('Verify_your_number_SET_UP')
            set_up_button.click()
            time.sleep(2)
            number_verify_page = browser.find_element_by_xpath("//div[@class='VerifyPhoneModal_header__2KkM7']").text
            assert number_verify_page == 'Verify phone number'
            print("Verify")
    except NoSuchElementException:
        print("Item not Found")
        message = browser.find_element_by_xpath("//h3[@class='NotFoundItem_header__SXhtQ']").text
        assert message == 'You have no active listings yet'
        print(message)
    time.sleep(1)


def test_check_album_screen_item_screen_view_market_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
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
    time.sleep(3)
    user_drop = browser.find_element_by_xpath("//div[@class='UserHeaderCard_dropdownBtn__eXCOo']").click()
    time.sleep(1)
    my_collection = browser.find_elements_by_xpath("//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    time.sleep(1)
    album_tab = browser.find_element_by_id('profileCollectionAlbums').click()
    time.sleep(1)
    album_mame = browser.find_elements_by_xpath(
        "//div[@class='CollectionCardList_header__GyzhH CollectionCardList_text__abUZ4']")
    album = album_mame[0].text
    albums = browser.find_elements_by_xpath("//div[@class='CollectionCardList_card__3TwI5 undefined']")
    albums[0].click()
    time.sleep(3)
    collections_name = browser.find_element_by_xpath("//div[@class='CollectionDetail_nav2__96nT8']").text
    assert album == collections_name
    time.sleep(2)
    item_name_on_screen = browser.find_elements_by_xpath(
        "//div[@class='FeaturesCardList_card__c0a2s']//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    item_name = item_name_on_screen[0].text
    item = browser.find_elements_by_xpath("//div[@class='FeaturesCardList_card__c0a2s']")
    item[0].click()
    time.sleep(2)
    buttons = browser.find_elements_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    buttons[0].click()
    time.sleep(2)
    message = browser.find_element_by_xpath("//p[@class='TradeStepsModal_desc__D1IJK']").text
    assert message == 'Select a copy which you want to sell or trade'
    print(message)
    time.sleep(1)

