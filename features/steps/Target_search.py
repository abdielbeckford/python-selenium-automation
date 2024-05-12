from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then
from webdriver_manager.core import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.wait = WebDriverWait(driver, 10)

Search_input = (By.ID, 'search')
Search_Btn = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
Search_Result_Header = (By.XPATH, "//div[@data-test='resultsHeading']")

# open the url
# @given('Open Target main page')
# def open_target_main_page(context):
#     context.driver.get('https://www.target.com/')

driver.wait.until(EC.element_to_be_clickable(Search_Result_Header))


@when('Search for {item}')
def search_for(context, item):
    context.driver.find_element(Search_input).send_keys(item)
    context.driver.find_element(Search_Btn).click()
    sleep(3)


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(Search_Result_Header).text
    assert expected_item in actual_text
