# import statements
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# loading driver without chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# loading URL
driver.get("https://www.google.com")

# switching to frame
f = driver.find_element(By.TAG_NAME,"iframe")
driver.switch_to.frame(f)

# clicking on no thanks button
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(1)

# Switching back to main window
driver.switch_to.default_content()

# Search bar enter text and press Enter button
driver.find_element(By.NAME,"q").send_keys("hi", Keys.ENTER)
time.sleep(3)

# going back
driver.back()

#