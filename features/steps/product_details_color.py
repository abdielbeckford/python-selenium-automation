from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, "button[class*='StyledBaseButton'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "div[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapper']")


@given('Open Target product {product_id} page')
def open_target_product(context, product_id):
    context.driver.get(www.target.com / p / {product_id})
    sleep(6)


@then('Verify user can click through colors')
def verify_colors(context):
    expected_colors = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert actual_colors == expected_colors, f'Expected {expected_colors}, got {actual_colors}'
