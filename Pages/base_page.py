from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Support.logger import logger


class Page:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver

    def open(self, url):
        logger.info(f"Opening {url}")
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f'{actual_text} != {expected_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'{expected_text} != {actual_text}'

    def wait_until_clickable_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator),
                        f" Message: Element not visible in {locator}").click()

    def wait_until_visible(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator),
                        f" Message: Element not visible in {locator}")

    def wait_until_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element_located(locator),
                        f" Message: Element still visible in {locator}")

    def get_current_window(self):
        current_window = self.driver.current_window_handle
        print('Current:', current_window)
        print('All windows:', self.driver.window_handles)
        return current_window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles  #win1, win2...
        print('All windows:', self.driver.window_handles)
        print('Switching to...', all_windows[1])
        self.driver.switch_to.window(all_windows[1])

    def switch_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(EC.url_contains(expected_partial_url), ),
        f'Partial URL did not match {expected_partial_url}'

    def verify_url(self, expected_url):
        self.wait.until(EC.url_matches(expected_url),
                        f"URL did not match {expected_url}")

    def save_screenshot(self, name):
        self.driver.save_screenshot(f"{name}.png")

    def close(self):
        self.driver.close()
