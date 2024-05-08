from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

sleep(2)
#Locator for Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email field
driver.find_element(By.ID, "ap_email")

#continue button
driver.find_element(By.ID, "continue")

#Conditions of use link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#Privacy Notice Link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#forgot your password link
driver.find_element(By.XPATH, "//a[contains(@href,'forgotpassword?')]")

#other issues with sign in link
driver.find_element(By.ID, "ap-other-signin-issues-link")

#create your amazon account button
driver.find_element(By.ID, "createAccountSubmit")
