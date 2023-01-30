import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Launch the URL
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

#Enter 'samsung mobile' in the Search Tab
search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("samsung mobile")
search_box.submit()
time.sleep(4)
#Count number of times the text '4GB RAM' appears
results = driver.find_elements(By.XPATH,"//h2[@data-attribute='4 GB RAM']")

#Print the count
print(len(results))
