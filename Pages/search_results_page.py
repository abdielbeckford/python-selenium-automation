from Pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):

    Search_Result_Header = (By.XPATH, "//div[@data-test='resultsHeading']")
    Add_to_cart = (By.CSS_SELECTOR, "button[aria-label='Add Premium Mango - each to cart']")

    def verify_search_results(self, expected_item):
        actual_text = self.driver.find_element(*self.Search_Result_Header).text
        assert expected_item in actual_text

    def add_to_cart_btn(self):
        self.driver.find_element(*self.Add_to_cart).click()

