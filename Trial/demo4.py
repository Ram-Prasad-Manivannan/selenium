# Necessary import statements
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
# id import
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Importing Select class
from selenium.webdriver.support.ui import Select


print("...demo 3 started...")

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

# P1
 #Selecting Drop down Demo from listbox
driver.find_element(By.XPATH, '(//a[text()="Select Dropdown List"])[1]').click()
time.sleep(3)
#
# # Selecting first drop down list aka single select
# ele = driver.find_element(By.XPATH, '//select[@id="select-demo"]')
# drop = Select(ele)
#
# # Select by value
# drop.select_by_value("Thursday")
# time.sleep(4)
#
# # check display
# chk1 = driver.find_element(By.XPATH, '//p[@class="selected-value"]').text
# assert chk1 == "Day selected :- Thursday"
#
# # Select by index
# drop.select_by_index(3)
# time.sleep(4)
#
# # check display
# chk2 = driver.find_element(By.XPATH, '//p[@class="selected-value"]').text
# assert chk2 == "Day selected :- Tuesday"
#
# # Select by visible text
# drop.select_by_visible_text("Monday")
# time.sleep(4)
#
# # check display
# chk3 = driver.find_element(By.XPATH, '//p[@class="selected-value"]').text
# assert chk3 == "Day selected :- Monday"

# # Select by id ????
# id1 = driver.find_element(By.XPATH,'//select[@id="select-demo"]/option[7]')
# drop.select_by_value(id1)
# time.sleep(3)

# # check display
# chk4 = driver.find_element(By.XPATH, '//p[@class="selected-value"]').text
# assert chk4 == "Day selected :- Friday"

# P2
# Selecting all options
ele1 = driver.find_element(By.XPATH, "//select[@id='multi-select']")
#ele1 = driver.find_element(By.XPATH, "//select[@id='multi-select']//option[@value='Ohio']")
#drop1 = Select(ele1)
#drop1.select_by_value("Texas")
#time.sleep(3)
# # for option in options:
val1 = driver.find_element(By.XPATH, "//select[@id='multi-select']//option[@value='Ohio']")
val2 = driver.find_element(By.XPATH, "//select[@id='multi-select']//option[@value='Texas']")
val3 = driver.find_element(By.XPATH, "//select[@id='multi-select']//option[@value='California']")
ActionChains(driver).key_down(Keys.CONTROL).click(val1).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(val2).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(val3).key_up(Keys.CONTROL).perform()

#ActionChains(driver).send_keys(Keys.CONTROL).click(driver.find_element(By.XPATH, "//select[@id='multi-select']//option[@value='Ohio']"))
#ActionChains(driver).send_keys(Keys.CONTROL).click(driver.find_element(By.XPATH, "//select[@id='multi-select']//option[@value='California']"))
time.sleep(3)

# click button show all choices
driver.find_element(By.XPATH,'//button[@id="printAll"]').click()

# Check display
txt = driver.find_element(By.XPATH,'//p[@class="getall-selected"]').text
print(txt)