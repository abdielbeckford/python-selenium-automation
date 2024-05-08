from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# open the url
@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')

@when('Click Target signin button')
def click_target_signin_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()

@when("Click 'Sign in' as the pop-up appears")
def click_target_signin_popup(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test*=signIn]")

@then("Verify your taken to 'Sign into your Target account' page")
def verify_target_signin_page(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'StyledHeading')]").text
    expected_text = "Sign into your Target account"
    assert actual_text == expected_text, f"Expected '{expected_text}' but got '{actual_text}'"
