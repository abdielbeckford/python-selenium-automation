from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


# open the url
@given('Open Target main page')
def open_target_main_page(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()


#Click Cart Icon
@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()

    sleep(3)


#Verification
@then('Verify cart is empty')
def verify_cart(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")
    assert actual_text.text == 'Your cart is empty', f'Error: Text Your cart is empty not in '
