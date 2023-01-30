from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

print("sample test case started")
driver = webdriver.Chrome()
# driver=webdriver.firefox()
# driver=webdriver.ie()
# maximize the window size
driver.maximize_window()
# navigate to the url
driver.get("https://www.google.com/")
# identify the Google search text box and enter the value
driver.find_element(By.NAME, "q").send_keys("Mistral Solutions ")
time.sleep(3)
# click on the Google search button
driver.find_element(By.NAME, "btnK").send_keys(Keys.ENTER)
time.sleep(3)
# close the browser
driver.close()
print("sample test case successfully completed")