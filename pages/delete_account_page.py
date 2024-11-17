from locators.locators import DeleteAccountLocators
from pages.base_page import BasePage


class DeleteAccount(BasePage):
    locators = DeleteAccountLocators()

    def find_header(self):
        return self.find_element(self.locators.header_delete_acc)

    def click_continue_btn(self):
        self.click_element(self.locators.continue_btn)