from conftest import driver
from data.urls import Urls
from pages.account_information_page import AccountInformationPage
from pages.delete_account_page import DeleteAccount
from pages.signup_login_page import SignupLogin
from pages.welcome_page import WelcomePage


class TestCreateUser:
    url = Urls()

    def test_click_signup_btn(self, driver):
        page = WelcomePage(driver, self.url.automation_exercise_base_url)
        page.open()
        page.click_btn_signup_login()

    def test_signup(self, driver):
        page = SignupLogin(driver, self.url.login_signup_page_url)
        page.open()
        page.fill_fields_signup()

    def test_create_user(self, driver):
        page = WelcomePage(driver, self.url.automation_exercise_base_url)
        page.open()
        page.click_btn_signup_login()
        page_signup = SignupLogin(driver, self.url.login_signup_page_url)
        page_signup.fill_fields_signup()
        page_acc = AccountInformationPage(driver, self.url.create_account_page_url)
        page_acc.fill_all_fields()

        expected_name, text = page.find_btn_logged_as()
        assert expected_name in text, 'Text does not contain the expected substring.'

    def test_login_and_delete_user(self, driver):
        page = WelcomePage(driver, self.url.automation_exercise_base_url)
        page.open()
        page.click_btn_signup_login()
        page_login = SignupLogin(driver, self.url.login_signup_page_url)
        page_login.fill_fields_login()

        expected_name, text = page.find_btn_logged_as()
        assert expected_name in text, 'Text does not contain the expected substring.'
        del_btn = page.find_delete_btn()
        assert del_btn.is_displayed()
        color = page.find_color_of_element()
        assert color == 'rgba(165, 42, 42, 1)'
        del_btn.click()

        page_delete = DeleteAccount(driver, self.url.delete_account_page_url)
        # не работает - исправить
        # header = page_delete.find_header()
        # assert header.text == 'Account Deleted!'
        page_delete.click_continue_btn()
        assert driver.current_url == self.url.automation_exercise_base_url

