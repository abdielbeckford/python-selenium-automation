from Pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class Header(Page):
    Search_input = (By.ID, 'search')
    Search_Btn = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, item):
        self.input_text(item, *self.Search_input)
        self.click(*self.Search_Btn)
        sleep(6)

