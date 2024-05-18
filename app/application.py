from Pages.main_page import MainPage
from Pages.header import Header
from Pages.search_results_page import SearchResultsPage
from Pages.cart_page import CartPage
from Pages.base_page import Page
from Pages.side_nav_page import SideNavPage
from Pages.sign_in_page import SignInPage
from Pages.target_app_page import TargetAppPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(self.main_page)
        self.search_results_page = SearchResultsPage(self.main_page)
        self.cart_page = CartPage(self.main_page)
        self.side_nav_page = SideNavPage(self.main_page)
        self.sign_in_page = SignInPage(self.main_page)
        self.target_app_page = TargetAppPage(self.main_page)