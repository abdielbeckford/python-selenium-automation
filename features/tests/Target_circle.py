from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


Circle_Logo = (By.CSS_SELECTOR, "image[href*='LogoTargetCircle']"

@given('Open Target Circle')
def open_target_circle(context):
    context.driver.get(https://www.target.com/circle)


@then('Verify header is shown')
def verify_header(context):
    context.driver.find_element(Circle_Logo)

@then('Verify Target Circle has 10 benefit cells')
def verify_benefit_cells(context):
