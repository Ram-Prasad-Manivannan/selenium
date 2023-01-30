# Necessary import statements
# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

print("...Modal started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(2)

# Maximize
driver.maximize_window()

# Finding Alerts & Modals
# driver.find_element(By.XPATH, "//a[text()='Alerts & Modals']").click()
driver.find_element(By.XPATH, "(//li[@class='dropdown'])[5]/a").click()
time.sleep(2)

# bootstrap Modals
driver.find_element(By.XPATH,"//a[text()='Bootstrap Modals']").click()
time.sleep(2)

# title
assert "Selenium Easy Demo - Bootstrap Modal Demo to Automate" in driver.title

# click 1 modal
driver.find_element(By.XPATH,"//a[@href='#myModal0']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[text()='Close']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@href='#myModal0']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[text()='Save changes']").click()
time.sleep(2)

# click 2nd modal
driver.find_element(By.XPATH,"//a[@href='#myModal']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@href='#myModal2']").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//a[text()='Close'])[3]").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@href='#myModal2']").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//a[text()='Save changes'])[3]").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@href='#myModal']").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//a[text()='Save changes'])[2]").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@href='#myModal']").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//a[text()='Close'])[2]").click()
time.sleep(2)

# close
driver.close()
