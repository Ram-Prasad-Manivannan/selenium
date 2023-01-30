# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# main program
print("...data filter started...")

# Driver initiation
driver = webdriver.Chrome()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://demo.seleniumeasy.com/data-list-filter-demo.html")

# Verify title
assert driver.title == "Selenium Easy - Data list Filter demo"

# verify header
head = driver.find_element(By.XPATH,"//h2").text
assert head == "Data List Filter"

# verify list of searchable items:

# number
x = driver.find_elements(By.XPATH,"//div[@class='searchable-container']/div/div")
no = len(x)+1
assert no == 7

# name
name = []
ac_name = ['Tyreese Burn', 'Brenda Tree', 'Glenn Pho shizzle', 'Brian Hoyies', 'Glenn Pho shizzle', 'Arman Cheyia']
for i in range(1,no):
    tx = driver.find_element(By.XPATH,f"//div[@class='searchable-container']/div[{i}]/div/h4")
    name.append(tx.text)
    for ik, ele in enumerate(name):
        name[ik] = ele.replace('Name: ', '')
assert name == ac_name

# phone
ph = []
ac_ph = ['321-456-1111', '644-555-2222', '980-543-3333', '564-234-4444', '555-454-5555', '234-555-6666']
for i in range(1,no):
    tx = driver.find_element(By.XPATH,f"//div[@class='searchable-container']/div[{i}]/div/span[1]")
    ph.append(tx.text)
    for ik, ele in enumerate(ph):
        ph[ik] = ele.replace('Phone: ', '').strip(",")
assert ph == ac_ph

# mail
ma = []
ac_ma = ['test1@company.com', 'test2@company.com', 'test3@company.com', 'test4@company.com',
         'test5@company.com', 'test6@company.com']
for i in range(1,no):
    tx = driver.find_element(By.XPATH,f"//div[@class='searchable-container']/div[{i}]/div/span[2]")
    ma.append(tx.text)
    for ik, ele in enumerate(ma):
        ma[ik] = ele.replace('Email: ', '')
assert ma == ac_ma

# Title
ti = []
ac_ti = ['Manager', 'Manager', 'Manager', 'Manager', 'Manager', 'Manager']
for i in range(1,no):
    tx = driver.find_element(By.XPATH,f"//div[@class='searchable-container']/div[{i}]/div/p")
    ti.append(tx.text)
    for ik, ele in enumerate(ti):
        ti[ik] = ele.replace('Title: ', '')
assert ti == ac_ti

# Company Name
CN = []
ac_cn = ['Company Name', 'Company Name', 'Company Name', 'Company Name', 'Company Name', 'Company Name']
for i in range(1,no):
    tx = driver.find_element(By.XPATH,f"//div[@class='searchable-container']/div[{i}]/div/h5")
    CN.append(tx.text)
assert CN == ac_cn

# Search
driver.find_element(By.ID,"input-search").send_keys("b")
time.sleep(1)

# result

# number
ele = driver.find_elements(By.XPATH,"//div[@class='searchable-container']/div[@style='display: block;']")
no = len(ele)+1
assert no == 4

# name
li = []
ac_li = ['Tyreese Burn', 'Brenda Tree', 'Brian Hoyies']
for i in range(1,no):
    t = driver.find_element(By.XPATH,f"//div[@class='searchable-container']/div[@style='display: block;'][{i}]/div/h4")
    li.append(t.text)
    for ik, ele in enumerate(li):
        li[ik] = ele.replace('Name: ', '')
assert ac_li == li

# to clear search
driver.refresh()
time.sleep(2)

# Search again
driver.find_element(By.ID,"input-search").send_keys("rees")
time.sleep(1)

# verify through number
ele = driver.find_elements(By.XPATH,"//div[@class='searchable-container']/div[@style='display: block;']")
no = len(ele)+1
assert no == 2

# verify through text
res = driver.find_element(By.XPATH,"//div[@class='searchable-container']/div[@style='display: block;']/div/h4").text
# res = res.replace('Name: ','')  #this also works
res = res.strip("Name: ")
assert res == "Tyreese Burn"

print("...data filter ended...")

# close
driver.close()