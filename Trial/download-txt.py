# from python
import time
import random
import string
import glob
import os

# from selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# random char generator
charLen = 50
txtgen = ''.join(random.choice(string.printable) for i in range(charLen))

# main program
print("...exe1 started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")

# Finding Alerts & Modals
# driver.find_element(By.XPATH, "//a[text()='Alerts & Modals']").click()
driver.find_element(By.XPATH, "(//li[@class='dropdown'])[5]/a").click()
time.sleep(2)

# File download
driver.find_element(By.XPATH,"//a[text()='File Download']").click()
time.sleep(2)

# button check
t = driver.find_element(By.XPATH,"//button[@id='create']").get_attribute("disabled")
assert t == "true"

# text area
driver.find_element(By.XPATH,"//textarea[@id='textbox']").send_keys(txtgen)
time.sleep(15)

# click
driver.find_element(By.XPATH,"//button[@id='create']").click()
time.sleep(4)
x = driver.find_element(By.XPATH,"//a[text()='Download']")
#WebDriverWait(driver,10).until(EC.element_to_be_clickable(x))
x.click()
time.sleep(4)

# file read
#list_of_files = glob.glob(r'C:\Users\rampr\Downloads\easyinfo.txt')  # recent file
#latest_file = max(list_of_files, key=os.path.getctime)
# open the file
file = open(r"C:\Users\rampr\Downloads\easyinfo.txt", "r+")
# read the file
content = file.read()
# close the file
file.close()
# store the content in a string
string = str(content)

print("input is :",txtgen)
print("output is :",string)
#assert string == txtgen
