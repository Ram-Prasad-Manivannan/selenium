from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("start-maximized")

webdriver_service = Service('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

url = "https://demo.seleniumeasy.com/jquery-dropdown-search-demo.html"

driver.get(url)

select_country = Select(wait.until(EC.element_to_be_clickable((By.ID, 'country'))))
select_country.select_by_value("Denmark")