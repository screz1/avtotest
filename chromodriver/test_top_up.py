from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from driver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

STAGE_URL = 'https://stage.xnl.zpoken.io/login'
DEV_URL = 'https://dev.xnl.zpoken.io/login'
URL = 'https://stage.xnl.zpoken.io/login'
USER_WITH_EMAIL_VERIFICATION = 'chronicletest110@gmail.com'
USER_WITH_EMAIL_AND_KYC_VERIFICATION = 'chronicletest5@ukr.net'


def test_top_up_usdc_use_valid_data_with_fiat():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")))
    balance_before = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal1 = balance_before[0].text
    print(bal1)

    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    sum = 100
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys(sum)
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[1].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    deposit_funds.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')))
    top_up = browser.find_element(By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')
    top_up.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']")))
    cong = browser.find_element(By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']").text
    assert cong == 'Your transaction was successful'
    back_to_store = browser.find_element(
        By.XPATH, "//a[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    back_to_store.click()
    time.sleep(5)
    balance_after = browser.find_elements(By.XPATH, "//span[@class='UserHeaderCard_value__zgpGT']")
    bal2 = balance_after[0].text
    # bal3 = int(bal2) - sum
    print(bal1)
    assert float(bal1) == float(bal2) - sum
    time.sleep(5)


def test_top_up_usdc_use_valid_data_with_fiat_check_nevermind_button():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    deposit_funds.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Are_you_sure_you_want_to_make_a_top_up__nevermind')))
    never_mind = browser.find_element(By.ID, 'Are_you_sure_you_want_to_make_a_top_up__nevermind')
    never_mind.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    back_button = browser.find_elements(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    back_button[2].click()
    time.sleep(1)


def test_top_up_usdc_use_valid_data_with_fiat_user_leave_address_line2_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    deposit_funds.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')))
    top_up = browser.find_element(By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')
    top_up.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']")))
    cong = browser.find_element(By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']").text
    assert cong == 'Your transaction was successful'
    back_to_store = browser.find_element(
        By.XPATH, "//a[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    back_to_store.click()
    time.sleep(5)


def test_top_up_usdc_use_valid_data_min_deposit_with_fiat():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('0.80')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    deposit_funds.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')))
    top_up = browser.find_element(By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')
    top_up.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']")))
    cong = browser.find_element(By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']").text
    assert cong == 'Your transaction was successful'
    back_to_store = browser.find_element(
        By.XPATH, "//a[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    back_to_store.click()
    browser.quit()


def test_top_up_usdc_use_valid_data_max_deposit_with_fiat():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('3000')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    deposit_funds.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')))
    top_up = browser.find_element(By.ID, 'Are_you_sure_you_want_to_make_a_top_up__top_up')
    top_up.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']")))
    cong = browser.find_element(By.XPATH, "//p[@class='__3dsecure_smallText__V9LrF']").text
    assert cong == 'Your transaction was successful'
    back_to_store = browser.find_element(
        By.XPATH, "//a[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    back_to_store.click()
    browser.quit()


def test_top_up_usdc_use_invalid_data_more_than_max_deposit_with_fiat():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('3000.01')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PriceInput_tipError__I0RRi']")))
    error = browser.find_element(By.XPATH, "//div[@class='PriceInput_tipError__I0RRi']").text
    assert error == 'Should be 3 000 USDC or less'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()

    browser.close()


def test_top_up_usdc_use_invalid_data_less_than_min_deposit_with_fiat():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('0.79')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PriceInput_tipError__I0RRi']")))
    error = browser.find_element(By.XPATH, "//div[@class='PriceInput_tipError__I0RRi']").text
    assert error == 'Should be 0.8 USDC or bigger'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()

    browser.close()


def test_top_up_usdc_use_invalid_data_lost_deposit_field_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('Name Surname')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PriceInput_tipError__I0RRi']")))
    error = browser.find_element(By.XPATH, "//div[@class='PriceInput_tipError__I0RRi']").text
    assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()

    browser.close()


def test_top_up_usdc_use_invalid_data_deposit_field_not_correct():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('-10')
    amount.get_property('value')
    print(amount.get_property('value'))
    assert amount.get_property('value') == '10'


def test_top_up_usdc_use_invalid_data_deposit_field_using_symbols():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('qwerty')
    amount.get_property('value')
    print(amount.get_property('value'))
    assert amount.get_property('value') == ''


def test_top_up_usdc_use_invalid_data_lost_card_holder_field_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200 0000 0000 0000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    time.sleep(1)
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()

    browser.close()


def test_top_up_usdc_use_invalid_data_lost_card_number_field_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    time.sleep(1)
    #error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    #assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    time.sleep(1)
    browser.close()


def test_top_up_usdc_use_invalid_data_fill_card_number_field_not_full():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('420000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    time.sleep(1)
    #error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    #assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    time.sleep(1)
    browser.close()


def test_top_up_usdc_use_invalid_data_card_number_field_using_symbols():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='cardnumber']")))
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('')
    card_number.get_property('value')
    print(card_number.get_property('value'))
    assert card_number.get_property('value') == ''


def test_top_up_usdc_use_invalid_data_lost_mm_yy_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    time.sleep(1)
    #error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    #assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    browser.close()


def test_top_up_usdc_use_invalid_data_fill_mm_yy_field_not_full():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('4200000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('12')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    time.sleep(1)
    #error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    #assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    browser.close()


def test_top_up_usdc_use_invalid_data_mm_yy_field_using_symbols():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='expiry']")))
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('qwerty')
    mm_yy.get_property('value')
    print(mm_yy.get_property('value'))
    assert mm_yy.get_property('value') == ''


def test_top_up_usdc_use_invalid_data_lost_cvc_field_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('42000000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('')
    country_drop = browser.find_element(
        By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    time.sleep(1)
    #error = browser.find_element_by_xpath("//div[@class='Input_tipError__CKiEf']").text
    #assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    browser.close()


def test_top_up_usdc_use_invalid_data_cvc_field_using_symbols():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='cvc']")))
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('qwerty')
    cvc.get_property('value')
    print(cvc.get_property('value'))
    assert cvc.get_property('value') == ''


def test_top_up_usdc_use_invalid_data_country_not_selected():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='amount']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('42000000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('123')
    country_drop = browser.find_element(By.XPATH, "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('City')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    browser.close()


def test_top_up_usdc_use_invalid_data_lost_city_field_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('42000000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('address one')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    time.sleep(1)
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    browser.close()


def test_top_up_usdc_use_invalid_data_lost_address_field_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('42000000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('district')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    browser.close()


def test_top_up_usdc_use_invalid_data_lost_province_field_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('42000000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('58000')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Required'
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    browser.close()


def test_top_up_usdc_use_invalid_data_lost_postal_field_empty():
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(
        ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")))
    manage_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL']")
    manage_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'USDC')))
    usdc_drop = browser.find_element(By.ID, 'USDC')
    usdc_drop.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'Top_up_with_fiat')))
    fiat = browser.find_element(By.ID, 'Top_up_with_fiat')
    fiat.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    amount = browser.find_element(By.XPATH, "//input[@name='amount']")
    amount.send_keys('100')
    card_holder = browser.find_element(By.XPATH, "//input[@name='ccname']")
    card_holder.send_keys('clark kent')
    card_number = browser.find_element(By.XPATH, "//input[@name='cardnumber']")
    card_number.send_keys('42000000000000000')
    mm_yy = browser.find_element(By.XPATH, "//input[@name='expiry']")
    mm_yy.send_keys('1224')
    cvc = browser.find_element(By.XPATH, "//input[@name='cvc']")
    cvc.send_keys('')
    country_drop = browser.find_element(
        By.XPATH,
        "//div[@class='CustomSelect_select__5EopE CustomSelect_crypto__mGhH3 CustomSelect_montserrat__L3McY']")
    country_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")))
    country = browser.find_elements(By.XPATH, "//div[@class='CustomSelect_option__x3Rbv']")
    country[0].click()
    city = browser.find_element(By.XPATH, "//input[@name='city']")
    city.send_keys('')
    address_one = browser.find_element(By.XPATH, "//input[@name='addressLine_1']")
    address_one.send_keys('')
    address_two = browser.find_element(By.XPATH, "//input[@name='addressLine_2']")
    address_two.send_keys('address two')
    province = browser.find_element(By.XPATH, "//input[@name='district']")
    province.send_keys('')
    postal = browser.find_element(By.XPATH, "//input[@name='postalCode']")
    postal.send_keys('')
    province.click()
    deposit_funds = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    deposit_funds.click()
    assert deposit_funds.is_displayed()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Input_tipError__CKiEf']")))
    error = browser.find_element(By.XPATH, "//div[@class='Input_tipError__CKiEf']").text
    assert error == 'Required'
    browser.close()