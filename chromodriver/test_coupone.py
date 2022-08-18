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


def test_create_discount_coupon_on_usdc_simple():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    #coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.send_keys("1")
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_create')))
    create_button = browser.find_element(By.ID, "DiscountCoupon_create")
    create_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")))
    creation_message = browser.find_element(By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']").text
    assert creation_message == "CREATION SUCCESSFUL!"
    browser.find_element(By.XPATH, "//*[text() = 'Contents']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Tables_col__lFjTk']")))
    coupon_names = browser.find_elements(By.XPATH, "//div[@class='Tables_col__lFjTk']")
    coupon_name = coupon_names[4].text
    browser.get(URL)
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")))
    items_for_purchase_usd = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    items_for_purchase_usd[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    buy_button = browser.find_element(By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(1)
    try:
        buy_anyway_button = browser.find_element(By.ID, 'Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    tab_wallet = browser.find_element(By.ID, 'confirmBoughtwallet').click()
    wait.until(ec.visibility_of_element_located((By.ID, "coupon")))
    price_before = browser.find_element(By.XPATH, "//div[@class='ConfirmBoughtModal_totalValue__qoUoG']").text
    insert_coupon = browser.find_element(By.ID, "coupon")
    insert_coupon.send_keys(coupon_name)
    time.sleep(3)
    apply_button = browser.find_element(By.XPATH, "//*[text() = 'apply']")
    apply_button.click()
    time.sleep(2)
    price_after = browser.find_element(By.XPATH, "//div[@class='ConfirmBoughtModal_totalValue__qoUoG']").text
    assert price_before != price_after
    pay_now = browser.find_element(By.XPATH, "//*[text() = 'Pay now']")
    pay_now.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, "login")))
    browser.find_element(By.ID, "login").send_keys("savchukura888@gmail.com")
    browser.find_element(By.ID, "password").send_keys("213456qaZ")
    browser.find_element(By.ID, "LoginPage_Sign_in").click()
    #time.sleep(4)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href='/contents']")))
    side_menu = browser.find_element(By.XPATH, "//a[@href='/contents']")
    side_menu.click()
    wait.until(ec.visibility_of_element_located((By.ID, "createCard_coupon")))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Tables_more__V-0H- Tables_icon__kHaaB']")))
    set_but = browser.find_elements(By.XPATH, "//button[@class='Tables_more__V-0H- Tables_icon__kHaaB']")
    set_but[0].click()
    drop_but = browser.find_elements(By.XPATH, "//button[@class='Tables_dropDown__zineI']")
    drop_but[1].click()
    wait.until(ec.visibility_of_element_located((By.ID, "InfoModal_Delete_coupon_Delete_it")))
    del_but = browser.find_element(By.ID, "InfoModal_Delete_coupon_Delete_it").click()
    time.sleep(0.5)
    browser.quit()


def test_create_discount_coupon_on_xnl_simple():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    #coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v XNL']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.send_keys("1")
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_create')))
    create_button = browser.find_element(By.ID, "DiscountCoupon_create")
    create_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")))
    creation_message = browser.find_element(By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']").text
    assert creation_message == "CREATION SUCCESSFUL!"
    browser.find_element(By.XPATH, "//*[text() = 'Contents']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Tables_col__lFjTk']")))
    coupon_names = browser.find_elements(By.XPATH, "//div[@class='Tables_col__lFjTk']")
    coupon_name = coupon_names[4].text
    browser.get(URL)
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r XNL']")))
    items_for_purchase_xnl = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r XNL']")
    items_for_purchase_xnl[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    buy_button = browser.find_element(By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(1)
    try:
        buy_anyway_button = browser.find_element(By.ID, 'Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    tab_wallet = browser.find_element(By.ID, 'confirmBoughtwallet').click()
    wait.until(ec.visibility_of_element_located((By.ID, "coupon")))
    price_before = browser.find_element(By.XPATH, "//div[@class='ConfirmBoughtModal_totalValue__qoUoG']").text
    insert_coupon = browser.find_element(By.ID, "coupon")
    insert_coupon.send_keys(coupon_name)
    time.sleep(3)
    apply_button = browser.find_element(By.XPATH, "//*[text() = 'apply']")
    apply_button.click()
    time.sleep(2)
    price_after = browser.find_element(By.XPATH, "//div[@class='ConfirmBoughtModal_totalValue__qoUoG']").text
    assert price_before != price_after
    pay_now = browser.find_element(By.XPATH, "//*[text() = 'Pay now']")
    pay_now.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, "login")))
    browser.find_element(By.ID, "login").send_keys("savchukura888@gmail.com")
    browser.find_element(By.ID, "password").send_keys("213456qaZ")
    browser.find_element(By.ID, "LoginPage_Sign_in").click()
    #time.sleep(4)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href='/contents']")))
    side_menu = browser.find_element(By.XPATH, "//a[@href='/contents']")
    side_menu.click()
    wait.until(ec.visibility_of_element_located((By.ID, "createCard_coupon")))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Tables_more__V-0H- Tables_icon__kHaaB']")))
    set_but = browser.find_elements(By.XPATH, "//button[@class='Tables_more__V-0H- Tables_icon__kHaaB']")
    set_but[0].click()
    drop_but = browser.find_elements(By.XPATH, "//button[@class='Tables_dropDown__zineI']")
    drop_but[1].click()
    wait.until(ec.visibility_of_element_located((By.ID, "InfoModal_Delete_coupon_Delete_it")))
    del_but = browser.find_element(By.ID, "InfoModal_Delete_coupon_Delete_it").click()
    time.sleep(0.5)
    browser.quit()


