from conftest import driver
from data.urls import Urls
from pages.account_information_page import AccountInformationPage
from pages.signup_page import Signup
from pages.welcome_page import WelcomePage


class TestCreateUser:
    url = Urls()

    def test_click_signup_btn(self, driver):
        page = WelcomePage(driver, self.url.automation_exercise_base_url)
        page.open()
        page.click_btn_signup_login()

    def test_signup(self, driver):
        page = Signup(driver, self.url.login_signup_page_url)
        page.open()
        page.fill_fields()

    def test_create_user(self, driver):
        page = Signup(driver, self.url.login_signup_page_url)
        page.open()
        page.fill_fields()
        page_acc = AccountInformationPage(driver, self.url.create_account_page_url)
        page_acc.fill_all_fields()
