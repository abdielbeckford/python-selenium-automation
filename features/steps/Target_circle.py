from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then


Cells = (By.CSS_SELECTOR, "div[class*='CellItemContainer']")

Circle_Logo = (By.CSS_SELECTOR, "image[href*='LogoTargetCircle']")


@given("Open Target Circle")
def open_target_circle(context):
    context.driver.get("https://www.target.com/circle")
    sleep(5)


@then('Verify header is shown')
def verify_header(context):
    context.driver.find_element(*Circle_Logo)
    sleep(5)


@then('Verify Target Circle has {expected_amount} benefit cells')
def verify_benefit_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(Cells)
    print(cells)
    assert len(cells) == expected_amount, f"Expected 10 benefit cells, got {len(cells)}"

    for cell in cells:
        print(cells.text)
