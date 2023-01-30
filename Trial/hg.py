# Necessary import statements
# from python
import datetime
import time
import csv
# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

print("...demo table 4 started...")

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

# Finding Table Sort & Search
driver.find_element(By.XPATH, "//a[text()='Table Sort & Search']").click()
time.sleep(2)

# verify the page title
assert "Selenium Easy - Tabel Sort and Search Demo" in driver.title

# verify the table is present
table = driver.find_element(By.ID, "example")
assert table is not None

# verifying that it is the required table
a = table.get_attribute("class")
assert a == "display dataTable no-footer"

# assigning 50 as records per page for ease of access
ele = driver.find_element(By.XPATH, "//select[@name='example_length']")
ch = Select(ele)
ch.select_by_value("50")
time.sleep(2)


dat = []
column_name = ['Name','Position','Office','Age','Start date','Salary']

# ascending data

# initializing the lists
name = []
position = []
office = []
age = []
startdate = []
salary = []

# opening the csv file
with open('data.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile, delimiter=';')

    # extracting each data row one by one
    for row in csvreader:
        # adding columns to respective lists
        name.append(row[0])
        position.append(row[1])
        office.append(row[2])
        age.append(row[3])
        startdate.append(row[4])
        salary.append(row[5])

# ascending data
name_asc = sorted(name)
position_asc = sorted(position)
office_asc = sorted(office)
age_asc = sorted(age)

# descending data
name_des = sorted(name, reverse=True)
position_des = sorted(position, reverse=True)
office_des = sorted(office, reverse=True)
age_des = sorted(age, reverse=True)

# start date sort



# salary sort
#Ascending Order
salary_asc = sorted(salary,key=lambda x: int(x[1:].replace(",", "").replace("/y", "")))

#Descending Order
salary_des = sorted(salary,key=lambda x: int(x[1:].replace(",", "").replace("/y", "")), reverse=True)

name_act = []
name_act1 = []
# checking sort by name
# descending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Name']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[1]").text
    name_act.append(txt)

assert name_des == name_act

# ascending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Name']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[1]").text
    name_act1.append(txt)

assert name_act1 == name_asc

position_act = []
position_act2 = []
# ascending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Position']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[2]").text
    position_act.append(txt)

assert position_act == position_asc

# descending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Position']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[2]").text
    position_act2.append(txt)

assert position_act2 == position_des

office_act = []
office_act2 = []

# ascending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Office']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[3]").text
    office_act.append(txt)

assert office_act == office_asc

# descending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Office']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[3]").text
    office_act2.append(txt)

assert office_act2 == office_des

age_act = []
age_act1 = []
# ascending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Age']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[4]").text
    age_act.append(txt)

assert age_act == age_asc

# descending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Age']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[4]").text
    age_act1.append(txt)

assert age_act1 == age_des

startdate_act = []
startdate_act1 = []
# ascending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Start date']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[5]").text
    startdate_act.append(txt)

#assert startdate_act == startdate_asc

# descending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Start date']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[5]").text
    startdate_act1.append(txt)

#assert startdate_act1 == startdate_des

salary_act = []
salary_act1 = []
# ascending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Salary']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[6]").text
    salary_act.append(txt)

assert salary_act == salary_asc

# descending:
driver.find_element(By.XPATH,f"//thead/tr/th[text()='Salary']").click()
ele = driver.find_elements(By.XPATH, "//tbody/tr")
le = len(ele) + 1
for m in range(1,le):
    txt = driver.find_element(By.XPATH, f"//tbody/tr[{m}]/td[6]").text
    salary_act1.append(txt)

assert salary_act1 == salary_des

print("sorting is verified column by column except start date")
