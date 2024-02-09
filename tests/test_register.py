from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest
from tests.conftest import setup_and_teardown


class Testregister(BaseTest):
    def test_register_with_mandatory_details(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_acc_drop_menu()
        home_page.click_on_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Amit")
        register_page.enter_last_name("kale")
        register_page.enter_email(self.genrate_email_with_time_span())
        register_page.enter_telphone_no("1234567890")
        register_page.enter_password("12345")
        register_page.enter_confirm_password("12345")
        register_page.click_on_agree_chekbox()
        register_page.click_on_continue_button()
        expected_text_after_succesful_register="Your Account Has Been Created!"
        acc_success_page = AccountSuccessPage(self.driver)
        assert acc_success_page.verify_acc_creation_sms().__eq__(expected_text_after_succesful_register)

    def test_register_with_All_details(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_acc_drop_menu()
        home_page.click_on_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name("Amit")
        register_page.enter_last_name("kale")
        register_page.enter_email(self.genrate_email_with_time_span())
        register_page.enter_telphone_no("1234567890")
        register_page.enter_password("12345")
        register_page.enter_confirm_password("12345")
        register_page.select_radio_button()
        register_page.click_on_agree_chekbox()
        register_page.click_on_continue_button()
        expected_text_after_succesful_register="Your Account Has Been Created!"
        acc_success_page = AccountSuccessPage(self.driver)
        assert acc_success_page.verify_acc_creation_sms().__eq__(expected_text_after_succesful_register)

    """def test_register_with_duplicate_email_id(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("Amit")
        self.driver.find_element(By.ID, "input-lastname").send_keys("kale")
        self.driver.find_element(By.ID, "input-email").send_keys("amitkale.281995@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.ID, "input-confirm").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_text_after_same_email_idused= "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(expected_text_after_same_email_idused)

    def test_register_with_empty_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys("")
        self.driver.find_element(By.ID, "input-lastname").send_keys("")
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-telephone").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.ID, "input-confirm").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()

        expected_privacy_sms= "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__( expected_privacy_sms)

        expected_firstname_warningsms="First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div").text.__eq__(expected_firstname_warningsms)

        expexted_last_name_sms="Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-lastname']/following-sibling::div").text.__eq__(expexted_last_name_sms)

        expected_email_sms="E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-email']/following-sibling::div").text.__eq__(expected_email_sms)

        expected_telephone_sms="Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-telephone']/following-sibling::div").text.__eq__(expected_telephone_sms)

        expexted_password_sms="Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-password']/following-sibling::div").text.__eq__(expexted_password_sms)  """

    # just creating one method for chek new email each time whenever automate.it will give new mail every time .
    def genrate_email_with_time_span(self):
        time_stamp= datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "amitkale"+time_stamp+"@gmail.com"