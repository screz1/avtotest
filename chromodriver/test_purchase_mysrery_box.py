from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest101@gmail.com'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_WITHOUT_MONEY = 'chronicletest1@ukr.net'
USER_WITH_EMAIL_AND_KYC_VERIFICATION_FOR_SALES = 'chronicletest5@ukr.net'


CARD = '  4242 4242 4242 4242  12 24  123  58000 '
INVALID_CARD = '  4200 0000 0000 0000  12 24  123  58000 '


def test_buy_usdc_mystery_box_with_wallet():
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
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[0].text
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='MysteryBoxPrice_value__Mg8SM']")))
    price = browser.find_element(By.XPATH, "//div[@class='MysteryBoxPrice_value__Mg8SM']").text
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    wallet_tab = browser.find_element(By.ID, 'confirmBoughtwallet')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    pay_now = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now[1].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congrat = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_after = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    assert bal1 != bal2


def test_buy_usdc_mystery_box_with_stripe():
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
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[0].text
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='MysteryBoxPrice_value__Mg8SM']")))
    price = browser.find_element(By.XPATH, "//div[@class='MysteryBoxPrice_value__Mg8SM']").text
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtpay with card')))
    card_tab = browser.find_element(By.ID, 'confirmBoughtpay with card')
    card_tab.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@class="__PrivateStripeElement-input"]')))
    card_number_input = browser.find_element(By.XPATH, '//input[@class="__PrivateStripeElement-input"]')
    card_number_input.send_keys(CARD)
    wait.until(ec.visibility_of_element_located((By.NAME, 'Save for future payments')))
    save_card = browser.find_element(By.NAME, 'Save for future payments')
    save_card.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    pay_now = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    time.sleep(1)


def test_buy_usdc_mystery_box_with_stripe_saved_card():
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
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtmy saved cards')))
    saved_card_tab = browser.find_element(By.ID, 'confirmBoughtmy saved cards')
    saved_card_tab.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    pay_now = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations= browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    time.sleep(1)


def test_buy_xnl_mystery_box_with_wallet():
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
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    wallet_tab = browser.find_element(By.ID, 'confirmBoughtwallet')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    pay_now = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    pay_now[1].click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congrat = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congrat == "Congratulations ... it's yours!"
    time.sleep(1)


def test_buy_usdc_mystery_box_with_wallet_user_have_not_money():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    wallet_tab = browser.find_element(By.ID, 'confirmBoughtwallet')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    pay_now = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    nevermind = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    nevermind.click()
    time.sleep(1)


def test_buy_xnl_mystery_box_with_wallet_user_have_not_money():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    wallet_tab = browser.find_element(By.ID, 'confirmBoughtwallet')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    pay_now = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    never_mind = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    never_mind.click()
    time.sleep(1)


def test_buy_usdc_mystery_box_with_wallet_user_not_avtorise_sign_in_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'Logo_min__TBvKP')))
    browser.find_element(By.CLASS_NAME, 'Logo_min__TBvKP').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Header_links__EHO60']")))
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    sign_in = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    sign_in[1].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.is_displayed()
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.is_displayed()
    time.sleep(1)


def test_buy_usdc_mystery_box_with_wallet_user_not_avtorise_register_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'Logo_min__TBvKP')))
    browser.find_element(By.CLASS_NAME, 'Logo_min__TBvKP').click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Header_links__EHO60']")))
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//*[text() = 'register']")))
    register = browser.find_element(
        By.XPATH, "//*[text() = 'register']")

    register.click()
    wait.until(ec.visibility_of_element_located((By.NAME, "email")))
    email_input = browser.find_element(By.NAME, "email")
    email_input.is_displayed()
    password_input = browser.find_element(By.NAME, "password")
    password_input.is_displayed()


def test_buy_usdc_mystery_box_with_wallet_user_have_not_kyc():
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
    pop_up_two_fa = browser.find_element(By.XPATH, "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1000)")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    details = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    details[1].click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")))
    try_your_luck = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL MysteryBoxPrice_btn__05O7g MysteryBoxPrice_fullBtn__kdDyC']")
    try_your_luck[0].click()
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    wallet_tab = browser.find_element(By.ID, 'confirmBoughtwallet')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    pay_now = browser.find_elements(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    pay_now[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_link__x13mQ']")))
    set_up_wallet = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_link__x13mQ']")
    set_up_wallet.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='first_name']")))
    first_name_input = browser.find_element(By.XPATH, "//input[@name='first_name']")
    first_name_input.is_displayed()
    last_name_input = browser.find_element(By.XPATH, "//input[@name='last_name']")
    last_name_input.is_displayed()
    try:
        birthday_input = browser.find_element(By.XPATH, "//input[@placeholder='DD/MM/YYYY']")
        if birthday_input.is_displayed():
            print("...")
    except NoSuchElementException:
        print("...")
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']//h5[@class='CustomSelect_label__e7_op']")
    country_drop.click()
    city_input = browser.find_element(By.XPATH, "//input[@name='city']")
    city_input.is_displayed()
    address_line_one_input = browser.find_element(By.XPATH, "//input[@name='line1']")
    address_line_one_input.is_displayed()
    address_line_two_input = browser.find_element(By.XPATH, "//input[@name='line2']")
    address_line_two_input.is_displayed()
    province_input = browser.find_element(By.XPATH, "//input[@name='district']")
    province_input.is_displayed()
    zip_code_input = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    zip_code_input.is_displayed()
    time.sleep(1)

