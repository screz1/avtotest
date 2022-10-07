from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest4@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'


def test_purchase_with_usd_wallet_card():
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
        (By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[3].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")))
    items_for_purchase_usd = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    items_for_purchase_usd[2].click()
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


def test_purchase_with_usd_wallet_card_invalid_user():
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
        (By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[4].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")))
    items_for_purchase_usd = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    items_for_purchase_usd[2].click()
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
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    pay_now_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now_button.is_displayed()
    wait.until(ec.visibility_of_element_located((By.XPATH, 'confirmBoughtwallet')))
    set_up_button = browser.find_elements(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_link__x13mQ']")
    set_up_button[1].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")))
    verify_text = browser.find_element(By.XPATH, "//h3[@class='WalletComponets_title__kw_3n']").text
    assert verify_text == 'PLEASE VERIFY YOUR IDENTITY'


def test_purchase_user_not_avtorize():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get('https://dev.xnl.zpoken.io/store')
    wait = WebDriverWait(browser, 15, 0.3)

    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[4].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")))
    items_for_purchase_usd = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    items_for_purchase_usd[2].click()
    time.sleep(2)
    try:
        buy_anyway_button = browser.find_element(By.ID, 'Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    back_to_store = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    back_to_store.click()


def test_purchase_with_usd_wallet_card_user_has_not_enough_usd():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(USER_WITH_EMAIL_AND_KYC_VERIFICATION)
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[4].click()
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
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    pay_now_button = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now_button[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    never_mind_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    never_mind_button.click()
