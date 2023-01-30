# Necessary import statements
from selenium import webdriver
import time

# keyboard actions
from selenium.webdriver import ActionChains

# id import
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Importing Select class
from selenium.webdriver.support.ui import Select

print("...demo 4.4 started...")

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

# Selecting Drop down Demo from listbox
driver.find_element(By.XPATH, '(//a[text()="Select Dropdown List"])[1]').click()
time.sleep(3)

# P1

# Selecting first drop down list aka single select
ele = driver.find_element(By.XPATH, '//select[@id="select-demo"]')
drop = Select(ele)

# Select by value
drop.select_by_value("Thursday")
time.sleep(3)

# check display
chk1 = driver.find_element(By.XPATH, '//p[@class="selected-value"]').text
assert chk1 == "Day selected :- Thursday"

# Select by index
drop.select_by_index(3)
time.sleep(3)

# check display
chk2 = driver.find_element(By.XPATH, '//p[@class="selected-value"]').text
assert chk2 == "Day selected :- Tuesday"

# Select by visible text
drop.select_by_visible_text("Monday")
time.sleep(4)

# check display
chk3 = driver.find_element(By.XPATH, '//p[@class="selected-value"]').text
assert chk3 == "Day selected :- Monday"

# P2

bu = driver.find_element(By.XPATH,'//button[@id="printAll"]')

# Selecting all options

ele1 = driver.find_element(By.XPATH, "//select[@id='multi-select']")
drop1 = Select(ele1)

list1 = ["Florida", "New Jersey", "New York", "Ohio", "Texas", "Pennsylvania", "Washington"]

driver.find_element(By.XPATH, "//select[@id='multi-select']/option[1]").click()

for i in list1:
    val1 = driver.find_element(By.XPATH, f"//select[@id='multi-select']/option[text()='{i}']")
    ActionChains(driver).key_down(Keys.CONTROL).click(val1).key_up(Keys.CONTROL).perform()

time.sleep(2)

# click button show all choices
bu.click()
time.sleep(3)

# Check display
txt = driver.find_element(By.XPATH,'//p[@class="getall-selected"]').text
print(txt)

# Close
driver.close()
