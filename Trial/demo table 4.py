# Necessary import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

# Finding Table Sort & Search
driver.find_element(By.XPATH, "//a[text()='Table Sort & Search']").click()
time.sleep(2)

# Total records
tot = driver.find_element(By.XPATH, "//div[@id='example_info']").text

rec = tot.split("of ")[1]
print("Total number of records :", rec)

act = rec.split("entries")[0].strip()
print(act)
act = int(act)
assert act == 32

ele = driver.find_element(By.XPATH, "//select[@name='example_length']")
ch = Select(ele)
ch.select_by_value("50")
time.sleep(2)
#
#
# total = driver.find_elements(By.XPATH,"//tbody/tr")
# total1 = len(total)
#
# assert act == total1
# # getting numbers from string
# ints = [eval(x) for x in rec]
# print(ints)

# # using List comprehension + isdigit() +split()
# # getting numbers from string
# res = [int(i) for i in rec.split() if i.isdigit()]
# print(res)

# Number of Records per page
# ele = driver.find_element(By.XPATH, "//select[@name='example_length']")
# ch = Select(ele)
# ch.select_by_value("50")
# time.sleep(5)

# Searching

# sort name:
list0 = ["A. Cox","A. Ramos","A. Satou","B. Greer","B. Wagner","B. Williamson","C. Hurst","C. Kelly","C. Marshall",
         "C. Vance","D. Rios","D. Wilder","F. Green","G. Joyce","G. Little","G. Winters","H. Chandler","H. Kennedy",
         "J. Caldwell","J. Chang","J. Gaines","M. House","M. Silva","P. Byrd","Q. Flynn","R. Davidson","S. Burks",
         "S. Frost","S. Itou","T. Fitzpatrick","T. Nixon","Y. Berry"]

list1 = [],list2 = []

for i in range(1,33):
    text = driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[1]").text
    list1.append(text)

assert list0 == list1
# reverse list
list0.reverse()

driver.find_element(By.XPATH,"//thead/tr/th[1]").click()
time.sleep(3)
for i in range(1,33):
    text = driver.find_element(By.XPATH,f"//tbody/tr[{i}]/td[1]").text
    list2.append(text)

assert list2 == list0

