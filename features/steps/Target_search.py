from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then
from webdriver_manager.core import driver
from selenium.webdriver.support import expected_conditions as EC

Search_input = (By.ID, 'search')
Search_Btn = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
Search_Result_Shown = (By.XPATH, "//div[@data-test='resultsHeading']")


# open the url
# @given('Open Target main page')
# def open_target_main_page(context):
#     context.driver.get('https://www.target.com/')

# driver.wait.until(EC.element_to_be_clickable(Search_Result_Header))

@when('Hover favorites icon')
def hover_favorites(context):
    context.app.search_results_page.hover_fav_icon()


@when('Search for {item}')
def search_for(context, item):
    context.app.header.search_product(item)


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    context.app.search_results_page.verify_search_results(expected_item)

@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results_page.verify_fav_tooltip()