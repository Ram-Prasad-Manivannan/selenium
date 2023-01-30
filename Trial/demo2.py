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

# Selecting Check Box Demo from listbox
driver.find_element(By.XPATH, '(//a[text()="Checkbox Demo"])[1]').click()
time.sleep(3)

# State of checkbox
state = driver.find_element(By.XPATH, '//input[@id="isAgeSelected"]').is_selected()

if state:
    print("Check box is already enabled...")
else:
    print("clicking on the check box now...")
    driver.find_element(By.XPATH, '//input[@id="isAgeSelected"]').click()
    time.sleep(3)

state = driver.find_element(By.XPATH, '//input[@id="isAgeSelected"]').is_selected()
if state:
    print("...Check box is selected successfully...")
else:
    print("...There is some error in the process... !!!xxx ERROR xxx!!!")

# Uncheck
print("...Unchecking the checkbox...")
driver.find_element(By.XPATH, '//input[@id="isAgeSelected"]').click()
time.sleep(3)

# Multiple check box
for i in range(1, 5):
    chk_xpath = f'//div[@id="easycont"]/div/div[2]/div[2]/div[2]/div[{i}]/label/input'
    sel = driver.find_element(By.XPATH, chk_xpath).is_selected()
    if sel:
        print("option", i, "is selected already")
    else:
        print("...Selecting option ", i, "Now...")
        driver.find_element(By.XPATH, chk_xpath).click()
        time.sleep(2)

        # checking to see if all are selected
        sel = driver.find_element(By.XPATH, chk_xpath).is_selected()
        if sel:
            print("option", i, "is selected successfully")

time.sleep(3)
# Click on the check all/uncheck all button  ????????
driver.find_element(By.XPATH, '//input[@id="check1"]').click()
time.sleep(10)

driver.close()
