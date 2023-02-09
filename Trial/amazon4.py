from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")

search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("Samsung mobile")
search_box.send_keys(Keys.RETURN)

results = driver.find_elements(By.XPATH,"//div[@data-index]")
count = 0
for result in results:
    if "4GB RAM" in result.text:
        count += 1

print(f"Number of search results with text '4GB RAM': {count}")

