import json

from conftest import driver
from locators.locators import SignupLoginLocators
from pages.base_page import BasePage

class SignupLogin(BasePage):
    locators = SignupLoginLocators()

    def fill_fields_signup(self):
        data = self.get_data_from_json(self,'../data/user_data.json')
        self.find_element(self.locators.name_signup_input).send_keys(data['name'])
        self.find_element(self.locators.email_signup_input).send_keys(data['email'])
        self.click_element(self.locators.signup_btn)

    def fill_fields_login(self):
        data = self.get_data_from_json(self, '../data/user_data.json')
        self.find_element(self.locators.email_login_input).send_keys(data['email'])
        self.find_element(self.locators.password_login_input).send_keys(data['password'])
        self.click_element(self.locators.login_btn)
