from Pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    Search_Result_Header = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search_results(self, expected_item):
        actual_text = self.driver.find_element(*self.Search_Result_Header).text
        assert expected_item in actual_text
