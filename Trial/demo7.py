# Necessary import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

print("...demo 7 started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(2)

# Maximize
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# Finding Input Forms
driver.find_element(By.XPATH, '(//a[@class="dropdown-toggle"])[1]').click()
time.sleep(2)

# selecting JQuery Select dropdown option
driver.find_element(By.XPATH, '(//a[text()="JQuery Select dropdown"])[1]').click()
time.sleep(2)

# tc1 p1

# for country 1
driver.find_element(By.XPATH,"//span[@aria-labelledby='select2-country-container']").click()
driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input").send_keys("Denmark",Keys.ENTER)
time.sleep(2)

# # for country 2
# ele = driver.find_element(By.XPATH, "//select[@id='country']")
# drop = Select(ele)
# drop.select_by_value("Denmark")
# time.sleep(3)

# #for country 3
# select_country = Select(wait.until(EC.element_to_be_clickable((By.ID, 'country'))))
# select_country.select_by_value("Denmark")
# time.sleep(2)

# for state
list1 = ["Delaware","California"]
for i in list1:
    driver.find_element(By.XPATH,"//input[@class='select2-search__field']").send_keys(i,Keys.ENTER)
    time.sleep(2)

# for US OT
ote = driver.find_element(By.XPATH,"//select[@class='js-example-disabled-results select2-hidden-accessible']")
drop = Select(ote)
drop.select_by_value("VI")
time.sleep(2)

# for file
fle = driver.find_element(By.XPATH,"//select[@id='files']")
drop = Select(fle)
drop.select_by_visible_text("Ruby")
time.sleep(3)

# close
print("closing the index file now")
driver.close()