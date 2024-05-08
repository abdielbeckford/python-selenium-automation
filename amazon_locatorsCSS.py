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
driver.get('https://www.amazon.com/)


#Locator for Amazon logo
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")

#Locator for Creat account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#Locator for your name
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

#Locator mobile number or email
driver.find_element(By.CSS_SELECTOR, ".a-input-text[type='email']")

#Locator for password
driver.find_element(By.CSS_SELECTOR, "#ap_password[placeholder='At least 6 characters']")

#Locator for re-enter password
driver.find_element(By.CSS_SELECTOR, "input[name='passwordCheck'][type='password']")

#Locator for create your amazon account
driver.find_element(By.CSS_SELECTOR, "input#continue")

#Locator for conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")

#Locator for privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='privacy_notice']")

#Locator for sign in
driver.find_element(By.CSS_SELECTOR, "a[href*=signin]")




