from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver =driver

    email_address_field_id="input-email"
    password_field="input-password"
    login_button_xpath="//input[@value='Login']"
    no_match_warning_smsfor_invalidcredentials="//div[@id='account-login']/div[1]"


    def enter_email_address(self,email_address_text):
        self.driver.find_element(By.ID,self.email_address_field_id).click()
        self.driver.find_element(By.ID,self.email_address_field_id).clear()
        self.driver.find_element(By.ID,self.email_address_field_id).send_keys(email_address_text)

    def enter_password_filed(self,password_text):
        self.driver.find_element(By.ID,self.password_field).click()
        self.driver.find_element(By.ID,self.password_field).clear()
        self.driver.find_element(By.ID,self.password_field).send_keys(password_text)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath)

    def retrive_warning_sms(self):
        return self.driver.find_element(By.XPATH,self.no_match_warning_smsfor_invalidcredentials).text

