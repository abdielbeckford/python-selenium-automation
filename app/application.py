from Pages.main_page import MainPage
from Pages.header import Header
from Pages.search_results_page import SearchResultsPage
from Pages.cart_page import CartPage
from Pages.base_page import Page
from Pages.side_nav_page import SideNavPage
from Pages.sign_in_page import SignInPage
from Pages.target_app_page import TargetAppPage
from Pages.help_page import HelpPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.side_nav_page = SideNavPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.help_page = HelpPage(driver)