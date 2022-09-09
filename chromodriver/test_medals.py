from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
import re
from selenium.webdriver.support.color import Color
from driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://dev.xnl.zpoken.io/login'
URL_ADMIN = 'https://dev-admin.xnl.zpoken.io/'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest103@gmail.com'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'
USER_WITH_EMAIL_AND_KYC_FOR_CREATE_OFFERS = 'chronicletest1@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest3@ukr.net'


def test_user_buy_medal_on_mystery_box_valid_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")))
    check_box = browser.find_element(By.XPATH,
                                     "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
                                          "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    time.sleep(2)
    pop_up_two_fa = browser.find_element(By.XPATH,
                                         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Chronicle medals']")))
    chronicle_medals = browser.find_element(By.XPATH, "//*[text() = 'Chronicle medals']")
    chronicle_medals.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    time.sleep(1)
    try_your_luck_button.click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    pay_now_button = browser.find_elements(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now_button[1].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"


def test_user_equip_bronze_medal_valid_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")))
    check_box = browser.find_element(By.XPATH,
                                     "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
                                          "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    time.sleep(2)
    pop_up_two_fa = browser.find_element(By.XPATH,
                                         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, "profileCollectionMedals")))
    medals_tab = browser.find_element(By.ID, "profileCollectionMedals")
    medals_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    medal = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    medal[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_name__5EP5t']")))
    what_is_medal = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_name__5EP5t']").text

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    equip_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    equip_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")))
    de_equip_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")

    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_medal__x5b6w']")))
    equipped_medal = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_medal__x5b6w']//img[@decoding='async']")
    equipped_medal.get_attribute("alt")
    med = equipped_medal.get_attribute("alt")

    assert what_is_medal == med


def test_user_de_equip_medal_valid_data():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")))
    check_box = browser.find_element(By.XPATH,
                                     "//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    check_box.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
                                          "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    time.sleep(2)
    pop_up_two_fa = browser.find_element(By.XPATH,
                                         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, "profileCollectionMedals")))
    medals_tab = browser.find_element(By.ID, "profileCollectionMedals")
    medals_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    medal = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    medal[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_name__5EP5t']")))
    what_is_medal = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_name__5EP5t']").text
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_medal__x5b6w']")))
    equipped_medal = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_medal__x5b6w']//img[@decoding='async']")
    equipped_medal.get_attribute("alt")
    med = equipped_medal.get_attribute("alt")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")))
    de_equip_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 Button_withIcon__1TgpF']")
    de_equip_button.click()
    time.sleep(2)
    try:
        equipped_medal = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_medal__x5b6w']//img[@decoding='async']")
        if equipped_medal.is_displayed():
            print("bad")
            return False
    except NoSuchElementException:
        print("good")
        return True


def test_user_merge_silver_medal():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    #wait.until(ec.visibility_of_element_located((By.XPATH,"//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")))
    #check_box = browser.find_element(By.XPATH,"//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
                                          "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    time.sleep(2)
    pop_up_two_fa = browser.find_element(By.XPATH,
                                         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, "profileCollectionMedals")))
    medals_tab = browser.find_element(By.ID, "profileCollectionMedals")
    medals_tab.click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MedalsCollection_btn__QalVk Button_withIcon__1TgpF']")))
    merge_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MedalsCollection_btn__QalVk Button_withIcon__1TgpF']")
    merge_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Merge_medal__O1KDH']")))
    medals_for_merge = browser.find_elements(By.XPATH, "//div[@class='Merge_medal__O1KDH']")
    silver_medal = medals_for_merge[0]
    silver_medal.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Merge_btn__e3Yfr Button_withIcon__1TgpF']")))
    craft_medal_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Merge_btn__e3Yfr Button_withIcon__1TgpF']")
    craft_medal_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, "Merge_medals__Merge_medals")))
    merge_medal_button = browser.find_element(By.ID, "Merge_medals__Merge_medals")
    merge_medal_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"


def test_user_create_medal_offer_for_usdc():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")
    #wait.until(ec.visibility_of_element_located((By.XPATH,"//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")))
    #check_box = browser.find_element(By.XPATH,"//div[@class='LoginForm_input__ZZfRr LoginForm_checkbox__KEUgt']//label[@class='Input_checkbox__cuH_e']")
    #check_box.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
                                          "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    time.sleep(2)
    pop_up_two_fa = browser.find_element(By.XPATH,
                                         "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='Dropdown_link__FcCSx']")))
    my_collection = browser.find_elements(By.XPATH, "//a[@class='Dropdown_link__FcCSx']")
    my_collection[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, "profileCollectionMedals")))
    medals_tab = browser.find_element(By.ID, "profileCollectionMedals")
    medals_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")))
    medal = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_card__c0a2s']")
    medal[1].click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='HeaderItemCard_name__5EP5t']")))
    what_is_medal = browser.find_element(By.XPATH, "//div[@class='HeaderItemCard_name__5EP5t']").text

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    put_on_sale_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    put_on_sale_button.click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")))
    next_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    next_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")))
    carency_drop = browser.find_element(By.XPATH, "//h5[@class='CustomSelect_label__e7_op USDC']")
    carency_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")))
    usdc = browser.find_element(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv CustomSelect_checked__LYhDC']")
    usdc.click()
    price_input = browser.find_element(By.ID, 'price_steps_modal')
    price_input.send_keys('9.99')
    create = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL TradeStepsModal_btnIcon__6t66Z Button_withIcon__1TgpF']")
    create.click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")))
    of = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_header__gNIR8 FeaturesCardList_lineText__Qt65n']")
    offer_name = of[0].text
    assert what_is_medal == offer_name
    time.sleep(1)