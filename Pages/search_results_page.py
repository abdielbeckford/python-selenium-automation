from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class SearchResultsPage(Page):

    Search_Result_Header = (By.XPATH, "//div[@data-test='resultsHeading']")
    Add_to_cart = (By.CSS_SELECTOR, "button[aria-label='Add Premium Mango - each to cart']")
    favorites_tooltip_txt = (By.XPATH, "//*[text()='Click to sign in and save']")
    favorites_btn = (By.CSS_SELECTOR, '[data-test="FavoritesButton"]')

    def hover_fav_icon(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(*self.favorites_btn))
        actions.perform()

    def verify_fav_tooltip(self):
        self.find_element(*self.favorites_tooltip_txt)
        #or self.verify_text('Click to sign in and save')

    def verify_search_results(self, expected_item):
        actual_text = self.driver.find_element(*self.Search_Result_Header).text
        assert expected_item in actual_text

    def add_to_cart_btn(self):
        self.driver.find_element(*self.Add_to_cart).click()

