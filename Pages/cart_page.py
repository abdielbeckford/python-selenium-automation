from selenium.webdriver.common.by import By
from Pages.base_page import Page
from features.steps.Add_to_cart import Mango_in_cart


class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon']")
    Cart_empty_msg = (By.XPATH, "//h1[text()='Your cart is empty']")
    Mango_in_cart = (By.XPATH, "//div[text()='Premium Mango - each']")

    def verify_cart_empty(self):
        actual_text = self.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
        assert actual_text.text == 'Your cart is empty', f'Error: Text Your cart is empty not in '

    def verify_item_in_cart(self, item):
        actual_text = self.driver.find_element(*self.Mango_in_cart).text
        assert actual_text == item, f'Error: {item} not in cart '
