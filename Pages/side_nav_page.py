from Pages.base_page import Page
from selenium.webdriver.common.by import By


class SideNavPage(Page):
    Side_Nav_Sign_In = (By.CSS_SELECTOR, "a[data-test*=signIn]")
    Add_to_cart_pt2 = (By.CSS_SELECTOR, "button[aria-label*='Add to cart for Premium Mango']")
    View_cart = (By.XPATH, "//a[text()='View cart & check out']")

    def click_signin_on_side_nav(self):
        self.wait_until_clickable_click()(*self.Side_Nav_Sign_In)

    def add_to_cart_side_nav(self):
        self.wait_until_clickable_click()(*self.Add_to_cart_pt2)

    def view_cart_side_nav(self):
        self.wait_until_clickable_click()(*self.View_cart)
