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

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

expected = 'Sign into your Target account'
actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'StyledHeading')]").text
assert expected == actual, f'Expected: {expected}, Actual: {actual}'

# Make sure login button is shown
driver.find_element(By.ID, 'login')


sleep(5)