def test_create_discount_coupon_on_percent_simple_usdc():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    #coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.send_keys("50")
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_create')))
    create_button = browser.find_element(By.ID, "DiscountCoupon_create")
    create_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")))
    creation_message = browser.find_element(By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']").text
    assert creation_message == "CREATION SUCCESSFUL!"
    browser.find_element(By.XPATH, "//*[text() = 'Contents']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Tables_col__lFjTk']")))
    coupon_names = browser.find_elements(By.XPATH, "//div[@class='Tables_col__lFjTk']")
    coupon_name = coupon_names[4].text
    browser.get(URL)
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")))
    items_for_purchase_usd = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r USDC']")
    items_for_purchase_usd[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    buy_button = browser.find_element(By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(1)
    try:
        buy_anyway_button = browser.find_element(By.ID, 'Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    tab_wallet = browser.find_element(By.ID, 'confirmBoughtwallet').click()
    wait.until(ec.visibility_of_element_located((By.ID, "coupon")))
    price_before = browser.find_element(By.XPATH, "//div[@class='ConfirmBoughtModal_totalValue__qoUoG']").text
    insert_coupon = browser.find_element(By.ID, "coupon")
    insert_coupon.send_keys(coupon_name)
    time.sleep(3)
    apply_button = browser.find_element(By.XPATH, "//*[text() = 'apply']")
    apply_button.click()
    time.sleep(2)
    price_after = browser.find_element(By.XPATH, "//div[@class='ConfirmBoughtModal_totalValue__qoUoG']").text
    assert price_before != price_after
    pay_now = browser.find_element(By.XPATH, "//*[text() = 'Pay now']")
    pay_now.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, "login")))
    browser.find_element(By.ID, "login").send_keys("savchukura888@gmail.com")
    browser.find_element(By.ID, "password").send_keys("213456qaZ")
    browser.find_element(By.ID, "LoginPage_Sign_in").click()
    #time.sleep(4)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href='/contents']")))
    side_menu = browser.find_element(By.XPATH, "//a[@href='/contents']")
    side_menu.click()
    wait.until(ec.visibility_of_element_located((By.ID, "createCard_coupon")))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Tables_more__V-0H- Tables_icon__kHaaB']")))
    set_but = browser.find_elements(By.XPATH, "//button[@class='Tables_more__V-0H- Tables_icon__kHaaB']")
    set_but[0].click()
    drop_but = browser.find_elements(By.XPATH, "//button[@class='Tables_dropDown__zineI']")
    drop_but[1].click()
    wait.until(ec.visibility_of_element_located((By.ID, "InfoModal_Delete_coupon_Delete_it")))
    del_but = browser.find_element(By.ID, "InfoModal_Delete_coupon_Delete_it").click()
    time.sleep(0.5)
    browser.quit()


