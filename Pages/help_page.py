from time import sleep

from selenium.webdriver.common.by import By
from Pages.base_page import Page
from selenium.webdriver.support.ui import Select


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_STR}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def get_locator(self,text):
        # HEADER = (By.XPATH, "//h1[text()=' {HEADER_STR}']")
        # (By.XPATH, "//h1[text()=' Returns']")
        return[self.HEADER[0], self.HEADER[1].replace('{HEADER_STR}', text)]

    def open_help_returns(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def self_topic(self, option):
        topic_dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dd)
        select.select_by_value(option)
        sleep(10)

    def verify_promotions_header(self, expected_header_text):
        self.wait_until_visible(*self.HEADER_PROMOTIONS)

    # def verify_returns_header(self):
    #     self.wait_until_visible(*self.HEADER_RETURNS)

    def verify_header(self, header):
        locator = self.get_locator(header)
        self.wait_until_visible(*locator)
