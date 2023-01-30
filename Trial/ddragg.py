# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# main program
print("...drag and drop started...")

# Driver initiation
driver = webdriver.Chrome()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
time.sleep(6)

# title
x = driver.find_element(By.XPATH,"//h1").text
assert x == "Drag And Drop"

# frames
fr = driver.find_element(By.XPATH,"//div[@id='post-2669']/div[2]/div/div/div[1]/p/iframe")
driver.switch_to.frame(fr)

# target element
target = driver.find_element(By.ID,"trash")

# source:
source = driver.find_element(By.XPATH,"//ul[@id='gallery']/li[2]/img")

# drag
# ActionChains(driver).click_and_hold(source).move_to_element(target).release(source).perform()
ActionChains(driver).drag_and_drop(source,target).perform()
time.sleep(8)

# verify
ver = "//div[@id='trash']/ul"
ele = driver.find_element(By.XPATH,ver)
# wait = WebDriverWait(driver,10)
# x1 = wait.until(EC.presence_of_element_located(driver.find_element(By.XPATH,ver)))
# print(x1)
time.sleep(5)

# frame back
driver.switch_to.parent_frame()

# click 2 list
driver.find_element(By.XPATH,"//li[@id='Accepted Elements']").click()
time.sleep(3)
iframe = driver.find_element(By.XPATH,"//div[@id='post-2669']/div[2]/div/div/div[2]/p/iframe")
driver.switch_to.frame(iframe)

# drag 1
source1 = driver.find_element(By.XPATH,"//div[@id='draggable-nonvalid']")
source2 = driver.find_element(By.XPATH,"//div[@id='draggable']")
target = driver.find_element(By.XPATH,"//div[@id='droppable']")

ActionChains(driver).click_and_hold(source1).move_to_element(target).release(source1).perform()
time.sleep(4)

# verify
assert driver.find_element(By.XPATH,"//div[@id='droppable']/p").text == "accept: '#draggable'"

ActionChains(driver).click_and_hold(source2).move_to_element(target).release(source2).perform()
time.sleep(4)

# verify
assert driver.find_element(By.XPATH,"//div[@id='droppable']/p").text == "Dropped!"

# frame back
driver.switch_to.parent_frame()

# click 3 list
driver.find_element(By.XPATH,"//li[@id='Propagation']").click()
time.sleep(2)

# frame
iframe = driver.find_element(By.XPATH,"//div[@id='post-2669']/div[2]/div/div/div[3]/p/iframe")
driver.switch_to.frame(iframe)
time.sleep(2)

# elements
source = driver.find_element(By.XPATH,"//div[@id='draggable']")
target1 = driver.find_element(By.XPATH,"//div[@id='droppable']")
target2 = driver.find_element(By.XPATH,"//div[@id='droppable']/div")
target3 = driver.find_element(By.XPATH,"//div[@id='droppable2']")
target4 = driver.find_element(By.XPATH,"//div[@id='droppable2']/div")

# drag 2
ActionChains(driver).drag_and_drop(source,target2).perform()
time.sleep(3)

# verify
assert driver.find_element(By.XPATH,"//div[@id='droppable']/p").text == "Dropped!"
assert driver.find_element(By.XPATH,"//div[@id='droppable']/div/p").text == "Dropped!"

# drag 1
ActionChains(driver).drag_and_drop(source,target1).perform()
time.sleep(3)

# verify
assert driver.find_element(By.XPATH,"//div[@id='droppable']/p").text == "Dropped!"
assert driver.find_element(By.XPATH,"//div[@id='droppable']/div/p").text == "Dropped!"

# drag 4
ActionChains(driver).drag_and_drop(source,target4).perform()
time.sleep(3)

# verify
assert driver.find_element(By.XPATH,"//div[@id='droppable2']/p").text != "Dropped!"
assert driver.find_element(By.XPATH,"//div[@id='droppable2']/div/p").text == "Dropped!"

# drag 3
ActionChains(driver).drag_and_drop(source,target3).perform()
time.sleep(3)

# verify
assert driver.find_element(By.XPATH,"//div[@id='droppable2/p']").text == "Dropped!"
assert driver.find_element(By.XPATH,"//div[@id='droppable2']/div/p").text == "Dropped!"
