# from python
import time
# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://www.amazon.in/")

# finding search bar
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Samsung mobile")
driver.find_element(By.ID,"twotabsearchtextbox").submit()

time.sleep(5)
ele = driver.find_elements(By.PARTIAL_LINK_TEXT,"4GB R")
no = len(ele)
print(no)

