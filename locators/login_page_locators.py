from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_INPUT = (By.XPATH, '//input[@name="login"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
    SIGN_IN_BUTTON = (By.XPATH, "//div[@class='LoginForm_button__tiE3C']")