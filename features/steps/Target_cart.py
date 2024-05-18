from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then

CART_ICON = (By.CSS_SELECTOR, "div[data-test='@web/CartIcon']")
Cart_empty_msg = (By.XPATH, "//h1[text()='Your cart is empty']")


# open the url
@given('Open Target main page')
def open_target_main_page(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()


#Click Cart Icon
@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart()

    sleep(3)


#Verification
@then('Verify cart is empty')
def verify_cart(context):
    context.app.cart_page.verify_cart_empty()