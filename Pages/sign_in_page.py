from Pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    Sign_In_Header = (By.XPATH, "//span[text()='Sign into your Target account']")
    terms_and_conditions_link = (By.XPATH, "//a[text()='Target terms and conditions']")

    def verify_signin_page(self, expected_text, *locator):
        actual_text = self.driver.find_element(*self.Sign_In_Header).text
        assert expected_text == actual_text, f"Expected: {expected_text}, Actual: {actual_text}"

    def open_sign_in_page(self):
        self.open(
            'https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def click_terms_and_conditions_link(self):
        click(self.terms_and_conditions_link)

    def verify_TC_opened(self):
        self.verify_partial_url('terms-condition')