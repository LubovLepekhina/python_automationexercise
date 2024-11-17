from locators.locators import WelcomePageLocators
from pages.base_page import BasePage


class WelcomePage(BasePage):
    locators = WelcomePageLocators()

    def click_btn_signup_login(self):
        self.click_element(self.locators.signup_login_btn)

    def find_btn_logged_as(self):
        data = self.get_data_from_json(self, '../data/user_data.json')
        el = self.find_element(self.locators.logged_in_as_btn)
        return data['name'], el.text

    def find_color_of_element(self):
        return self.find_style_of_element(self.locators.delete_account_btn, 'color')

    def find_delete_btn(self):
        return self.find_element(self.locators.delete_account_btn)