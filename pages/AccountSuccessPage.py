from selenium.webdriver.common.by import By


class AccountSuccessPage:
    def __init__(self,driver):
        self.driver=driver

    account_creation_success_sms="//div[@id='content']/h1"

    def verify_acc_creation_sms(self):
        return self.driver.find_element(By.XPATH,self.account_creation_success_sms).text