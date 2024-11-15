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

    def type(self, locator,text):
        self.find_element(locator).send_keys(text)

    def select_option(self, locator, item):
        # Найти элемент выпадающего списка
        dropdown = self.find_element(locator)  # Замените на реальный ID

        # Работа с выпадающим списком через класс Select
        select = Select(dropdown)

        # Выбрать элемент по видимому тексту
        select.select_by_visible_text(item)

        # Выбрать элемент по значению атрибута value
        # select.select_by_value("option_value")
        #
        # # Выбрать элемент по индексу
        # select.select_by_index(2)