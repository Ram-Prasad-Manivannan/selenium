# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# main program
print("...exe1 started...")

# Driver initiation
driver = webdriver.Chrome()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://demo.seleniumeasy.com/")

# List Box
# driver.find_element(By.XPATH, "//a[text()='List Box']").click()
driver.find_element(By.XPATH, "(//li[@class='dropdown'])[6]/a").click()
time.sleep(2)

# JQuery List Box
driver.find_element(By.XPATH,"//a[text()='JQuery List Box']").click()
time.sleep(2)

# verify list through numbers and text
xx = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickData']/option")
le = len(xx)+1
assert le == 16

li = []
ac_li = ['Isis', 'Sophia', 'Alice', 'Isabella', 'Manuela', 'Laura', 'Luiza', 'Valentina', 'Giovanna',
         'Maria Eduarda', 'Helena', 'Beatriz', 'Maria Luiza', 'Lara', 'Julia']

for i in range(1,le):
    xxx = driver.find_element(By.XPATH,f"//select[@class='form-control pickListSelect pickData']/option[{i}]")
    li.append(xxx.text)
assert li == ac_li

# verify empty of 2nd list
x = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option")
lll = len(x)
assert lll == 0

# empty add
driver.find_element(By.XPATH,"//button[@class='pAdd btn btn-primary btn-sm']").click()

# verify empty again
x = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option")
lll = len(x)
assert lll == 0

# selecting from list
ele = driver.find_element(By.XPATH,"//select[@class='form-control pickListSelect pickData']")
drop = Select(ele)
drop.select_by_index(2)

# click add
driver.find_element(By.XPATH,"//button[@class='pAdd btn btn-primary btn-sm']").click()
time.sleep(4)

# verify
t = driver.find_element(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option").text
assert t == "Alice"
# getting options from list:
options = ele.find_elements(By.TAG_NAME,"option")
for option in options:
    if option.text == "Alice":
        flag = "error"
    else:
        flag = "pass"
# noinspection PyUnboundLocalVariable
assert flag == "pass"

# empty remove
driver.find_element(By.XPATH,"//button[@class='pRemove btn btn-primary btn-sm']").click()

# verify again
t = driver.find_element(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option").text
assert t == "Alice"

# select option to remove
driver.find_element(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option").click()

# remove
driver.find_element(By.XPATH,"//button[@class='pRemove btn btn-primary btn-sm']").click()
time.sleep(2)

# verify remove
# first verify emptiness of 2nd list
x = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option")
lll = len(x)
assert lll == 0

# element is back in 1st list
# getting options from list:
options = ele.find_elements(By.TAG_NAME,"option")
for option in options:
    if option.text == "Alice":
        flag = "pass"
    else:
        flag = "error"
assert flag == "pass"

# selecting multiple elements from list 1:
drop.select_by_visible_text("Valentina")
drop.select_by_visible_text("Beatriz")
drop.select_by_visible_text("Julia")
drop.select_by_visible_text("Sophia")

# click add button:
driver.find_element(By.XPATH,"//button[@class='pAdd btn btn-primary btn-sm']").click()
time.sleep(3)

# verify the operation
# list 2 contains all selected option
# through number
x = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option")
lll = len(x)
assert lll == 4
# through text
lii = []
act_lii = ['Sophia', 'Valentina', 'Beatriz', 'Julia']
for i in range(1,lll+1):
    tx = driver.find_element(By.XPATH,f"//select[@class='form-control pickListSelect pickListResult']/option[{i}]").text
    lii.append(tx)
assert lii == act_lii

# list 1 does not contain selected options
options = ele.find_elements(By.TAG_NAME,"option")
for option in options:
    # not exactly correct get list append it and compare list
    if option.text not in ['Sophia', 'Valentina', 'Beatriz', 'Julia']:
        flag = "pass"
    else:
        flag = "error"
assert flag == "pass"

# selecting 2 from list 2 to remove:
ele1 = driver.find_element("//select[@class='form-control pickListSelect pickListResult']")
drop1 = Select(ele1)
drop1.select_by_visible_text("Sophia")
drop1.select_by_visible_text("Beatriz")

driver.find_element(By.XPATH,"//button[@class='pRemove btn btn-primary btn-sm']").click()
time.sleep(2)

# verify remove
# first verify numbers of 2nd list
x = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option")
lll = len(x)
assert lll == 2
# by text
options1 = ele1.find_elements(By.TAG_NAME,"option")
for option in options1:
    if option.text not in ['Sophia', 'Beatriz']:
        flag = "pass"
    else:
        flag = "error"
assert flag == "pass"
# element is back in 1st list
# getting options from list:
options = ele.find_elements(By.TAG_NAME,"option")
for option in options:
    if option.text in ['Sophia', 'Beatriz']:  # not exactly correct get list append it and compare list
        flag = "pass"
    else:
        flag = "error"
assert flag == "pass"


# click on remove all button:
driver.find_element(By.XPATH,"//button[@class='pRemoveAll btn btn-primary btn-sm']").click()
time.sleep(3)

# verify 2nd empty
x = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option")
lll = len(x)
assert lll == 0

# verify elements in list 1
options = ele.find_elements(By.TAG_NAME,"option")
for option in options:
    if option.text in ['Valentina', 'Julia']:
        flag = "pass"
    else:
        flag = "error"
assert flag == "pass"

# click add all:
driver.find_element(By.XPATH,"//button[@class='pAddAll btn btn-primary btn-sm']").click()
time.sleep(5)

# verify null on list 1
xx = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickData']/option")
le = len(xx)
assert le == 0

# verify list 2
# number
xx = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option")
le = len(xx)+1
assert le == 16
# text
li1 = []
for i in range(1,le):
    xxx = driver.find_element(By.XPATH,f"//select[@class='form-control pickListSelect pickListResult']/option[{i}]")
    li1.append(xxx.text)
assert li1 == ac_li

# click on remove all button:
driver.find_element(By.XPATH,"//button[@class='pRemoveAll btn btn-primary btn-sm']").click()
time.sleep(5)

# verify empty of 2nd list
x = driver.find_elements(By.XPATH,"//select[@class='form-control pickListSelect pickListResult']/option")
lll = len(x)
assert lll == 0
