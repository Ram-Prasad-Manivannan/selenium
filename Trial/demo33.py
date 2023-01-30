# Necessary import statements
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

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

# Selecting Radio Button Demo from listbox
driver.find_element(By.XPATH, '(//a[text()="Radio Buttons Demo"])[1]').click()
time.sleep(3)

list1 = ["Male","Female"]
list2 = ["0 - 5","5 - 15","15 - 50"]

# p1

# "when none of radio buttons are selected"
driver.find_element(By.XPATH, '//button[@id="buttoncheck"]').click()
val = driver.find_element(By.XPATH, '//p[@class="radiobutton"]').text
print(val)

for i in list1:
    # selecting male/female
    driver.find_element(By.XPATH, f'(//input[@value="{i}"])[1]').click()
    # clicking on Get checked value button
    driver.find_element(By.XPATH, '//button[@id="buttoncheck"]').click()
    # printing the value
    val = driver.find_element(By.XPATH, '//p[@class="radiobutton"]').text
    print(val)

# p2

# "when none of radio buttons are selected"
print("when none of radio buttons are selected")
driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
time.sleep(3)
chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
print(chk)
# "when only sex is selected"
print("when only sex is selected")
for i in list1:
    driver.find_element(By.XPATH, f'(//input[@value="{i}"])[2]').click()
    driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
    time.sleep(3)
    chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
    print(chk)

# "when only age group is selected"
print("when only age group is selected")
driver.refresh()  # refreshing the page to clear the form
for j in list2:
    driver.find_element(By.XPATH, f'//input[@value="{j}"]').click()
    driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
    time.sleep(3)
    chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
    print(chk)

# "when both fields are selected"
for i in list1:
    driver.find_element(By.XPATH, f'(//input[@value="{i}"])[2]').click()
    for j in list2:
        driver.find_element(By.XPATH, f'//input[@value="{j}"]').click()
        driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
        time.sleep(3)
        chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
        print(chk)

driver.close()
