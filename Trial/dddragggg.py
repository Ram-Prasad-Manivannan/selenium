# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# main program
print("...drag and drop started...")

# Driver initiation
driver = webdriver.Chrome()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://demo.automationtesting.in/Static.html")
time.sleep(2)

# target element
target = driver.find_element(By.XPATH,"//div[@id='droparea']")

# source:
source = driver.find_element(By.XPATH,"//img[@id='mongo']")

# drag
ActionChains(driver).click_and_hold(source).move_to_element(target).release(source).perform()
time.sleep(4)
ActionChains(driver).