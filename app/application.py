from Pages.main_page import MainPage
from Pages.header import Header
from Pages.search_results_page import SearchResultsPage
class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(self.main_page)
        self.search_results_page = SearchResultsPage(self.main_page)


