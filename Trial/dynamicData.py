# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# main program
print("...drag and drop started...")

# Driver initiation
driver = webdriver.Edge()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://demo.seleniumeasy.com/dynamic-data-loading-demo.html")
time.sleep(2)

# verify title
assert driver.title == "Selenium Easy - Dynamically loading data on click"

# verify header
head = driver.find_element(By.XPATH,"//h3").text
assert head == "Loading the data Dynamically"

# verify text?????


# verify button presence
bu = driver.find_element(By.XPATH,"//button[text()='Get New User']")
flag = bu.is_displayed()
assert flag is True

# click the button new user
bu.click()
time.sleep(3)

# data
dat = driver.find_element(By.XPATH,"//div[@id='loading']").get_attribute("textContent")
print(dat)

# verify ????
if 'First Name : ' in dat:
    print("First name is available")
else:
    exit(1)
if 'Last Name :' in dat:
    print("Last name is available")
else:
    exit(1)
