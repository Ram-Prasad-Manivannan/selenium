# Necessary import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("...demo table 1 started...")

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

# Finding Table Pagination
driver.find_element(By.XPATH, "//a[text()='Table Pagination']").click()
time.sleep(2)

# pg 1 data table print one by one(only body)
print("only row 1")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[1]/td[{i}]").text)

print(driver.find_element(By.XPATH, "//tbody[@id='myTable']/tr[1]").text)

print("only row 2")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[2]/td[{i}]").text)

print(driver.find_element(By.XPATH, "//tbody[@id='myTable']/tr[2]").text)

print("only row 3")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[3]/td[{i}]").text)

print(driver.find_element(By.XPATH, "//tbody[@id='myTable']/tr[3]").text)

print("only row 4")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[4]/td[{i}]").text)

print(driver.find_element(By.XPATH, "//tbody[@id='myTable']/tr[4]").text)

print("only row 5")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[5]/td[{i}]").text)

print(driver.find_element(By.XPATH, "//tbody[@id='myTable']/tr[5]").text)

# trying to print 6th row
print("trying to print row 6")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[6]/td[{i}]").text)

print("all rows in pg 1 one by one")
for i in range(1,6):
    for j in range(1,8):
        print(i,j,"info")
        print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[{j}]").text)

print("all rows in pg 1 in line")
for i in range(1,6):
    print(i,"info")
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[{i}]").text)

print("only column 1")
for i in range(1,6):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[1]").text)

print("only column 2")
for i in range(1,6):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[2]").text)

print("only column 3")
for i in range(1,6):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[3]").text)

print("only column 4")
for i in range(1,6):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[4]").text)

print("only column 5")
for i in range(1,6):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[5]").text)

print("only column 6")
for i in range(1,6):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[6]").text)

print("only column 7")
for i in range(1,6):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[7]").text)

# move to next page: click on the next button i.e. >>
driver.find_element(By.XPATH, "//a[@class='next_link']").click()
print("...Moving to page 2...")

# trying to print 6th row again  HOW TO ASSERT NONE????
print("trying to print row 6 again")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[6]/td[{i}]").text)

print("print row 7")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[7]/td[{i}]").text)

print("print row 8")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[8]/td[{i}]").text)

print("print row 9")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[9]/td[{i}]").text)

print("print row 10")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[10]/td[{i}]").text)

# trying to print 11th row
print("trying to print row 11")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[11]/td[{i}]").text)

# trying to print 1st row again
print("trying to print row 1 again")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[1]/td[{i}]").text)

print("all rows in pg 2")
for i in range(6,11):
    for j in range(1,8):
        print(i,j,"info")
        print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[{j}]").text)

# move to previous page: click on the prev button i.e. <<
driver.find_element(By.XPATH, "//a[@class='prev_link']").click()
print("...Moving to page 1 again...")

# trying to print 1st row again
print("trying to print row 1 again")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[1]/td[{i}]").text)

# move to last page through page link 3
print("moving to page 3...")
driver.find_element(By.XPATH, "//a[text()='3']").click()

# trying to print 11th row again
print("trying to print row 11 again")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[11]/td[{i}]").text)

# trying to print 6th row again
print("trying to print row 6 again")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[6]/td[{i}]").text)

# trying to print 1st row again
print("trying to print row 1 again")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[1]/td[{i}]").text)

print("print row 12")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[12]/td[{i}]").text)

print("print row 13")
for i in range(1,8):
    print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']/tr[13]/td[{i}]").text)

print("all rows in pg 3")
for i in range(11,14):
    for j in range(1,8):
        print(i,j,"info")
        print(driver.find_element(By.XPATH, f"//tbody[@id='myTable']//tr[{i}]//td[{j}]").text)

# close
print("...Closing demo table 1...")
driver.close()
