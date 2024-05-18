from Pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Header(Page):
    Search_input = (By.ID, 'search')
    Search_Btn = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon']")
    Sign_In_Btn = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")

    def search_product(self, item):
        self.input_text(item, *self.Search_input)
        self.click(*self.Search_Btn)
        sleep(6)

    def click_cart(self):
        self.wait_until_clickable_click()(*self.CART_ICON).click()

    def click_sign_in(self):
        self.wait_until_clickable_click()(*self.Sign_In_Btn).click()

