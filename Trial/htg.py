# from python
import time
from datetime import datetime

# from selenium
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

# main program
print("...drag and drop started...")

# Driver initiation
driver = webdriver.Chrome()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://demo.seleniumeasy.com/bootstrap-date-picker-demo.html")
time.sleep(3)

# select date 1 through text
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/input").send_keys("1/12/2020")
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/input").send_keys(keys.Keys.ENTER)
time.sleep(1)
# verify
assert driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/input").get_attribute("value") == "01/12/2020"

# select date as today
# click on button
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/span").click()
time.sleep(6)
# click on today
driver.find_element(By.XPATH,"//div[@class='datepicker-days']/table/tfoot/tr").click()
time.sleep(2)

# verify 1
da = datetime.today().strftime('%d/%m/%Y')
assert driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/input").get_attribute('value') == da

# clear date
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/span").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='datepicker-days']/table/tfoot/tr[2]").click()
time.sleep(2)

# verify
assert driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/input").get_attribute('value') == ''

# pick 16
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/span").click()
time.sleep(3)
driver.find_element(By.XPATH,"//table[@class='table-condensed']/tbody/tr[3]/td[5]").click()
time.sleep(3)

# verify
assert driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/input").get_attribute('value') == '16/12/2022'

# select another month through widget
# say August 10th 2022
# clear date
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/span").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='datepicker-days']/table/tfoot/tr[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/span").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//table[@class='table-condensed']/thead/tr[2]/th[2])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='datepicker-months']/table/tbody/tr/td/span[8]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='datepicker-days']/table/tbody/tr[3]/td[3]").click()
time.sleep(2)
# verify
assert driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/input").get_attribute('value') == '10/08/2022'

# select another year in widget
# say July 12th 2001
# clear date
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/span").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='datepicker-days']/table/tfoot/tr[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/span").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//table[@class='table-condensed']/thead/tr[2]/th[2])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='datepicker-months']/table/thead/tr[2]/th[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='datepicker-years']/table/thead/tr[2]/th[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='datepicker-years']/table/thead/tr[2]/th[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='datepicker-years']/table/tbody/tr/td/span[3]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='datepicker-months']/table/tbody/tr/td/span[7]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='datepicker-days']/table/tbody/tr[3]/td[4]").click()
time.sleep(2)
# verify
assert driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/input").get_attribute('value') == '12/07/2001'


# date set 2
# text
driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[1]").send_keys("02/12/2022")
time.sleep(4)
driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[2]").clear()
driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[2]").send_keys("10/12/2022")
time.sleep(5)

# # verify
# assert driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[1]"
#                            ).get_attribute('value') == "10/12/2022"
# assert driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[2]"
#                            ).get_attribute('value') == "10/12/2022"

driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[1]").clear()
driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[2]").clear()
time.sleep(5)

#wiget
driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='datepicker-days']/table/tbody/tr[1]/td[7]").click()
driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[2]").clear()
driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='datepicker-days']/table/tbody/tr[3]/td[7]").click()
time.sleep(2)

# # verify
# assert driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[1]"
#                            ).get_attribute('value') == "03/12/2022"
# assert driver.find_element(By.XPATH,"//div[@class='input-daterange input-group']/input[2]"
#                            ).get_attribute('value') == "17/12/2022"

# close
driver.close()
