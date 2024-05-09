from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# open the url
@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


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
