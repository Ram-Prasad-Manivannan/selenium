# Necessary import statements
# from python
import time

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

print("...drag started...")

# Driver initiation
driver = webdriver.Chrome()

# wait for 10 seconds
wait = WebDriverWait(driver, 10)

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(2)

# Maximize
driver.maximize_window()

# Finding Alerts & Modals
# driver.find_element(By.XPATH, "//a[text()='Alerts & Modals']").click()
driver.find_element(By.XPATH, "(//li[@class='dropdown'])[5]/a").click()
time.sleep(2)

# bootstrap alerts
driver.find_element(By.XPATH,"//a[text()='Bootstrap Alerts']").click()
time.sleep(2)

# title
assert "Selenium Easy - Bootstrap Alerts Demo for Automation" in driver.title

# click 1 auto close message
driver.find_element(By.XPATH,"//button[@id='autoclosable-btn-success']").click()
q = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-autocloseable-success']").is_displayed()
assert q is True
t = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-autocloseable-success']").text
assert "I'm an autocloseable success message. I will hide in 5 seconds." in t
time.sleep(6)
t0 = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-autocloseable-success']").is_displayed()
assert t0 is False

# click 2 normal message
driver.find_element(By.XPATH,"//button[@id='normal-btn-success']").click()
time.sleep(2)
x = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-normal-success']").is_displayed()
assert x is True
t1 = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-normal-success']").text
assert "I'm a normal success message. To close use the appropriate button." in t1
# (//button[@class='close'])[1]
t2 = driver.find_element(By.XPATH,"(//button[@class='close'])[1]").is_displayed()
assert t2 is True
driver.find_element(By.XPATH,"//button[@class='close']").click()
time.sleep(4)

t3 = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-normal-success']").is_displayed()
assert t3 is False

# click 3 warning disappear
driver.find_element(By.XPATH,"//button[@id='autoclosable-btn-warning']").click()
x1 = driver.find_element(By.XPATH,"//div[@class='alert alert-warning alert-autocloseable-warning']").is_displayed()
time.sleep(4)
x2 = driver.find_element(By.XPATH,"//div[@class='alert alert-warning alert-autocloseable-warning']").is_displayed()
assert x1 is True
assert x2 is False

# click 4 warning
driver.find_element(By.XPATH,"//button[@id='normal-btn-warning']").click()
x3 = driver.find_element(By.XPATH,"//div[@class='alert alert-warning alert-normal-warning']").is_displayed()
time.sleep(3)
t3 = driver.find_element(By.XPATH,"(//button[@class='close'])[2]").is_displayed()
assert t3 is True
driver.find_element(By.XPATH,"(//button[@class='close'])[2]").click()
time.sleep(2)
x4 = driver.find_element(By.XPATH,"//div[@class='alert alert-warning alert-normal-warning']").is_displayed()
assert x3 is True
assert x4 is False

# click 5 danger disappear
driver.find_element(By.XPATH,"//button[@id='autoclosable-btn-danger']").click()
x5 = driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-autocloseable-danger']").is_displayed()
time.sleep(6)
x6 = driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-autocloseable-danger']").is_displayed()
assert x5 is True
assert x6 is False

# click 6 danger
driver.find_element(By.XPATH,"//button[@id='normal-btn-danger']").click()
x3 = driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-normal-danger']").is_displayed()
time.sleep(3)
t3 = driver.find_element(By.XPATH,"(//button[@class='close'])[3]").is_displayed()
assert t3 is True
driver.find_element(By.XPATH,"(//button[@class='close'])[3]").click()
time.sleep(2)
x4 = driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-normal-danger']").is_displayed()
assert x3 is True
assert x4 is False

# click 7 info disappear
driver.find_element(By.XPATH,"//button[@id='autoclosable-btn-info']").click()
x5 = driver.find_element(By.XPATH,"//div[@class='alert alert-info alert-autocloseable-info']").is_displayed()
time.sleep(7)
x6 = driver.find_element(By.XPATH,"//div[@class='alert alert-info alert-autocloseable-info']").is_displayed()
assert x5 is True
assert x6 is False

# click 8 info
driver.find_element(By.XPATH,"//button[@id='normal-btn-info']").click()
x3 = driver.find_element(By.XPATH,"//div[@class='alert alert-info alert-normal-info']").is_displayed()
time.sleep(3)
t3 = driver.find_element(By.XPATH,"(//button[@class='close'])[4]").is_displayed()
assert t3 is True
driver.find_element(By.XPATH,"(//button[@class='close'])[4]").click()
time.sleep(2)
x4 = driver.find_element(By.XPATH,"//div[@class='alert alert-info alert-normal-info']").is_displayed()
assert x3 is True
assert x4 is False
