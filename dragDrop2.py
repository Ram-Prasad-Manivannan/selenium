# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# main program
print("...drag and drop started...")

# Driver initiation
driver = webdriver.Chrome()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://demo.automationtesting.in/Dynamic.html")
time.sleep(2)

# target element
target = driver.find_element(By.XPATH,"//div[@id='droparea']")

# source:
source = driver.find_element(By.XPATH,"//div[@class='col-xs-10 col-xs-offset-2'][2]")

# drag
ActionChains(driver).drag_and_drop(source,target).perform()
time.sleep(20)

# close
#driver.close()
