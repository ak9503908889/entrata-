import pytest

from pages import Searchpage
from pages.HomePage import HomePage
from pages.Searchpage import SearchPage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):
    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_product()


    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("Honda")
        home_page.click_on_search_button()
        expected_text="There is no product that matches the search criteria."
        search_page = SearchPage(self.driver)
        assert search_page.retrive_no_product_sms().__eq__(expected_text)

    def test_search_for_blank_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("")
        home_page.click_on_search_button()
        expected_text="There is no product that matches the search criteria."
        search_page = SearchPage(self.driver)
        assert search_page.retrive_no_product_sms().__eq__(expected_text)
