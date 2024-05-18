from selenium.webdriver.common.by import By
from Pages.base_page import Page


def click(PP_LINK):
    pass


class TargetAppPage(Page):
    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")

    def open_target_app(self):
        self.open('https://www.target.com/c/target-app/')

    def click_pp_link(self):
        click(self.PP_LINK)

    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy/')