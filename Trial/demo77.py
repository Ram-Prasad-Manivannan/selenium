import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

url = "https://demo.seleniumeasy.com/jquery-dropdown-search-demo.html"

driver.get(url)

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@aria-labelledby='select2-country-container']"))).click()
time.sleep(3)
