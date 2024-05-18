from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then

Sign_In_Btn = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
Side_Nav_Sign_In = (By.CSS_SELECTOR, "a[data-test*=signIn]")
Sign_In_Header = (By.XPATH, "//span[text()='Sign into your Target account']")


# open the url
# @given('Open Target main page')
# def open_target_main_page(context):
#     context.driver.get('https://www.target.com/')
@when('Click Target signin button')
def click_target_signin_button(context):
    context.app.header.sign_in_button.click()


@when("Click 'Sign in' as the pop-up appears")
def click_target_signin_popup(context):
    context.app.side_nav_page.click_signin_on_side_nav.click()


@then("Verify your taken to 'Sign into your Target account' page")
def verify_target_signin_page(context):
    context.app.sign_in_page.verify_signin_page()

