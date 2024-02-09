import time
from datetime import datetime

import pytest
from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from tests.conftest import setup_and_teardown



class Testlogin(BaseTest):
    def test_login_with_valid_credentials(self):
        home_page=HomePage(self.driver)
        home_page.click_on_my_acc_drop_menu()
        time.sleep(10)
        home_page.select_login_option()
        login_page=LoginPage(self.driver)
        login_page.enter_email_address("amitkale.281995@gmail.com")
        login_page.enter_password_filed("12345")
        login_page.click_on_login_button()
        acc_page=AccountPage(self.driver)
        assert acc_page.display_status_of_your_acc_info_option()


    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_acc_drop_menu()
        time.sleep(10)
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address(self.genrate_email_with_time_span())
        login_page.enter_password_filed("12345")
        login_page.click_on_login_button()
        expected_warning_sms="Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrive_warning_sms().__contains__(expected_warning_sms)

    def genrate_email_with_time_span(self):
        time_stamp= datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "amitkale" + time_stamp + "@gmail.com"