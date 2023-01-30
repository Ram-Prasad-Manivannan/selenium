# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# main program
print("...drag and drop started...")

# Driver initiation
driver = webdriver.Edge()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://demo.seleniumeasy.com/drag-and-drop-demo.html")
time.sleep(2)

# Verify title
assert driver.title == "Selenium Easy Demo - Drag and Drop Demo"

# verify header
head = driver.find_element(By.XPATH,"//h2").text
assert head == "Drag and Drop Demo for Automation"

# drag elements
dno = driver.find_elements(By.XPATH,"//div[@id='todrag']/span")
no = len(dno)+1
assert no == 5

for i in range(1,no):
    d_ele = driver.find_element(By.XPATH,f"//div[@id='todrag']/span[{i}]").get_attribute("draggable")
    assert d_ele == "true"

# source = driver.find_element(By.XPATH,f"//div[@id='todrag']/span[1]")
source = driver.find_element(By.XPATH, "//div[@id='todrag']//span[text()='Draggable 1']")
target = driver.find_element(By.XPATH,"//div[@class='w50 moveleft']/div")
# action = ActionChains(driver)
# action.drag_and_drop(source,target).perform()
# time.sleep(2)

# drag all:
# for i in range(1,no):
#     source = driver.find_element(By.XPATH,f"//div[@id='todrag']/span[{i}]")
#     target = driver.find_element(By.XPATH,"//div[@id='mydropzone']")
#     action = ActionChains(driver)
#     action.drag_and_drop(source, target).perform()
#     time.sleep(2)
#
# time.sleep(5)

# verify
# source = driver.find_element(By.XPATH,"//div[@id='todrag']/span[text()='Draggable 1']")
# ActionChains(driver).drag_and_drop_by_offset(source,640,445).perform()
ActionChains(driver).click_and_hold(source).move_to_element_with_offset(target,250,10).release(source).perform()
time.sleep(5)

