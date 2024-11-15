import json

from conftest import driver
from locators.locators import WelcomePageLocators, SignupLoginLocators
from pages.base_page import BasePage

class Signup(BasePage):
    locators = SignupLoginLocators()

    def fill_fields(self):
        with open('../data/user_data.json', 'r') as data_user:
            data = json.load(data_user)
        self.find_element(self.locators.name_signup_input).send_keys(data['name'])
        self.find_element(self.locators.email_signup_input).send_keys(data['email'])
        self.click_element(self.locators.signup_btn)


