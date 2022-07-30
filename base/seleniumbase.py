from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

class SeleniumBase:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 15, 0.3)

    def get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.presence_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.wait.until(ec.presence_of_all_elements_located((self.get_selenium_by(find_by), locator)), locator_name)