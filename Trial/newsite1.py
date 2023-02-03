import time

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
driver.find_element(By.NAME,"name").send_keys("Akashvani")
driver.find_element(By.XPATH,"//input[@class='validate[required,custom[email]]']").send_keys("abcd@gmail.com")
driver.find_element(By.NAME,"telephone").send_keys("1234567890")
driver.find_element(By.NAME,"country").send_keys("Mt Kailash")
driver.find_element(By.NAME,"company").send_keys("Shiva groups pvt Lmt")
driver.find_element(By.NAME,"message").send_keys("Om Nama Shiva ya")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Submit").click()
time.sleep(5)
x = driver.find_element(By.XPATH,"//section[@id='presscore-contact-form-widget-3']/form/div[1]/div").text
assert x == "Feedback has been sent to the administrator"
