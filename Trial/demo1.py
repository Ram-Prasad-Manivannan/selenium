# Necessary import statements
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

print("...demo started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(3)

# Maximize
driver.maximize_window()

# Finding Input Forms
driver.find_element(By.XPATH, '(//a[@class="dropdown-toggle"])[1]').click()
time.sleep(3)

# Selecting Simple Form Demo from listbox
driver.find_element(By.XPATH, '(//a[text()="Simple Form Demo"])[1]').click()
time.sleep(3)

# Finding and entering data in textbox
driver.find_element(By.ID, "user-message").send_keys("Alive is Awesome")
time.sleep(3)

# Clicking on Show Message button
driver.find_element(By.XPATH, '//button[text()="Show Message"]').click()
time.sleep(3)

# Checking if the message displayed is the same as input
element = driver.find_element(By.XPATH, '//span[@id="display"]')
text1 = element.text

assert text1 == "Alive is Awesome"
# if text1 == "Alive is Awesome":
#     print("Same as input...Expected output achieved")
# else:
#     print("Expected Alive is Awesome as text but got: ", text1)

# finding sum value 1
driver.find_element(By.XPATH, '//input[@id="sum1"]').send_keys("5")

# finding sum value 2
driver.find_element(By.XPATH, '//input[@id="sum2"]').send_keys("10")

# getting total value
driver.find_element(By.XPATH, '//button[text()="Get Total"]').click()
element1 = driver.find_element(By.XPATH, '//span[@id="displayvalue"]')
text2 = element1.text

assert text2 == '15'
# if text2 == '15':
#     print("Expected output is achieved which is ", text2)
# else:
#     print("Expected 15 but got this instead : ", text2)

print("...demo 1 is automated successfully...")

# Close
driver.close()
