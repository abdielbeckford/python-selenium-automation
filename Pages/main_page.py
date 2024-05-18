from Pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):

    def open_main_page(self):
        self.driver.get('https://www.target.com/')
