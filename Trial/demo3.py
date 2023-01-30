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

# Radio button selection Male
status = driver.find_element(By.XPATH, '(//input[@value="Male"])[1]').is_selected()
if status:
    print("Already selected as male")
else:
    print("Selecting Male Now...")
    driver.find_element(By.XPATH, '(//input[@value="Male"])[1]').click()
    time.sleep(3)

# Clicking on button check
driver.find_element(By.XPATH, '//button[@id="buttoncheck"]').click()
time.sleep(3)

# getting value
val = driver.find_element(By.XPATH, '//p[@class="radiobutton"]').text
print(val)

# Radio button selection Female
status = driver.find_element(By.XPATH, '(//input[@value="Female"])[1]').is_selected()
if status:
    print("Already selected as female")
else:
    print("Selecting Female Now...")
    driver.find_element(By.XPATH, '//input[@value="Female"])[1]').click()
    time.sleep(3)

# Clicking on button check
driver.find_element(By.XPATH, '//button[@id="buttoncheck"]').click()

# getting value
val1 = driver.find_element(By.XPATH, '//p[@class="radiobutton"]').text
print(val1)

# Getting Multiple value
# Selecting sex as "Male" and age group as "15 to 50"
ch1 = driver.find_element(By.XPATH,'//input[@value="Male"])[2]').is_selected()
if ch1:
    print("Already selected as male...")
else:
    print("Selecting male now")
    driver.find_element(By.XPATH, '//input[@value="Male"])[2]').click()
    time.sleep(2)

ch2 = driver.find_element(By.XPATH,'//input[@value="15 - 50"]').is_selected()
if ch2:
    print("Already selected as required...")
else:
    print("Selecting Values now...")
    driver.find_element(By.XPATH, '//input[@value="15 - 50"]').click()
    time.sleep(2)

# Button click
driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
time.sleep(3)

# check the selection
chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
print(chk)
print("...Above is the selected value...")

# Selecting "Male" and "0-5"
ch1 = driver.find_element(By.XPATH,'//input[@value="Male"])[2]').is_selected()
if ch1:
    print("Already selected as male...")
else:
    print("Selecting male now")
    driver.find_element(By.XPATH, '//input[@value="Male"])[2]').click()
    time.sleep(2)

ch2 = driver.find_element(By.XPATH,'//input[@value="0 - 5"]').is_selected()
if ch2:
    print("Already selected as required...")
else:
    print("Selecting Values now...")
    driver.find_element(By.XPATH, '//input[@value="0 - 5"]').click()
    time.sleep(2)

# Button click
driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
time.sleep(3)

# check the selection
chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
print(chk)
print("...Above is the selected value...")

# Selecting "Male" and "5-15"
ch1 = driver.find_element(By.XPATH,'//input[@value="Male"])[2]').is_selected()
if ch1:
    print("Already selected as male...")
else:
    print("Selecting male now")
    driver.find_element(By.XPATH, '//input[@value="Male"])[2]').click()
    time.sleep(2)

ch2 = driver.find_element(By.XPATH,'//input[@value="5 - 15"]').is_selected()
if ch2:
    print("Already selected as required...")
else:
    print("Selecting Values now...")
    driver.find_element(By.XPATH, '////input[@value="5 - 15"]').click()
    time.sleep(2)

# Button click
driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
time.sleep(3)

# check the selection
chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
print(chk)
print("...Above is the selected value...")

# Selecting sex as "Female" and age group as "15 to 50"
ch1 = driver.find_element(By.XPATH,'//input[@value="Female"])[2]').is_selected()
if ch1:
    print("Already selected as female...")
else:
    print("Selecting female now")
    driver.find_element(By.XPATH, '//div[@id="easycont"]/div/div[2]/div[2]/div[2]/div[1]/label[2]/input').click()
    time.sleep(2)

ch2 = driver.find_element(By.XPATH,'//input[@value="15 - 50"]').is_selected()
if ch2:
    print("Already selected as required...")
else:
    print("Selecting Values now...")
    driver.find_element(By.XPATH, '//input[@value="15 - 50"]').click()
    time.sleep(2)

# Button click
driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
time.sleep(3)

# check the selection
chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
print(chk)
print("...Above is the selected value...")

# Selecting "female" and "0-5"
ch1 = driver.find_element(By.XPATH,'//input[@value="Female"])[2]').is_selected()
if ch1:
    print("Already selected as female...")
else:
    print("Selecting female now")
    driver.find_element(By.XPATH, '//input[@value="Female"])[2]').click()
    time.sleep(2)

ch2 = driver.find_element(By.XPATH,'//input[@value="0 - 5"]').is_selected()
if ch2:
    print("Already selected as required...")
else:
    print("Selecting Values now...")
    driver.find_element(By.XPATH, '//input[@value="0 - 5"]').click()
    time.sleep(2)

# Button click
driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
time.sleep(3)

# check the selection
chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
print(chk)
print("...Above is the selected value...")

# Selecting "Female" and "5-15"
ch1 = driver.find_element(By.XPATH,'//input[@value="Female"])[2]').is_selected()
if ch1:
    print("Already selected as female...")
else:
    print("Selecting female now")
    driver.find_element(By.XPATH, '//input[@value="Female"])[2]').click()
    time.sleep(2)

ch2 = driver.find_element(By.XPATH,'//input[@value="5 - 15"]').is_selected()
if ch2:
    print("Already selected as required...")
else:
    print("Selecting Values now...")
    driver.find_element(By.XPATH, '//input[@value="5 - 15"]').click()
    time.sleep(2)

# Button click
driver.find_element(By.XPATH, '//button[text()="Get values"]').click()
time.sleep(3)

# check the selection
chk = driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]').text
print(chk)
print("...Above is the selected value...")

# close
driver.close()
