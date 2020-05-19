import pytest 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestProductPage():
    def element_exist(self, selector, browser):
        try:
            x = browser.find_element_by_css_selector(selector)
            return True
        except NoSuchElementException: 
            return False


    def test_product_page_has_add_to_cart_button(self, browser): 
        browser.get("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        result = self.element_exist ('.btn-add-to-basket', browser)
        assert result == True,  "Button not found"