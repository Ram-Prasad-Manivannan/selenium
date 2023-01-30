def count_elements(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count

# Main program
list_of_elements = [1,2,3,4,1,5,1,6,7]
element = 1

print("Element {} is present {} times in the list".format(element,count_elements(list_of_elements, element)))






from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the URL
driver.get("https://demo.seleniumeasy.com/table-sort-search-demo.html")

# Check the page title
print(driver.title)

# Check the number of rows
row_count = len(driver.find_elements_by_xpath("//table[@id='example']/tbody/tr"))
print("Number of rows:", row_count)

# Check the number of columns
col_count = len(driver.find_elements_by_xpath("//table[@id='example']/thead/tr/th"))
print("Number of columns:", col_count)

# Sort the table by Age
driver.find_element_by_xpath("//table[@id='example']/thead/tr/th[3]").click()

# Verify the table is sorted by age in descending order
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@id='example']/tbody/tr[1]/td[3]")))
age_list = driver.find_elements_by_xpath("//table[@id='example']/tbody/tr/td[3]")
age_list = [int(age.text) for age in age_list]
sorted_age_list = sorted(age_list, reverse=True)
assert age_list == sorted_age_list

# Search for a name
search_box = driver.find_element_by_xpath("//input[@type='search']")
search_box.send_keys("Alex")

# Verify the name is present in the table
wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@id='example']/tbody/tr/td[contains(text(),'Alex')]")))
name_list = driver.find_elements_by_xpath("//table[@id='example']/tbody/tr/td[2]")
name_list = [name.text for name in name_list]
assert "Alex" in name_list

# Close the browser
driver.quit()