import pytest

from Pages import SigninPage
from Pages.SigninPage import SignInpage
from Tests.BaseTest import BaseTest


class TestSignInPage(BaseTest):
    def test_signin_with_empty_field(self):  # verify warning sms for signin with empty field.

        sign_in=SignInpage(self.driver)
        sign_in.click_on_sign_in_option()
        sign_in.click_on_cookies_accept()
        sign_in.click_on_property_manager_login_option()
        sign_in.enter_username("")
        sign_in.enter_password("")
        sign_in.click_on_signin_button()
        expected_warning_sms="Please enter username and password"
        assert sign_in.display_warning_sms_for_blank_input().__eq__( expected_warning_sms)
