import json

from locators.locators import AccountInformationLocators
from pages.base_page import BasePage


class AccountInformationPage(BasePage):
    locators = AccountInformationLocators()

    def fill_all_fields(self):
        with open('../data/user_data.json', 'r') as data_user:
            data = json.load(data_user)
        if data['gender'] == 'female':
            self.find_element(self.locators.radio_btn_mrs).click()
        else:
            self.find_element(self.locators.radio_btn_mr).click()

        self.find_element(self.locators.password_input).send_keys(data['password'])
        self.find_element(self.locators.first_name_input).send_keys(data['first_name'])
        self.find_element(self.locators.last_name_input).send_keys(data['last_name'])
        self.find_element(self.locators.address1_input).send_keys(data['address1'])
        self.select_option(self.locators.select_country, data['country'])
        self.find_element(self.locators.state_input).send_keys(data['state'])
        self.find_element(self.locators.city_input).send_keys(data['city'])
        self.find_element(self.locators.zip_code_input).send_keys(data['zipcode'])
        self.find_element(self.locators.mobile_number_input).send_keys(data['mobile_number'])

        element = self.find_element(self.locators.create_account_btn)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.click_element(self.locators.create_account_btn)




