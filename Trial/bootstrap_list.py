# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Bootstrap List Box
driver.find_element(By.XPATH,"//a[text()='Bootstrap List Box']").click()
time.sleep(2)

# list verify
act_li_l = ['bootstrap-duallist', 'Dapibus ac facilisis in', 'Morbi leo risus',
            'Porta ac consectetur ac', 'Vestibulum at eros']
act_li_r = ['Cras justo odio', 'Dapibus ac facilisis in', 'Morbi leo risus',
            'Porta ac consectetur ac', 'Vestibulum at eros']

left_li = []
right_li = []
left_ele = driver.find_elements(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/ul/li")
right_ele = driver.find_elements(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/ul/li")
l_x = len(left_ele)+1
r_x = len(right_ele)+1
for i in range(1,l_x):
    left_l = driver.find_element(By.XPATH,f"//div[@class='dual-list list-left col-md-5']/div/ul/li[{i}]").text
    left_li.append(left_l)
for i in range(1,r_x):
    right_l = driver.find_element(By.XPATH,f"//div[@class='dual-list list-right col-md-5']/div/ul/li[{i}]").text
    right_li.append(right_l)

assert act_li_l == left_li
assert act_li_r == right_li

# check box:
# left:
# unchecked on start verify
x = driver.find_element(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/div/div[2]/div/a/i")\
    .get_attribute("class")
assert x == "glyphicon glyphicon-unchecked"

# click on check box
driver.find_element(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/div/div[2]/div/a").click()

# check box is selected verify
x1 = driver.find_element(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/div/div[2]/div/a/i")\
    .get_attribute("class")
assert x1 == "glyphicon glyphicon-check"

# all listed elements are selected verify
mu_ele = driver.find_elements(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/ul/li")
lll = len(mu_ele)+1
for i in range(1,lll):
    el = driver.find_element(By.XPATH,f"//div[@class='dual-list list-left col-md-5']/div/ul/li[{i}]")\
        .get_attribute("class")
    assert el == "list-group-item active"

# right:
# unchecked on start verify
x = driver.find_element(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/div/div/div/a/i")
assert x.get_attribute("class") == "glyphicon glyphicon-unchecked"

# click on check box
driver.find_element(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/div/div/div/a/i").click()

# check box is selected verify
x1 = driver.find_element(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/div/div/div/a/i")
assert x1.get_attribute("class") == "glyphicon glyphicon-check"

# all listed elements are selected verify
mu_ele = driver.find_elements(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/ul/li")
lll = len(mu_ele)+1
for i in range(1,lll):
    el = driver.find_element(By.XPATH,f"//div[@class='dual-list list-right col-md-5']/div/ul/li[{i}]")\
        .get_attribute("class")
    assert el == "list-group-item active"

# Unchecking operation verify
# left
# click on check box
driver.find_element(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/div/div[2]/div/a").click()

# check box is not selected verify
x1 = driver.find_element(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/div/div[2]/div/a/i")\
    .get_attribute("class")
assert x1 == "glyphicon glyphicon-unchecked"

# all listed elements are un selected verify
mu_ele = driver.find_elements(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/ul/li")
lll = len(mu_ele)+1
for i in range(1,lll):
    el = driver.find_element(By.XPATH,f"//div[@class='dual-list list-left col-md-5']/div/ul/li[{i}]")\
        .get_attribute("class")
    assert el == "list-group-item"

# right
# click on check box
driver.find_element(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/div/div/div/a/i").click()

# check box is not selected verify
x1 = driver.find_element(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/div/div/div/a/i")\
    .get_attribute("class")
assert x1 == "glyphicon glyphicon-unchecked"

# all listed elements are un selected verify
mu_ele = driver.find_elements(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/ul/li")
lll = len(mu_ele)+1
for i in range(1,lll):
    el = driver.find_element(By.XPATH,f"//div[@class='dual-list list-right col-md-5']/div/ul/li[{i}]")\
        .get_attribute("class")
    assert el == "list-group-item"

# checking selection of elements one by one in the list
s_el_le = driver.find_elements(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/ul/li")
s_el_ri = driver.find_elements(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/ul/li")
l_s_el_le = len(s_el_le)+1
l_s_el_ri = len(s_el_ri)+1
for i in range(1,l_s_el_le):
    driver.find_element(By.XPATH,f"//div[@class='dual-list list-left col-md-5']/div/ul/li[{i}]").click()
    ch = driver.find_element(By.XPATH,f"//div[@class='dual-list list-left col-md-5']/div/ul/li[{i}]")
    assert ch.get_attribute("class") == "list-group-item active"
    driver.find_element(By.XPATH, f"//div[@class='dual-list list-left col-md-5']/div/ul/li[{i}]").click()
    ch = driver.find_element(By.XPATH, f"//div[@class='dual-list list-left col-md-5']/div/ul/li[{i}]")
    assert ch.get_attribute("class") == "list-group-item"
for i in range(1,l_s_el_ri):
    driver.find_element(By.XPATH,f"//div[@class='dual-list list-right col-md-5']/div/ul/li[{i}]").click()
    ch = driver.find_element(By.XPATH,f"//div[@class='dual-list list-right col-md-5']/div/ul/li[{i}]")
    assert ch.get_attribute("class") == "list-group-item active"
    driver.find_element(By.XPATH, f"//div[@class='dual-list list-right col-md-5']/div/ul/li[{i}]").click()
    ch = driver.find_element(By.XPATH, f"//div[@class='dual-list list-right col-md-5']/div/ul/li[{i}]")
    assert ch.get_attribute("class") == "list-group-item"

time.sleep(1)

# two or more selected???
# left
a1 = driver.find_element(By.XPATH,f"//div[@class='dual-list list-left col-md-5']/div/ul/li[1]")
a2 = driver.find_element(By.XPATH,f"//div[@class='dual-list list-left col-md-5']/div/ul/li[3]")
a3 = driver.find_element(By.XPATH,f"//div[@class='dual-list list-left col-md-5']/div/ul/li[5]")
a1.click()
a2.click()
a3.click()
assert a1.get_attribute("class") == "list-group-item active"
assert a2.get_attribute("class") == "list-group-item active"
assert a3.get_attribute("class") == "list-group-item active"
a1.click()
a2.click()
a3.click()
assert a1.get_attribute("class") == "list-group-item"
assert a2.get_attribute("class") == "list-group-item"
assert a3.get_attribute("class") == "list-group-item"

# right
a1 = driver.find_element(By.XPATH,f"//div[@class='dual-list list-right col-md-5']/div/ul/li[1]")
a2 = driver.find_element(By.XPATH,f"//div[@class='dual-list list-right col-md-5']/div/ul/li[2]")
a3 = driver.find_element(By.XPATH,f"//div[@class='dual-list list-right col-md-5']/div/ul/li[5]")
a1.click()
a2.click()
a3.click()
assert a1.get_attribute("class") == "list-group-item active"
assert a2.get_attribute("class") == "list-group-item active"
assert a3.get_attribute("class") == "list-group-item active"
a1.click()
a2.click()
a3.click()
assert a1.get_attribute("class") == "list-group-item"
assert a2.get_attribute("class") == "list-group-item"
assert a3.get_attribute("class") == "list-group-item"

sea_le_li = []
sea_ri_li = []
act_s_le_li = ['Dapibus ac facilisis in', 'Porta ac consectetur ac']
act_s_ri_li = ['Morbi leo risus', 'Vestibulum at eros']


# search 1
driver.find_element(By.NAME,"SearchDualList").send_keys("ac")
time.sleep(2)
muel = driver.find_elements(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/ul/li[not(@style)]")
l_mu = len(muel)+1
for i in range(1,l_mu):
    xx = driver.find_element(By.XPATH, f"//div[@class='dual-list list-left col-md-5']/div/ul/li[not(@style)][{i}]")
    sea_le_li.append(xx.text)

assert sea_le_li == act_s_le_li

# search 2
# //div[@class='dual-list list-right col-md-5']/div/div/div[2]/div/input
driver.find_element(By.XPATH,"(//input[@name='SearchDualList'])[2]").send_keys("m")
time.sleep(2)
muel = driver.find_elements(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/ul/li[not(@style)]")
l_mu = len(muel)+1
for i in range(1,l_mu):
    xx = driver.find_element(By.XPATH, f"//div[@class='dual-list list-right col-md-5']/div/ul/li[not(@style)][{i}]")
    sea_ri_li.append(xx.text)
assert sea_ri_li == act_s_ri_li

# moving one or two element:
# selecting from left
driver.find_element(By.XPATH,"(//div[@class='dual-list list-left col-md-5']/div/ul/li[not(@style)])[1]").click()

# clicking button >
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm move-right']").click()

mov_right_ele = []
act_right_ele = ['Morbi leo risus', 'Vestibulum at eros', 'Dapibus ac facilisis in']

# checking if the element is moved through numbers and text
muel = driver.find_elements(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/ul/li[not(@style)]")
l_mu = len(muel)+1
assert l_mu == 4
for i in range(1,l_mu):
    xx = driver.find_element(By.XPATH, f"//div[@class='dual-list list-right col-md-5']/div/ul/li[not(@style)][{i}]")
    mov_right_ele.append(xx.text)
assert mov_right_ele == act_right_ele

# selecting from right
driver.find_element(By.XPATH,"(//div[@class='dual-list list-right col-md-5']/div/ul/li[not(@style)])[1]").click()

# clicking button <
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm move-left']").click()

mov_left_ele = []
act_left_ele = ['Porta ac consectetur ac', 'Morbi leo risus', 'Dapibus ac facilisis in']

# checking if the element is moved through numbers and text
muel = driver.find_elements(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/ul/li[not(@style)]")
l_mu = len(muel)+1
assert l_mu == 4
for i in range(1,l_mu):
    xx = driver.find_element(By.XPATH, f"//div[@class='dual-list list-left col-md-5']/div/ul/li[not(@style)][{i}]")
    mov_left_ele.append(xx.text)
assert mov_left_ele == act_left_ele

driver.refresh()
time.sleep(2)

# selecting all from left
# click on check box
driver.find_element(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/div/div[2]/div/a").click()

# clicking on > button
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm move-right']").click()

# verify the move through numbers and text
muel = driver.find_elements(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/ul/li")
lmu = len(muel)+1
assert lmu == 11

act = ['Cras justo odio', 'Dapibus ac facilisis in', 'Morbi leo risus', 'Porta ac consectetur ac',
       'Vestibulum at eros', 'bootstrap-duallist', 'Dapibus ac facilisis in', 'Morbi leo risus',
       'Porta ac consectetur ac', 'Vestibulum at eros']

res = []
for i in range(1,lmu):
    xxx = driver.find_element(By.XPATH, f"//div[@class='dual-list list-right col-md-5']/div/ul/li[{i}]")
    res.append(xxx.text)
assert res == act

# verify left empty
muel = driver.find_elements(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/ul/li")
lmu = len(muel)
assert lmu == 0

# selecting all from right
# click on check box
driver.find_element(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/div/div/div/a/i").click()

# click on <
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-sm move-left']").click()

# verify the move through numbers and text
muel = driver.find_elements(By.XPATH,"//div[@class='dual-list list-left col-md-5']/div/ul/li")
lmu = len(muel)+1
assert lmu == 11

act2 = ['Cras justo odio', 'Dapibus ac facilisis in', 'Morbi leo risus', 'Porta ac consectetur ac',
        'Vestibulum at eros', 'bootstrap-duallist', 'Dapibus ac facilisis in', 'Morbi leo risus',
        'Porta ac consectetur ac', 'Vestibulum at eros']

res2 = []
for i in range(1,lmu):
    xxx = driver.find_element(By.XPATH, f"//div[@class='dual-list list-left col-md-5']/div/ul/li[{i}]")
    res2.append(xxx.text)
assert res2 == act2

# verify right empty
muel = driver.find_elements(By.XPATH,"//div[@class='dual-list list-right col-md-5']/div/ul/li")
lmu = len(muel)
assert lmu == 0

# close
driver.close()
