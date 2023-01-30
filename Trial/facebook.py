# import statements
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# To block notifications
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")

option.add_argument("start-maximized")

option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

# Loading driver and opening url
driver = webdriver.Chrome(chrome_options=option)
driver.get("https://www.facebook.com")

# Login elements and sending input
driver.find_element(By.ID, "email").send_keys("seleniumisawesome123@gmail.com")
driver.find_element(By.ID, "pass").send_keys("Selenium_is_awesome")

# clicking on login button
driver.find_element(By.NAME, "login").click()

time.sleep(8)

# Closing the webpage
driver.close()
