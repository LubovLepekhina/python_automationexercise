import json

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def select_option(self, locator, item):
        dropdown = self.find_element(locator)
        select = Select(dropdown)
        select.select_by_visible_text(item)

    @staticmethod
    def get_data_from_json(self, path):
        with open(path, 'r') as data_user:
            return json.load(data_user)

    def find_style_of_element(self, locator, style):
        element = self.find_element(locator)
        return element.value_of_css_property(style)