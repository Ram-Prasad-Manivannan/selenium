import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# loading driver
driver = webdriver.Chrome()
driver.maximize_window()

# loading URL
driver.get("https://www.seleniumframework.com/")
time.sleep(2)
assert driver.title == "Selenium Framework | Selenium, Cucumber, Ruby, Java et al."
p = driver.current_window_handle

# Click options
driver.find_element(By.XPATH,"//h3[@id='ui-id-3']/a[text()='Selenium WebDriver Basics']").click()
time.sleep(2)

# Click Basic Command
driver.find_element(By.LINK_TEXT,"Browser Commands").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.close()
driver.switch_to.window(driver.window_handles[0])

# Click Selenium WebDriver Tutorial
driver.find_element(By.LINK_TEXT,"Understanding HTML DOM").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
driver.find_element(By.LINK_TEXT,"behave first").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"What is behave ?").click()
time.sleep(1)
driver.find_element(By.NAME,"email").send_keys("aliveisawesome123@gmail.com")
driver.find_element(By.XPATH,"//input[@value='Subscribe']").click()
time.sleep(2)
driver.switch_to.new_window()
driver.close()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])

Name = driver.find_element(By.NAME,"name")
Email = driver.find_element(By.XPATH,"//input[@class='validate[required,custom[email]]']")
Phone = driver.find_element(By.NAME,"telephone")
Country = driver.find_element(By.NAME,"country")
Company = driver.find_element(By.NAME,"company")
Message = driver.find_element(By.NAME,"message")


def fill_form(na,em,ph,con,com,mes):
    Name.send_keys(na)
    Email.send_keys(em)
    Phone.send_keys(ph)
    Country.send_keys(con)
    Company.send_keys(com)
    Message.send_keys(mes)


fill_form("Akashvani","abcd@gmail.com","1234567890","Mt Kailash","Shiva groups pvt lmt","OM Nama Shiva ya")
time.sleep(3)

driver.find_element(By.LINK_TEXT,"Submit").click()
time.sleep(5)

x = driver.find_element(By.XPATH,"//section[@id='presscore-contact-form-widget-3']/form/div[1]/div")
assert x.text == "Feedback has been sent to the administrator"