def test_create_discount_coupon_on_percent_simple_xnl():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    #coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.send_keys("50")
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_create')))
    create_button = browser.find_element(By.ID, "DiscountCoupon_create")
    create_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']")))
    creation_message = browser.find_element(By.XPATH, "//div[@class='Toastify__toast Toastify__toast-theme--colored Toastify__toast--success']").text
    assert creation_message == "CREATION SUCCESSFUL!"
    browser.find_element(By.XPATH, "//*[text() = 'Contents']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Tables_col__lFjTk']")))
    coupon_names = browser.find_elements(By.XPATH, "//div[@class='Tables_col__lFjTk']")
    coupon_name = coupon_names[4].text
    browser.get(URL)
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(By.XPATH,
        "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")))
    pop_up_two_fa = browser.find_element(By.XPATH,
        "//div[@class='Modal_modal__77o1K Modal_center__9TGY8 ']//div[@class='Modal_yellow__0RbLH']//button[@class='Button_btn__JyuE1 Button_transparent__FdLwD Button_withIcon__1TgpF']")
    pop_up_two_fa.click()
    browser.execute_script("window.scrollTo(0,1800)")
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")))
    collections = browser.find_elements(By.XPATH, "//div[@class='AllCollectionCard_collectionCard__zDgyu']")
    collections[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r XNL']")))
    items_for_purchase_xnl = browser.find_elements(By.XPATH, "//div[@class='FeaturesCardList_priceWrap__Y6R4r XNL']")
    items_for_purchase_xnl[0].click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    buy_button = browser.find_element(By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(1)
    try:
        buy_anyway_button = browser.find_element(By.ID, 'Item_duplicate_Buy_anyway')
        if buy_anyway_button.is_displayed():
            buy_anyway_button.click()
            print("...")
    except NoSuchElementException:
        print("...")
    wait.until(ec.visibility_of_element_located((By.ID, 'confirmBoughtwallet')))
    tab_wallet = browser.find_element(By.ID, 'confirmBoughtwallet').click()
    wait.until(ec.visibility_of_element_located((By.ID, "coupon")))
    price_before = browser.find_element(By.XPATH, "//div[@class='ConfirmBoughtModal_totalValue__qoUoG']").text
    insert_coupon = browser.find_element(By.ID, "coupon")
    insert_coupon.send_keys(coupon_name)
    time.sleep(3)
    apply_button = browser.find_element(By.XPATH, "//*[text() = 'apply']")
    apply_button.click()
    time.sleep(2)
    price_after = browser.find_element(By.XPATH, "//div[@class='ConfirmBoughtModal_totalValue__qoUoG']").text
    assert price_before != price_after
    pay_now = browser.find_element(By.XPATH, "//*[text() = 'Pay now']")
    pay_now.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[@class='Review_h2__p7QZX']")))
    congratulations = browser.find_element(By.XPATH, "//h2[@class='Review_h2__p7QZX']").text
    assert congratulations == "Congratulations ... it's yours!"
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, "login")))
    browser.find_element(By.ID, "login").send_keys("savchukura888@gmail.com")
    browser.find_element(By.ID, "password").send_keys("213456qaZ")
    browser.find_element(By.ID, "LoginPage_Sign_in").click()
    #time.sleep(4)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href='/contents']")))
    side_menu = browser.find_element(By.XPATH, "//a[@href='/contents']")
    side_menu.click()
    wait.until(ec.visibility_of_element_located((By.ID, "createCard_coupon")))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='Tables_more__V-0H- Tables_icon__kHaaB']")))
    set_but = browser.find_elements(By.XPATH, "//button[@class='Tables_more__V-0H- Tables_icon__kHaaB']")
    set_but[0].click()
    drop_but = browser.find_elements(By.XPATH, "//button[@class='Tables_dropDown__zineI']")
    drop_but[1].click()
    wait.until(ec.visibility_of_element_located((By.ID, "InfoModal_Delete_coupon_Delete_it")))
    del_but = browser.find_element(By.ID, "InfoModal_Delete_coupon_Delete_it").click()
    time.sleep(0.5)
    browser.quit()


def test_create_discount_coupon_on_usdc_user_not_generate_coupon_name():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'name')))
    name = browser.find_element(By.ID, "name")
    name.click()
    wait.until(ec.visibility_of_element_located((By.ID, "intent id")))
    intent = browser.find_element(By.ID, "intent id")
    intent.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='Forms_subInfoText__Vg0Lg Forms_error__d7O4K']")))
    error = browser.find_element(By.XPATH, "//p[@class='Forms_subInfoText__Vg0Lg Forms_error__d7O4K']").text
    assert error == 'The field name is required'
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")))
    create_button = browser.find_element(By.XPATH, "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")
    create_button.click()


