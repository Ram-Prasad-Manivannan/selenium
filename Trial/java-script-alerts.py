# from python
import time
# from selenium
from selenium import webdriver
from selenium.common import TimeoutException
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

# Java Script Alert
driver.find_element(By.XPATH,"//a[text()='Javascript Alerts']").click()
time.sleep(2)

# click 1
try:
    driver.find_element(By.XPATH,"//button[@class='btn btn-default']").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    print("alert accepted")
except TimeoutException:
    print("no alert")

time.sleep(2)

# click 2
try:
    driver.find_element(By.XPATH,"//button[@onclick='myConfirmFunction()']").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    txt = driver.find_element(By.XPATH,"//p[@id='confirm-demo']").text
    print(txt)
    assert txt == "You pressed OK!"
    print("alert accepted")
except TimeoutException:
    print("no alert")

time.sleep(2)

try:
    driver.find_element(By.XPATH,"//button[@onclick='myConfirmFunction()']").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    alert = driver.switch_to.alert
    print(alert.text)
    alert.dismiss()
    txt = driver.find_element(By.XPATH, "//p[@id='confirm-demo']").text
    print(txt)
    assert txt == "You pressed Cancel!"
    print("alert cancelled")
except TimeoutException:
    print("no alert")

# click 3
try:
    driver.find_element(By.XPATH,"//button[@onclick='myPromptFunction()']").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    alert = driver.switch_to.alert
    print(alert.text)
    time.sleep(2)
    alert.send_keys("...Alive is Awesome...")
    time.sleep(2)
    alert.accept()
    tx = driver.find_element(By.XPATH,"//p[@id='prompt-demo']").text
    print(tx)
    assert tx == "You have entered '...Alive is Awesome...' !"
    print("alert ok ed")
except TimeoutException:
    print("no alert")

time.sleep(2)

try:
    driver.find_element(By.XPATH,"//button[@onclick='myPromptFunction()']").click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
    alert = driver.switch_to.alert
    print(alert.text)
    time.sleep(2)
    alert.send_keys("...Alive is Awesome...")
    time.sleep(2)
    alert.dismiss()
    tx = driver.find_element(By.XPATH, "//p[@id='prompt-demo']").text
    print(tx)
    assert tx == "You have entered '...Alive is Awesome...' !"
    print("alert canceled")
except TimeoutException:
    print("no alert")

# close
driver.close()
