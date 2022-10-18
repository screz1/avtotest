from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

EMAIL_FOR_REGISTRATION = 'chronicletest5@ukr.net'
URL = 'https://stage.xnl.zpoken.io/login'


def test_edit_display_name_valid_data():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
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
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")))
    edit_dis_name = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")
    edit_dis_name.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='Input_input__lvORT']")))
    name_input = browser.find_element(By.XPATH, "//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('validvalidsw')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    save_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    save_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_nick__Xc8TN']")))
    display_name = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_nick__Xc8TN']").text
    assert display_name == 'validvalidsw'


def test_create_user_avatar():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_camera__IFAz7']")))
    avatar_button = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_camera__IFAz7']")
    avatar_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
    upload_avatar = browser.find_element(By.XPATH, "//input[@type='file']")
    upload_avatar.send_keys("/home/user/PycharmProjects/avtotest/valid_image.png")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    save_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    save_button.click()


def test_create_user_avatar_check_nevermind_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_camera__IFAz7']")))
    avatar_button = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_camera__IFAz7']")
    avatar_button.click()
    wait.until(ec.visibility_of_element_located((By.ID, 'upload_avatar_nevermind')))
    never_mind_button = browser.find_element(By.ID, 'upload_avatar_nevermind')
    never_mind_button.click()
    time.sleep(1)


def test_create_user_avatar_check_remove_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_camera__IFAz7']")))
    avatar_button = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_camera__IFAz7']")
    avatar_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
    upload_avatar = browser.find_element(By.XPATH, "//input[@type='file']")
    upload_avatar.send_keys("/home/user/PycharmProjects/avtotest/valid_image.png")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 DragAndDrop_btnRemove__D0MaR Button_withIcon__1TgpF']")))
    remove_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 DragAndDrop_btnRemove__D0MaR Button_withIcon__1TgpF']")
    remove_button.click()
    time.sleep(1)


def test_edit_user_avatar():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_camera__IFAz7']")))
    avatar_button = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_camera__IFAz7']")
    avatar_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='file']")))
    upload_avatar = browser.find_element(By.XPATH, "//input[@type='file']")
    upload_avatar.send_keys("/home/user/PycharmProjects/avtotest/valid_image.png")
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    save_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    save_button.click()
    time.sleep(5)


def test_edit_display_name_valid_data_min_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")))
    edit_dis_name = browser.find_element(
        By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")
    edit_dis_name.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='Input_input__lvORT']")))
    name_input = browser.find_element(By.XPATH, "//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('w')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    save_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    save_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_nick__Xc8TN']")))
    display_name = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_nick__Xc8TN']").text
    assert display_name == 'w'


def test_edit_display_name_valid_data_max_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")))
    edit_dis_name = browser.find_element(
        By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")
    edit_dis_name.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='Input_input__lvORT']")))
    name_input = browser.find_element(By.XPATH, "//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('namenamenamenamenamenamenameww')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")))
    save_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']")
    save_button.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='PersonalSettingsModal_nick__Xc8TN']")))
    display_name = browser.find_element(By.XPATH, "//div[@class='PersonalSettingsModal_nick__Xc8TN']").text
    assert display_name == 'namenamenamenamenamenamenameww'


def test_edit_display_name_check_never_mind_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")))
    edit_dis_name = browser.find_element(
        By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")
    edit_dis_name.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='Input_input__lvORT']")))
    name_input = browser.find_element(By.XPATH, "//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('name')
    wait.until(ec.visibility_of_element_located((By.ID, 'change_display_name_nevermind')))
    never_mind_button = browser.find_element(By.ID, 'change_display_name_nevermind')
    never_mind_button.click()

    time.sleep(5)


def test_edit_display_name_input_more_than_30_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")))
    edit_dis_name = browser.find_element(
        By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")
    edit_dis_name.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='Input_input__lvORT']")))
    name_input = browser.find_element(By.XPATH, "//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('namenamenamenamenamenamenamewwq')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    save_button = browser.find_element(
        By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    save_button.click()
    time.sleep(1)


def test_edit_display_name_leave_name_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")))
    edit_dis_name = browser.find_element(
        By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")
    edit_dis_name.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='Input_input__lvORT']")))
    name_input = browser.find_element(By.XPATH, "//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('')
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")))
    save_button = browser.find_element(
        By.XPATH,
        "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    save_button.click()
    time.sleep(1)


def test_edit_display_name_use_already_register_display_name():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    wait = WebDriverWait(browser, 15, 0.3)

    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="login"]')))
    input_chronicle_login = browser.find_element(By.XPATH, '//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
    wait.until(ec.visibility_of_element_located((By.XPATH, '//input[@name="password"]')))
    input_chronicle_password = browser.find_element(By.XPATH, '//input[@name="password"]')
    input_chronicle_password.send_keys("213456qaZ")

    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")))
    sign_in_button = browser.find_element(
        By.XPATH, "//div[@class='LoginForm_button__tiE3C']//button[@type='button']")
    sign_in_button.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH,
         "//*[text() = 'skip for now']")))
    pop_up_two_fa = browser.find_element(
        By.XPATH,
        "//*[text() = 'skip for now']")
    time.sleep(2)
    pop_up_two_fa.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")))
    user_drop = browser.find_element(By.XPATH, "//div[@class='UserHeaderCard_dropdownBtn__eXCOo']")
    user_drop.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")))
    user_settings = browser.find_element(By.XPATH, "//div[@class='Dropdown_iconWrap__od6ky']")
    user_settings.click()
    wait.until(ec.visibility_of_element_located(
        (By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")))
    edit_dis_name = browser.find_element(
        By.XPATH, "//div[@class='PersonalSettingsModal_editNameIcon__7b1au']")
    edit_dis_name.click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@class='Input_input__lvORT']")))
    name_input = browser.find_element(By.XPATH, "//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('chronicletest3')
    wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='UserNameForm_tipError__Iw7i7']")))
    error_test = browser.find_element(By.XPATH, "//div[@class='UserNameForm_tipError__Iw7i7']").text
    assert error_test == 'Sorry... This username seems to be already taken.You can use letters, numbers, punctuation marks and special symbols. Get creative!'
    save_button = browser.find_element(By.XPATH, "//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']")
    save_button.click()
    time.sleep(2)

