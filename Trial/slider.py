# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
# Driver initiation
driver = webdriver.Chrome()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://jqueryui.com/slider/")
time.sleep(3)

# frame
iframe = driver.find_element(By.XPATH,"//div[@id='content']/iframe")
driver.switch_to.frame(iframe)

# slider span
slider = driver.find_element(By.XPATH,"//div[@id='slider']/span")
ActionChains(driver).click_and_hold(slider).move_by_offset(200,0).release(slider).perform()
time.sleep(3)

# verify
percentage = slider.get_attribute("style")
assert percentage == "left: 36%;"