def test_create_discount_coupon_on_usdc_user_not_input_amount():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    # coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH,
                                           "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.click()
    wait.until(ec.visibility_of_element_located((By.ID, "intent id")))
    intent = browser.find_element(By.ID, "intent id")
    intent.click()
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__H8fcx']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")))
    create_button = browser.find_element(By.XPATH,
                                         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")
    create_button.click()


def test_create_discount_coupon_on_usdc_user_input_amount_less_than_min_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    # coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH,
                                           "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.send_keys("0.79")
    wait.until(ec.visibility_of_element_located((By.ID, "intent id")))
    intent = browser.find_element(By.ID, "intent id")
    intent.click()
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__H8fcx']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")))
    create_button = browser.find_element(By.XPATH,
                                         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")
    create_button.click()


def test_create_discount_coupon_on_usdc_user_input_amount_more_than_max_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    # coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH,
                                           "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v USDC']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.send_keys("25000.01")
    wait.until(ec.visibility_of_element_located((By.ID, "intent id")))
    intent = browser.find_element(By.ID, "intent id")
    intent.click()
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__H8fcx']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")))
    create_button = browser.find_element(By.XPATH,
                                         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")
    create_button.click()


def test_create_discount_coupon_on_xnl_user_input_amount_less_than_min_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    # coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH,
                                           "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v XNL']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v XNL']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.send_keys("0.79")
    wait.until(ec.visibility_of_element_located((By.ID, "intent id")))
    intent = browser.find_element(By.ID, "intent id")
    intent.click()
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__H8fcx']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")))
    create_button = browser.find_element(By.XPATH,
                                         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")
    create_button.click()


def test_create_discount_coupon_on_xnl_user_input_amount_more_than_max_price():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL_ADMIN)
    wait = WebDriverWait(browser, 15, 0.3)
    wait.until(ec.visibility_of_element_located((By.ID, 'login')))
    admin_login = browser.find_element(By.ID, 'login').send_keys('savchukura888@gmail.com')
    wait.until(ec.visibility_of_element_located((By.ID, 'password')))
    admin_password = browser.find_element(By.ID, 'password').send_keys('213456qaZ')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Sign in']")))
    sign_in_button = browser.find_element(By.XPATH, "//*[text() = 'Sign in']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[text() = 'Create']")))
    browser.find_element(By.XPATH, "//*[text() = 'Create']").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'createCard_coupon')))
    browser.find_element(By.ID, "createCard_coupon").click()
    wait.until(ec.visibility_of_element_located((By.ID, 'DiscountCoupon_generate')))
    generate_button = browser.find_element(By.ID, "DiscountCoupon_generate")
    generate_button.click()
    time.sleep(2)
    # coupon_name = browser.find_element(By.XPATH, "//div[@class='CustomInput_input__6p7Y2']").text
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")))
    discount_amount = browser.find_element(By.XPATH,
                                           "//div[@id='root']/div[2]/div[2]/div/div[3]/div/div/form/div[2]/label/div[2]/div/div/div/h5")
    discount_amount.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v XNL']")))
    type = browser.find_element(By.XPATH, "//span[@class='CustomSelect_titleOption__IiH1v XNL']")
    type.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'default_price.value')))
    amount = browser.find_element(By.ID, "default_price.value")
    amount.send_keys("100000.01")
    wait.until(ec.visibility_of_element_located((By.ID, "intent id")))
    intent = browser.find_element(By.ID, "intent id")
    intent.click()
    rgb = browser.find_element(By.XPATH, "//span[@class='PriceInput_message__H8fcx']").value_of_css_property('Color')
    hex = Color.from_string(rgb).hex
    print(hex)
    assert hex == '#ff002e'
    wait.until(ec.visibility_of_element_located((By.XPATH,
                                                 "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")))
    create_button = browser.find_element(By.XPATH,
                                         "//button[@class='CustomButton_btn__noaTD CustomButton_violet__hMpsX Forms_btn__sN6XV CustomButton_disable__DcsSJ']")
    create_button.click()
