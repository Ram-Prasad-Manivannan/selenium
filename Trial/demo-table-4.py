# Necessary import statements
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

print("...demo table 4 started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(2)

# Maximize
driver.maximize_window()

# Finding Table
# driver.find_element(By.XPATH, "//a[text()='Table']").click()
driver.find_element(By.XPATH, "(//li[@class='dropdown'])[3]/a").click()
time.sleep(2)

# Finding Table Sort & Search
driver.find_element(By.XPATH, "//a[text()='Table Sort & Search']").click()
time.sleep(2)

# verify the page title
assert "Selenium Easy - Tabel Sort and Search Demo" in driver.title

# verify the table is present
table = driver.find_element(By.ID,"example")
assert table is not None

# pagination verification
# Total records
tot = driver.find_element(By.XPATH, "//div[@id='example_info']").text

a = tot.split('of')[1]                 # cutting 'showing 1 to n of' string and store the remaining to a variable
a = a.split(" entries")[0].strip()   # cutting 'entries' from '32 entries'

total_records = int(a)                 # converting string to int
print(total_records)

# Total pages
pg_sz = [10,25,50,100]
for i in pg_sz:
    print("number of records per page:",i)
    ele = driver.find_element(By.XPATH, "//select[@name='example_length']")
    ch = Select(ele)
    ch.select_by_value(f"{i}")
    time.sleep(2)
    if total_records <= i:
        print("All records are in same page")
        ele = driver.find_elements(By.XPATH, "//tbody/tr")
        length = len(ele)
        print("Total number of records in the page are :", length)
        assert total_records == length
    elif total_records > i:
        v = int(total_records/i)
        f = v+1
        final = 0
        for j in range(f):
            j = j+1
            driver.find_element(By.XPATH, f"//a[contains(@class,'paginate_button') and @data-dt-idx='{j}']").click()
            time.sleep(5)

            ele1 = driver.find_elements(By.XPATH, "//tbody/tr")
            v1 = len(ele1)
            final = final + v1

            print("Total number of records in the page:",j," is ", v1)
            print("Total records in all pages currently---",final)

        assert final == total_records
        print("Records are matched")
print("...Pagination is checked properly...")
