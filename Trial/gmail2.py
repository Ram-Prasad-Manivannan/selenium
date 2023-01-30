from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/SignUp?service=mail&continue=https://mail.google.com/mail/?pc=topnav-about-en")

with open('accounts.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        first_name = row[0]
        last_name = row[1]
        username = row[2]
        password = row[3]
        confirm_password = row[4]

        driver.find_element(By.ID, "FirstName").send_keys(first_name)
        driver.find_element(By.ID, "LastName").send_keys(last_name)
        driver.find_element(By.ID, "GmailAddress").send_keys(username)
        driver.find_element(By.ID, "Passwd").send_keys(password)
        driver.find_element(By.ID, "PasswdAgain").send_keys(confirm_password)

        driver.find_element(By.ID, "signIn").click()

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "errormsg_0_GmailAddress")))
        except TimeoutException:
            print("Time out exception")
        driver.find_element(By.ID, "FirstName").clear()
        driver.find_element(By.ID, "LastName").clear()
        driver.find_element(By.ID, "GmailAddress").clear()
        driver.find_element(By.ID, "Passwd").clear()
        driver.find_element(By.ID, "PasswdAgain").clear()
