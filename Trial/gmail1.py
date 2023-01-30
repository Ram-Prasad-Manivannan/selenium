from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv

def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver

def create_account(driver, first, last, username, password):
    driver.get("http://www.gmail.com")
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "create-account")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.click()
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys(first)
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "LastName")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys(last)
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "GmailAddress")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys(username)
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "Passwd")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys(password)
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "PasswdAgain")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys(password)
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "BirthDay")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys("1")
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "BirthDay")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys("January")
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "BirthDay")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys("1990")
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "RecoveryEmailAddress")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys("recovery@email.com")
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "Gender")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys("Female")
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "CountryCode")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.send_keys("US")
    try:
        element = driver.wait.until(EC.presence_of_element_located((By.ID, "submitbutton")))
    except TimeoutException:
        print("Timed out waiting for page to load")
    element.click()

if __name__ == "__main__":
    driver = init_driver()
    with open('accounts.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            create_account(driver, row['First'], row['Last'], row['Username'], row['Password'])