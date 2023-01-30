# from python
import time
# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("...Modal started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")

# Finding Alerts & Modals
# driver.find_element(By.XPATH, "//a[text()='Alerts & Modals']").click()
driver.find_element(By.XPATH, "(//li[@class='dropdown'])[5]/a").click()
time.sleep(2)

# Progress Bar Modal
driver.find_element(By.XPATH,"//a[text()='Progress Bar Modal']").click()
time.sleep(2)

# click show dialog
driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
time.sleep(1)
x = driver.find_element(By.XPATH,"//div[@class='modal fade in']").is_displayed()
te = driver.find_element(By.XPATH,"//div[@class='modal fade in']").get_attribute("textContent")
assert te == "Loading"

x1 = WebDriverWait(driver,5).until(EC.invisibility_of_element
                                   (driver.find_element(By.XPATH,"//div[@class='modal fade in']")))

# click show 2 dialog
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
time.sleep(1)
x21 = driver.find_element(By.XPATH,"//div[@class='modal fade in']").is_displayed()
te = driver.find_element(By.XPATH,"//div[@class='modal fade in']").get_attribute("textContent")
assert te == "Custom message"

x2 = WebDriverWait(driver,5).until(EC.invisibility_of_element
                                   (driver.find_element(By.XPATH,"//div[@class='modal fade in']")))

# click show 3 dialog
driver.find_element(By.XPATH,"//button[@class='btn btn-warning']").click()
time.sleep(1)
x31 = driver.find_element(By.XPATH,"//div[@class='modal fade in']").is_displayed()
te = driver.find_element(By.XPATH,"//div[@class='modal fade in']").get_attribute("textContent")
assert te == "Hello Mr. Alert !"

x3 = WebDriverWait(driver, 5).until(EC.invisibility_of_element
                                    (driver.find_element(By.XPATH,"//div[@class='modal fade in']")))


# close
driver.close()
