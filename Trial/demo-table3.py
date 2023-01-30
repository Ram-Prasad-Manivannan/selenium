# Necessary import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("...demo table 3 started...")

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

# Finding Table Filter
driver.find_element(By.XPATH, "//a[text()='Table Filter ']").click()
time.sleep(2)

# Total number of records in the display
tot = driver.find_elements(By.XPATH,"//tr")
totl = len(tot)
print("Total number of records in display: ",totl)

# Selecting Green button
# //div[@class='btn-group']/button[@class='btn btn-success btn-filter']
driver.find_element(By.XPATH, "//button[text()='Green']").click()
time.sleep(3)

# retrieving number of data
x1 = driver.find_elements(By.XPATH,"//span[text()='(Green)']")
print("Number of green data displayed: ",len(x1))
print("...Green data are as follows...")
x01 = driver.find_elements(By.XPATH,"//tr[@data-status='pagado']")
le = len(x01)+1
for i in range(1,le):
    print(driver.find_element(By.XPATH,f"(//tr[@data-status='pagado'])[{i}]").get_attribute("textContent"))

# Selecting Orange button
# //div[@class='btn-group']/button[@class='btn btn-warning btn-filter']
driver.find_element(By.XPATH, "//button[text()='Orange']").click()
time.sleep(3)

# retrieving number of data
x1 = driver.find_elements(By.XPATH,"//span[text()='(Orange)']")
print("Number of orange data displayed: ",len(x1))
print("...Orange data are as follows...")
x01 = driver.find_elements(By.XPATH,"//tr[@data-status='pendiente']")
le = len(x01)+1
for i in range(1,le):
    print(driver.find_element(By.XPATH,f"(//tr[@data-status='pendiente'])[{i}]").get_attribute("textContent"))

# Selecting Red button
# //div[@class='btn-group']/button[@class='btn btn-danger btn-filter']
driver.find_element(By.XPATH, "//button[text()='Red']").click()
time.sleep(3)

# retrieving number of data
x1 = driver.find_elements(By.XPATH,"//span[text()='(Red)']")
print("Number of red data displayed: ",len(x1))
print("...Red data are as follows...")
x01 = driver.find_elements(By.XPATH,"//tr[@data-status='cancelado']")
le = len(x01)+1
for i in range(1,le):
    print(driver.find_element(By.XPATH,f"(//tr[@data-status='cancelado'])[{i}]").get_attribute("textContent"))

# Selecting All button
# //div[@class='btn-group']/button[@class='btn btn-default btn-filter']
driver.find_element(By.XPATH, "//button[text()='All']").click()
time.sleep(3)

# retrieving number of data
x1 = driver.find_elements(By.XPATH,"//tr")
print("Number of All data displayed: ",len(x1))
print("...All data are as follows...")
x01 = driver.find_elements(By.XPATH,"//tr")
le = len(x01)+1
for i in range(1,le):
    print(driver.find_element(By.XPATH,f"(//tr)[{i}]").get_attribute("textContent"))
print("...Demo table 3 ended...")
# close
driver.close()
