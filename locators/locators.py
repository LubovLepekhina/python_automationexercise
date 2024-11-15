
class WelcomePageLocators:
     signup_login_btn = ('xpath', "//a[@href='/login']")

class SignupLoginLocators:
     name_signup_input = ('xpath', "//input[@data-qa='signup-name']")
     email_signup_input = ('xpath', "//input[@data-qa='signup-email']")
     signup_btn = ('xpath', "//button[@data-qa='signup-button']")

     email_login_input = ('xpath', "//input[@data-qa='login-email']")
     password_login_input = ('xpath', "//input[@data-qa='login-password']")
     login_btn = ('xpath', "//button[@data-qa='login-button']")

class AccountInformationLocators:
     radio_btn_mr = ('xpath', "//input[@value='Mr']")
     radio_btn_mrs = ('xpath', "//input[@value='Mrs']")

     name_input = ('xpath', "//input[@id='name']")
     email_input = ('xpath', "//input[@id='email']")
     password_input = ('xpath', "//input[@id='password']")
     first_name_input = ('xpath', "//input[@id='first_name']")
     last_name_input = ('xpath', "//input[@id='last_name']")
     address1_input = ('xpath', "//input[@id='address1']")
     select_country = ('xpath', "//select[@id='country']")
     state_input = ('xpath', "//input[@id='state']")
     city_input = ('xpath', "//input[@id='city']")
     zip_code_input = ('xpath', "//input[@id='zipcode']")
     mobile_number_input = ('xpath', "//input[@id='mobile_number']")

     create_account_btn = ('xpath', "//button[@data-qa='create-account']")