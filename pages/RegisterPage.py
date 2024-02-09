from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self,driver):
        self.driver = driver

    first_name_field_id="input-firstname"
    last_name_field_id="input-lastname"
    email_field_id="input-email"
    telephone_field_name="telephone"
    password_filed_id="input-password"
    confirm_pass_id="input-confirm"
    agree_checkbox_name="agree"
    continue_button_xpath="//input[@value='Continue']"
    yes_radio_button_xpath="//input[@name='newsletter'][@value='1']"


    def enter_first_name(self,first_name_text):
        self.driver.find_element(By.ID,self.first_name_field_id).click()
        self.driver.find_element(By.ID, self.first_name_field_id).clear()
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name_text)
    def enter_last_name(self,last_name):
        self.driver.find_element(By.ID,self.last_name_field_id).click()
        self.driver.find_element(By.ID,self.last_name_field_id).clear()
        self.driver.find_element(By.ID,self.last_name_field_id).send_keys(last_name)

    def enter_email(self,email_text):
        self.driver.find_element(By.ID,self.email_field_id).click()
        self.driver.find_element(By.ID,self.email_field_id).clear()
        self.driver.find_element(By.ID,self.email_field_id).send_keys(email_text)

    def enter_telphone_no(self,telephone):
        self.driver.find_element(By.NAME,self.telephone_field_name).click()
        self.driver.find_element(By.NAME,self.telephone_field_name).clear()
        self.driver.find_element(By.NAME,self.telephone_field_name).send_keys(telephone)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.password_filed_id).click()
        self.driver.find_element(By.ID,self.password_filed_id).clear()
        self.driver.find_element(By.ID,self.password_filed_id).send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.driver.find_element(By.ID,self. confirm_pass_id).click()
        self.driver.find_element(By.ID,self. confirm_pass_id).clear()
        self.driver.find_element(By.ID,self. confirm_pass_id).send_keys(confirm_password)

    def click_on_agree_chekbox(self):
        self.driver.find_element(By.NAME,self.agree_checkbox_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH,self. continue_button_xpath).click()

    def select_radio_button(self):
        self.driver.find_element(By.XPATH,self.yes_radio_button_xpath).click()


