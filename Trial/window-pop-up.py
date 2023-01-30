# Necessary import statements
# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

print("...Windows POP UP Modal started...")

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

# Window Popup Modal
driver.find_element(By.XPATH,"//a[text()='Window Popup Modal']").click()
time.sleep(2)

driver.find_element(By.XPATH,"//a[text()='  Follow On Twitter ']").click()
time.sleep(10)

driver.switch_to.window(driver.window_handles[1])
time.sleep(10)
assert "Twitter" in driver.title
driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.find_element(By.XPATH,"//a[text()='  Like us On Facebook ']").click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
assert driver.title == "Selenium Easy | Hyderabad | Facebook"

driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(1)

driver.find_element(By.XPATH,"//a[text()='Follow Twitter & Facebook']").click()
time.sleep(5)
assert driver.title == "Selenium Easy - Window Popup Modal Demo"

driver.switch_to.window(driver.window_handles[1])
assert "Twitter" in driver.title
driver.close()
time.sleep(5)

driver.switch_to.window(driver.window_handles[1])
assert driver.title == "Selenium Easy | Hyderabad | Facebook"
time.sleep(5)
driver.close()

driver.switch_to.window(driver.window_handles[0])
assert driver.title == "Selenium Easy - Window Popup Modal Demo"
time.sleep(2)

driver.find_element(By.ID,"followall").click()

driver.switch_to.window(driver.window_handles[1])
assert driver.title == "Sign in - Google Accounts"
driver.close()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
assert "Twitter" in driver.title
driver.close()

driver.switch_to.window(driver.window_handles[1])
assert driver.title == "Selenium Easy | Hyderabad | Facebook"
driver.close()

driver.switch_to.window(driver.window_handles[0])
assert driver.title == "Selenium Easy - Window Popup Modal Demo"

print("...Window pop up modals ended successfully...")
driver.close()
