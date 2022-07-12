from selenium import webdriver
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options #as chrome_options
#from fake_useragent import UserAgent
from driver import driver

EMAIL_FOR_REGISTRATION = 'chronicletest5@ukr.net'
URL = 'https://stage.xnl.zpoken.io/login'


def test_edit_display_name_valid_data():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    edit_dis_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_editNameIcon__7b1au']").click()
    time.sleep(1)
    name_input = browser.find_element_by_xpath("//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('validvalidsw')
    time.sleep(1)
    save_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(1)
    display_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_nick__Xc8TN']").text
    time.sleep(1)
    assert display_name == 'validvalidsw'


def test_create_user_avatar():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    avatar_button = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_camera__IFAz7']").click()
    time.sleep(1)
    upload_avatar = browser.find_element_by_xpath("//input[@type='file']")
    upload_avatar.send_keys("C:/Users/WellDone/PycharmProjects/Selenium/valid_image.png")
    time.sleep(3)
    save_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(5)


def test_create_user_avatar_check_nevermind_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    avatar_button = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_camera__IFAz7']").click()
    time.sleep(1)
    never_mind_button = browser.find_element_by_id('upload_avatar_nevermind')

    time.sleep(1)
    never_mind_button.click()
    time.sleep(5)


def test_create_user_avatar_check_remove_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    avatar_button = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_camera__IFAz7']").click()
    time.sleep(1)
    upload_avatar = browser.find_element_by_xpath("//input[@type='file']")
    upload_avatar.send_keys("C:/Users/WellDone/PycharmProjects/Selenium/valid_image.png")
    time.sleep(3)
    remove_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_red__p8Ej9 DragAndDrop_btnRemove__D0MaR Button_withIcon__1TgpF']").click()
    time.sleep(5)


def test_edit_user_avatar():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    avatar_button = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_camera__IFAz7']").click()
    time.sleep(1)
    upload_avatar = browser.find_element_by_xpath("//input[@type='file']")
    upload_avatar.send_keys("C:/Users/WellDone/PycharmProjects/Selenium/image_two.png")
    time.sleep(3)
    save_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(5)


def test_edit_display_name_valid_data_min_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    edit_dis_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_editNameIcon__7b1au']").click()
    time.sleep(1)
    name_input = browser.find_element_by_xpath("//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('w')
    time.sleep(1)
    save_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(1)
    display_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_nick__Xc8TN']").text
    assert display_name == 'w'


def test_edit_display_name_valid_data_max_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    edit_dis_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_editNameIcon__7b1au']").click()
    time.sleep(1)
    name_input = browser.find_element_by_xpath("//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('namenamenamenamenamenamenameww')
    time.sleep(1)
    save_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF']").click()
    time.sleep(1)
    display_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_nick__Xc8TN']").text
    assert display_name == 'namenamenamenamenamenamenameww'


def test_edit_display_name_check_never_mind_button():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)

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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    edit_dis_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_editNameIcon__7b1au']").click()
    time.sleep(1)
    name_input = browser.find_element_by_xpath("//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('namenamenamena')
    time.sleep(1)
    never_mind_button = browser.find_element_by_id('change_display_name_nevermind')
    never_mind_button.click()

    time.sleep(5)


def test_edit_display_name_input_more_than_30_symbols():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    edit_dis_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_editNameIcon__7b1au']").click()
    time.sleep(1)
    name_input = browser.find_element_by_xpath("//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('namenamenamenamenamenamenamewwq')
    time.sleep(1)
    save_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']").click()
    time.sleep(1)


def test_edit_display_name_leave_name_field_empty():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    edit_dis_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_editNameIcon__7b1au']").click()
    time.sleep(1)
    name_input = browser.find_element_by_xpath("//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('')
    time.sleep(1)
    save_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']").click()
    time.sleep(2)


def test_edit_display_name_use_already_register_display_name():
    browser = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver')
    browser.get(URL)
    input_chronicle_login = browser.find_element_by_xpath('//input[@name="login"]')
    input_chronicle_login.send_keys(EMAIL_FOR_REGISTRATION)
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
    user_settings = browser.find_element_by_xpath("//div[@class='Dropdown_iconWrap__od6ky']").click()
    time.sleep(1)
    edit_dis_name = browser.find_element_by_xpath("//div[@class='PersonalSettingsModal_editNameIcon__7b1au']").click()
    time.sleep(1)
    name_input = browser.find_element_by_xpath("//input[@class='Input_input__lvORT']")
    name_input.clear()
    time.sleep(1)
    name_input.send_keys('chronicletest102')
    time.sleep(1)
    error_test = browser.find_element_by_xpath("//div[@class='UserNameForm_tipError__Iw7i7']").text
    assert error_test == 'Sorry... This username seems to be already taken.You can use letters, numbers, punctuation marks and special symbols. Get creative!'
    save_button = browser.find_element_by_xpath("//button[@class='Button_btn__JyuE1 Button_violet__5aLbL Button_withIcon__1TgpF Button_disable__0XBGJ']").click()
    time.sleep(2)

