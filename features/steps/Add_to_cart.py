from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then

Search_Btn = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
Search_Result_Header = (By.XPATH, "//div[@data-test='resultsHeading']")
Add_to_cart = (By.CSS_SELECTOR, "button[aria-label='Add Premium Mango - each to cart']")
Add_to_cart_pt2 = (By.CSS_SELECTOR, "button[aria-label*='Add to cart for Premium Mango']")
View_cart = (By.XPATH, "//a[text()='View cart & check out']")
Mango_in_cart = (By.XPATH, "//div[text()='Premium Mango - each']")


# @given('Open Target main page')
# def open_target_main_page(context):
#     context.driver.get('https://www.target.com/')


# @when('Search for {item}')
# def search_for_mango(context, item):
#     context.driver.find_element(By.ID, 'search').send_keys(item)
#     context.driver.find_element(Search_Btn).click()
#     sleep(3)


@then('{item} Search result is shown')
def search_for_mango_result(context, item):
    actual_text = context.driver.find_element(Search_Result_Header).text
    assert item in actual_text


@then('Click add to cart')
def click_add_to_cart(context):
    context.driver.find_element(Add_to_cart).click()
    context.driver.find_element(Add_to_cart_pt2).click()
    sleep(4)


@then('Click view cart & check out')
def click_view_cart(context):
    context.driver.find_element(View_cart).click()
    sleep(4)


@then('Verify {item} is added to cart')
def verify_mango(context, item):
    actual_text = context.driver.find_element(Mango_in_cart).text
    assert "Premium Mango - each" in actual_text
