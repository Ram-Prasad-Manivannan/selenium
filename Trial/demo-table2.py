# Necessary import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

print("...demo table 2 started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(2)

# Maximize
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# Finding Table
# driver.find_element(By.XPATH, "//a[text()='Table']").click()
driver.find_element(By.XPATH, "(//li[@class='dropdown'])[3]/a").click()
time.sleep(2)

# Finding Table Data Search
driver.find_element(By.XPATH, "//a[text()='Table Data Search']").click()
time.sleep(2)

# table 1
print("displaying all rows of table 1:")
for i in range(1,8):
    print(driver.find_element(By.XPATH,f"//tbody/tr[{i}]").text)

# enabling the filter option
driver.find_element(By.XPATH, "//input[@id='task-table-filter']").click()
driver.find_element(By.XPATH, "//input[@id='task-table-filter']").send_keys("c")
time.sleep(2)

print("displaying all rows of table 1 containing 'c' :")

listed_count = driver.find_elements(By.XPATH, "//table[@id='task-table']//tbody//tr[*]")
print("Row is printed")
print("Listed Rows -:- " ,len(listed_count))

for sizeOf in range(len(listed_count)):
    sizeOf = sizeOf+1

    attri = driver.find_element(By.XPATH, f"//table[@id='task-table']//tbody//tr[{sizeOf}]").get_attribute("style")
    print("Current Row Attribute =:= ", attri)

    if attri.__eq__("display: none;"):
        print(f"Row {sizeOf} Data is Not Available")
    else:
        ele = driver.find_element(By.XPATH, f"//table[@id='task-table']//tbody//tr[{sizeOf}]").text
        print(f"Row {sizeOf} Retrieved Details -:- ", ele)


# eles = driver.find_element(By.XPATH,"//tbody/tr[contains(@style,'display:')][1]")
# print("Table Row Is Retrieved -:- ", eles.text)
# ele = driver.find_elements(By.XPATH,"//tbody/tr[@style='display: table-row;']")
# for e in ele:
#     print(e.text)
#

#time.sleep(120)

