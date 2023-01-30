# Necessary import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("...demo 6 started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(2)

# Maximize
driver.maximize_window()

# Finding Input Forms
driver.find_element(By.XPATH, '(//a[@class="dropdown-toggle"])[1]').click()
time.sleep(2)

# selecting Ajax Form Submit option
driver.find_element(By.XPATH, '(//a[text()="Ajax Form Submit"])[1]').click()
time.sleep(2)

# t1-p

# input name
driver.find_element(By.XPATH, "//input[@id='title']").send_keys("Raja Singham")
time.sleep(3)

# submit button
driver.find_element(By.XPATH,"//input[@id='btn-submit']").click()

# validate
v = driver.find_element(By.XPATH,"//div[@id='submit-control']").text
assert v == "Form submited Successfully!"

# t2-p
# input name
driver.find_element(By.XPATH, "//input[@id='title']").send_keys("Raja Singham")
time.sleep(3)

# input comment
driver.find_element(By.XPATH,"//textarea").send_keys("...Alive is awesome...")
time.sleep(3)

# submit button
driver.find_element(By.XPATH,"//input[@id='btn-submit']").click()

# validate
v = driver.find_element(By.XPATH,"//div[@id='submit-control']").text
assert v == "Form submited Successfully!"

# t3-n
driver.refresh()
# empty submit
# submit button
driver.find_element(By.XPATH,"//input[@id='btn-submit']").click()

tes = driver.find_element(By.XPATH, "//span[@class='title-validation validation-error']").text
assert tes == "*"

# input comment
driver.find_element(By.XPATH,"//textarea").send_keys("...Alive is awesome...")
time.sleep(3)

# submit button
driver.find_element(By.XPATH,"//input[@id='btn-submit']").click()

tes = driver.find_element(By.XPATH, "//span[@class='title-validation validation-error']").text
assert tes == "*"
