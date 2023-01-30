# from python
import calendar
import time
from datetime import date,timedelta

# from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# main program
print("...date...")

# Driver initiation
driver = webdriver.Chrome()

# Maximize
driver.maximize_window()

# Website loading
driver.get("https://demo.seleniumeasy.com/bootstrap-date-picker-demo.html")
time.sleep(3)

# select calendar button
driver.find_element(By.XPATH,"//div[@id='sandbox-container1']/div/span").click()
time.sleep(6)

#//div[@class='datepicker-days']//table[@class='table-condensed']//tbody//tr[1]//td[7]

row = 6
data = 7

CurrentDate = date.today()
currentMonthCount = calendar.monthrange(date.today().year,date.today().month)[1]
NumberOfDaysNotInMonth = 42 - currentMonthCount
PreviousMonthCount = date.today().replace(day=1) - timedelta(days=1)
PreviousMonthCount = PreviousMonthCount.day
NextMonthCount = 10


for i in range(row):
    r=i+1
    for j in range(data):
        driver
