# Necessary import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("...demo table 2 started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(2)

# Maximize
driver.maximize_window()

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
    print(driver.find_element(By.XPATH,f"//table[@id='task-table']/tbody/tr[{i}]").text)

# enabling the filter option
driver.find_element(By.XPATH, "//input[@id='task-table-filter']").click()
driver.find_element(By.XPATH, "//input[@id='task-table-filter']").send_keys("c")
time.sleep(2)

print("displaying all rows of table 1 containing 'c' :")

# try 1
ele = driver.find_elements(By.XPATH, "//table[@id='task-table']//tbody/tr[not(@style)]")
leng = len(ele)+1
print("Length = ", leng-1)
for i in range(1,leng):
    print(driver.find_element(By.XPATH, f"(//table[@id='task-table']//tbody/tr[not(@style)])[{i}]").text)

# try 2
ele = driver.find_elements(By.XPATH, "(//table[@id='task-table']/tbody/tr[@style='display: none;'])")
leng = len(ele)+1
print("input is not in total of rows",leng-1)
for i in range(1,leng):
    print(driver.find_element(By.XPATH, f"//table[@id='task-table']/tbody/tr[@style='display: none;'][{i}]")
          .get_attribute("textContent"))

# # try 3
# ele = driver.find_elements(By.XPATH, "(//table[@id='task-table']//tbody//tr[*]")
# length = len(ele)
# print("Rows are : ",length)
# for i in range(1,length):
#     print(driver.find_element(By.XPATH,f"(//table[@id='task-table']/tbody/tr[{i}]").text)

print("Printing data with only one filter applied")
x1 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[not(@style)]")
l0 = len(x1)+1
print("The Number of rows in 2nd table: ",len(x1))

print("2 nd table turning filter on...")
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-xs btn-filter']").click()
time.sleep(2)

print("input 2 in 1st filter....")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[1]/input").send_keys("2")
time.sleep(4)

print("Printing data after applying 1st filter...")
print(driver.find_element(By.XPATH,"//table[@class='table']/tbody/tr[not(@style)]").text)

print("clearing the filter...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[1]/input").clear()
time.sleep(1)

print("Entering data in 2nd filter only....")
driver.find_element(By.XPATH,"//table/thead/tr/th[2]/input").send_keys("k")
time.sleep(5)

x2 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l1 = len(x2)+1
print("After 2nd filter total rows: ",len(x2))
print("Printing data accordingly....")
for i in range(1,l1):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing the filter...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[2]/input").clear()
time.sleep(1)

print("input B in 3rd filter aka first name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[3]/input").send_keys("B")
time.sleep(1)

x3 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l2 = len(x3)+1
print("After 3rd filter total rows: ",len(x3))
print("Printing data accordingly....")
for i in range(1,l2):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing 3rd filter aka first name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[3]/input").clear()
time.sleep(1)

print("input S in 4th filter aka last name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[4]/input").send_keys("S")
time.sleep(1)

x4 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l3 = len(x4)+1
print("After 3rd filter total rows: ",len(x4))
print("Printing data accordingly....")
for i in range(1,l3):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing 4th filter aka last name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[4]/input").clear()
time.sleep(1)

print("Using two filters at the same time...")

print("Entering data in 2nd filter aka Username....")
driver.find_element(By.XPATH,"//table/thead/tr/th[2]/input").send_keys("m")
time.sleep(5)

print("input o in 3rd filter aka first name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[3]/input").send_keys("o")
time.sleep(1)

x5 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l4 = len(x5)+1
print("Total no of rows after applying filter...",len(x5))
print("printing data after applying filter...")
for i in range(1,l4):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing the 2nd filter...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[2]/input").clear()
time.sleep(1)

print("clearing 3rd filter aka first name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[3]/input").clear()
time.sleep(1)

print("Applying 3rd and 4th filter")

print("input o in 3rd filter aka first name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[3]/input").send_keys("o")
time.sleep(1)

print("input o in 4th filter aka last name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[4]/input").send_keys("o")
time.sleep(1)

x6 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l5 = len(x6)+1
print("Total no of rows after applying filter...",len(x6))
print("printing data after applying filter...")
for i in range(1,l5):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing 3rd filter aka first name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[3]/input").clear()
time.sleep(1)

print("clearing 4th filter aka last name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[4]/input").clear()
time.sleep(1)

print("Applying 2nd and 4th filter")

print("Entering data in 2nd filter aka Username....")
driver.find_element(By.XPATH,"//table/thead/tr/th[2]/input").send_keys("m")
time.sleep(5)

print("input o in 4th filter aka last name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[4]/input").send_keys("o")
time.sleep(1)

x7 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l6 = len(x7)+1
print("Total no of rows after applying filter...",len(x7))
print("printing data after applying filter...")
for i in range(1,l6):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing 2nd filter aka first name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[2]/input").clear()
time.sleep(1)

print("clearing 4th filter aka last name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[4]/input").clear()
time.sleep(1)

print("...1 and 2...")
print("input 4 in 1st filter....")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[1]/input").send_keys("4")
time.sleep(4)

print("Entering data in 2nd filter....")
driver.find_element(By.XPATH,"//table/thead/tr/th[2]/input").send_keys("m")
time.sleep(5)

x8 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l7 = len(x8)+1
print("After two filters total rows: ",len(x8))
print("Printing data accordingly....")
for i in range(1,l7):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing the filter...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[2]/input").clear()
time.sleep(1)

print("Not getting expected output but , This logic works too... ")

print("...1 and 3...")
print("Entering data in 3rd filter....")
driver.find_element(By.XPATH,"//table/thead/tr/th[3]/input").send_keys("o")
time.sleep(5)

x9 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l8 = len(x9)+1
print("After two filters total rows: ",len(x9))
print("Printing data accordingly....")
for i in range(1,l8):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing the filter...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[3]/input").clear()
time.sleep(1)

print("Not getting expected output but , This logic works too... ")

print("...1 and 4...")

print("input o in 4th filter aka last name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[4]/input").send_keys("o")
time.sleep(1)

x10 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l9 = len(x10)+1
print("After two filters total rows: ",len(x10))
print("Printing data accordingly....")
for i in range(1,l9):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("clearing 4th filter aka last name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[4]/input").clear()
time.sleep(1)

print("...applying 3 filters...","1 2 and 3")

print("Entering data in 2nd filter aka Username....")
driver.find_element(By.XPATH,"//table/thead/tr/th[2]/input").send_keys("m")
time.sleep(5)

print("input o in 3rd filter aka first name...")
driver.find_element(By.XPATH, "//table[@class='table']/thead/tr/th[3]/input").send_keys("o")
time.sleep(1)

x11 = driver.find_elements(By.XPATH,"//table[@class='table']/tbody/tr[@style='display: table-row;']")
l10 = len(x11)+1
print("Total no of rows after applying filter...",len(x11))
print("printing data after applying filter...")
for i in range(1,l10):
    print(driver.find_element(By.XPATH, f"//table[@class='table']/tbody/tr[@style='display: table-row;'][{i}]").text)

print("...Demo table 2 is a success...")

# close
driver.close()
