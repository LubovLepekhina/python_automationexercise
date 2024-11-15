from locators.locators import WelcomePageLocators
from pages.base_page import BasePage


class WelcomePage(BasePage):
    locators = WelcomePageLocators()

    def click_btn_signup_login(self):
        self.click_element(self.locators.signup_login_btn)


