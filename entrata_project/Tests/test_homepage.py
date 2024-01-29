from telnetlib import EC

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.HomePage import HomePage
from Pages.SigninPage import SignInpage
from Tests.BaseTest import BaseTest



class TestHomePage(BaseTest):
    def test_homepage_title(self):

        # This test is to verify page title.
        home_page=HomePage(self.driver)
        expected_title_entrata = "Property Management Software | Entrata"
        assert home_page.disply_home_page_title(expected_title_entrata)


    def test_text_present_on_homepage(self):
        # verify text is correct which is present on homepage.
        home_page=HomePage(self.driver)
        assert home_page.display_home_page_text()

    # verify watch demo button
    def test_watch_demo_is_click_or_navigate_to_next_page(self):
        home_page = HomePage(self.driver)
        home_page.click_on_watch_demo()
        assert home_page.display_watch_demo_page_text()

    # verify linkedin option is clickable or navigate to next page
    def test_linkedin_option_navigation(self):
        sign_in = SignInpage(self.driver)
        sign_in.click_on_cookies_accept()
        self.driver.implicitly_wait(20)
        home_page = HomePage(self.driver)
        self.driver.execute_script("window.scrollTo(0,8000);")
        #home_page.click_on_linkedin_logo()
        linkedin_logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Entrata Inc. Linkedin Page']"))
        )
        linkedin_logo.click()
        try:
            WebDriverWait(self.driver, 10).until(EC.url_contains("linkedin.com"))
            assert "linkedin.com" in self.driver.current_url
        except Exception as e:
            print(f"Navigation to LinkedIn failed: {str(e)}")












