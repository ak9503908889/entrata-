from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self,driver):
        self.driver=driver


    hompage_text_xpath="//div[@class='hero-left']/h1"
    watch_demo_link_text="Watch Demo"
    watch_demo_pagetitle_text_xpath="//div[@id='Banner_Title']"
    linkedin_xpath="//a[@title='Entrata Inc. Linkedin Page']"

    def disply_home_page_title(self, expected_title):
        actual_title = self.driver.title    # there is a method to get the page title
        return actual_title==expected_title

    def display_home_page_text(self):
        return self.driver.find_element(By.XPATH,self.hompage_text_xpath).is_displayed()

    def click_on_watch_demo(self):
        self.driver.find_element(By.LINK_TEXT,self.watch_demo_link_text).click()

    def display_watch_demo_page_text(self):
        return self.driver.find_element(By.XPATH,self.watch_demo_pagetitle_text_xpath).is_displayed()

    def click_on_linkedin_logo(self):
        self.driver.find_element(By.XPATH,self.linkedin_xpath)














