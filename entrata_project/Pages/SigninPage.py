from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class SignInpage:
    def __init__(self,driver):
        self.driver=driver



    sign_in_optin_link_text="Sign In"
    #propery_manager_login_link_text="Property Manager Login"
    property_manager_login_xpath="//a[@title='Client Login Button']"
    username_id="entrata-username"
    password_id="entrata-password"
    signin_button_xpath="//button[@type='submit']"
    warning_sms_for_blank_input_signin_xpath="//div[@class='login-errors hide']/p"
    cookies_xpath="//button[@id='rcc-decline-button']"

    def click_on_sign_in_option(self):
        self.driver.find_element(By.LINK_TEXT,self.sign_in_optin_link_text).click()

    def click_on_property_manager_login_option(self):

         self.driver.find_element(By.XPATH,self.property_manager_login_xpath).click()

        # Explicit wait using WebDriverWait for the cookie consent form to disappear
        #  WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH,"//a[@title='Client Login Button']"))
        #  ).click()


    def enter_username(self,username):
        self.driver.find_element(By.ID,self.username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.password_id).send_keys(password)

    def click_on_signin_button(self):
        self.driver.find_element(By.XPATH,self.signin_button_xpath).click()

    def display_warning_sms_for_blank_input(self):
        return self.driver.find_element(By.XPATH,self.warning_sms_for_blank_input_signin_xpath).text

    def click_on_cookies_accept(self):
        self.driver.find_element(By.XPATH,self.cookies_xpath).click()