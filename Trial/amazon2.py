# from selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch the URL
driver = webdriver.Chrome()
driver.get('https://www.amazon.in')

# Enter "samsung mobile" in Search Tab and press ENTER key
search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys('samsung mobile')
search_box.submit()

time.sleep(4)

# # Count the number of times '4GB RAM' appears and print it
# results = driver.find_elements(By.XPATH,'//div[@class="a-section a-spacing-medium"]')
# count = 0
# for result in results:
#     if '4GB RAM' in result.text:
#         count += 1
#
# print('4GB RAM appears {} times'.format(count))

driver.quit()