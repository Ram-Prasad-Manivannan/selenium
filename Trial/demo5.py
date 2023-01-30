# Necessary import statements
from selenium import webdriver
import time

# id import
from selenium.webdriver.common.by import By

# Importing Select class
from selenium.webdriver.support.ui import Select

# keyboard actions
from selenium.webdriver.common.keys import Keys

print("...demo 5 started...")

# Driver initiation
driver = webdriver.Chrome()

# Website loading
driver.get("https://demo.seleniumeasy.com/")
time.sleep(2)

# Maximize
driver.maximize_window()

# Finding Input Forms
driver.find_element(By.XPATH, '(//a[@class="dropdown-toggle"])[1]').click()
time.sleep(2)

# selecting Input Form Submit option
driver.find_element(By.XPATH, '(//a[text()="Input Form Submit"])[1]').click()
time.sleep(2)

# PSTV_TC

# Input first name
driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("Raja")
time.sleep(1)

# validating
empty1 = driver.find_element(By.XPATH, "//small[@data-bv-validator='notEmpty']").get_attribute("data-bv-result")
assert empty1 == "VALID"

len1 = driver.find_element(By.XPATH, "//small[@data-bv-validator='stringLength']").get_attribute("data-bv-result")
assert len1 == "VALID"


# Input last name
driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("Singham")
time.sleep(1)

# validating
len2 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[2]").get_attribute("data-bv-result")
assert len2 == "VALID"

empty2 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[2]").get_attribute("data-bv-result")
assert empty2 == "VALID"

# Input email id
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("seleniumisawesome123@gmail.com")
time.sleep(1)

# validating
ema = driver.find_element(By.XPATH, "//small[@data-bv-validator='emailAddress']").get_attribute("data-bv-result")
assert ema == "VALID"

empty3 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[3]").get_attribute("data-bv-result")
assert empty3 == "VALID"

# Input phone number
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("(987)111-1123")
time.sleep(1)

# validating
phn = driver.find_element(By.XPATH, "//small[@data-bv-validator='phone']").get_attribute("data-bv-result")
assert phn == "VALID"

empty4 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[4]").get_attribute("data-bv-result")
assert empty4 == "VALID"

# Input address
driver.find_element(By.XPATH, "//input[@name='address']").send_keys("TV Kovil,Trichy")
time.sleep(1)

# validating
len5 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[3]").get_attribute("data-bv-result")
assert len5 == "VALID"

empty5 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[5]").get_attribute("data-bv-result")
assert empty5 == "VALID"

# Input city
driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Trichy")
time.sleep(1)

# validating
len6 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[4]").get_attribute("data-bv-result")
assert len6 == "VALID"

empty6 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[6]").get_attribute("data-bv-result")
assert empty6 == "VALID"

# Input State
ele = driver.find_element(By.XPATH, "//select[@name='state']")
drop = Select(ele)

drop.select_by_visible_text("Indiana")
time.sleep(1)

# validating
empty7 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[7]").get_attribute("data-bv-result")
assert empty7 == "VALID"

# Input zip code
driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("1234")
time.sleep(1)

# validating
empty8 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[8]").get_attribute("data-bv-result")
assert empty8 == "VALID"

zipc = driver.find_element(By.XPATH, "//small[@data-bv-validator='zipCode']").get_attribute("data-bv-result")
assert zipc == "VALID"

# Input web domain
driver.find_element(By.XPATH, "//input[@name='website']").send_keys("www.awesomeisme.com")
time.sleep(1)

# Input hosting status yes/no now as yes
driver.find_element(By.XPATH, "(//input[@name='hosting'])[1]").click()
time.sleep(1)

# Input description
driver.find_element(By.XPATH, "//textarea").send_keys(":) Alive is awesome is the description here... ha ha")
time.sleep(2)

# validating
len9 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[5]").get_attribute("data-bv-result")
assert len9 == "VALID"

empty9 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[9]").get_attribute("data-bv-result")
assert empty9 == "VALID"


# Send button
driver.find_element(By.XPATH, "//button[@class='btn btn-default']").click()
time.sleep(2)

# NGTV TC
driver.refresh()

# Input first name
driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys(Keys.SPACE)

empty1 = driver.find_element(By.XPATH, "//small[@data-bv-validator='notEmpty']").get_attribute("data-bv-result")
assert empty1 == "INVALID"

len1 = driver.find_element(By.XPATH, "//small[@data-bv-validator='stringLength']").get_attribute("data-bv-result")
assert len1 == "INVALID"

driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys(Keys.SPACE)
time.sleep(1)

empty1 = driver.find_element(By.XPATH, "//small[@data-bv-validator='notEmpty']").get_attribute("data-bv-result")
assert empty1 == "INVALID"

driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("R")
len1 = driver.find_element(By.XPATH, "//small[@data-bv-validator='stringLength']").get_attribute("data-bv-result")
assert len1 == "VALID"

driver.find_element(By.XPATH, "//input[@name='first_name']").clear()

driver.find_element(By.XPATH, "//input[@name='first_name']").send_keys("R")
len1 = driver.find_element(By.XPATH, "//small[@data-bv-validator='stringLength']").get_attribute("data-bv-result")
assert len1 == "INVALID"
empty1 = driver.find_element(By.XPATH, "//small[@data-bv-validator='notEmpty']").get_attribute("data-bv-result")
assert empty1 == "VALID"


# Input last name
driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("raaaaaaaaaaaaaaz")
driver.find_element(By.XPATH, "//input[@name='last_name']").clear()
time.sleep(1)

len2 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[2]").get_attribute("data-bv-result")
assert len2 == "INVALID"

empty2 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[2]").get_attribute("data-bv-result")
assert empty2 == "INVALID"

driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys("S")
time.sleep(1)

len2 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[2]").get_attribute("data-bv-result")
assert len2 == "INVALID"

empty2 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[2]").get_attribute("data-bv-result")
assert empty2 == "VALID"

# Input email
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("seleniumisawesome123@gmail.com")
driver.find_element(By.XPATH, "//input[@name='email']").clear()
time.sleep(1)

ema = driver.find_element(By.XPATH, "//small[@data-bv-validator='emailAddress']").get_attribute("data-bv-result")
assert ema == "INVALID"

empty3 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[3]").get_attribute("data-bv-result")
assert empty3 == "INVALID"

# only text any length
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("seleniumisawesome123")
time.sleep(1)

ema = driver.find_element(By.XPATH, "//small[@data-bv-validator='emailAddress']").get_attribute("data-bv-result")
assert ema == "INVALID"

empty3 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[3]").get_attribute("data-bv-result")
assert empty3 == "VALID"

# adding @
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("seleniumisawesome123@")
time.sleep(1)

ema = driver.find_element(By.XPATH, "//small[@data-bv-validator='emailAddress']").get_attribute("data-bv-result")
assert ema == "INVALID"

empty3 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[3]").get_attribute("data-bv-result")
assert empty3 == "VALID"

# 2 letter followed by @
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("seleniumisawesome123@ww")
time.sleep(1)

ema = driver.find_element(By.XPATH, "//small[@data-bv-validator='emailAddress']").get_attribute("data-bv-result")
assert ema == "INVALID"

empty3 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[3]").get_attribute("data-bv-result")
assert empty3 == "VALID"

# ending with .
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("seleniumisawesome123@WER.")
time.sleep(1)

ema = driver.find_element(By.XPATH, "//small[@data-bv-validator='emailAddress']").get_attribute("data-bv-result")
assert ema == "INVALID"

empty3 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[3]").get_attribute("data-bv-result")
assert empty3 == "VALID"

# Input phone
# empty
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("(987)111-1123")
driver.find_element(By.XPATH, "//input[@name='phone']").clear()
time.sleep(1)

phn = driver.find_element(By.XPATH, "//small[@data-bv-validator='phone']").get_attribute("data-bv-result")
assert phn == "INVALID"

empty4 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[4]").get_attribute("data-bv-result")
assert empty4 == "INVALID"

# more than 10
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("98765432101")
time.sleep(1)

phn = driver.find_element(By.XPATH, "//small[@data-bv-validator='phone']").get_attribute("data-bv-result")
assert phn == "INVALID"

empty4 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[4]").get_attribute("data-bv-result")
assert empty4 == "VALID"

# less than 10
driver.find_element(By.XPATH, "//input[@name='phone']").clear()
driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("987654321")
time.sleep(1)

phn = driver.find_element(By.XPATH, "//small[@data-bv-validator='phone']").get_attribute("data-bv-result")
assert phn == "INVALID"

empty4 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[4]").get_attribute("data-bv-result")
assert empty4 == "VALID"

# Input address
# empty
driver.find_element(By.XPATH, "//input[@name='address']").send_keys("TV Kovil,Trichy")
driver.find_element(By.XPATH, "//input[@name='address']").clear()
time.sleep(1)

len5 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[3]").get_attribute("data-bv-result")
assert len5 == "INVALID"

empty5 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[5]").get_attribute("data-bv-result")
assert empty5 == "INVALID"

# less than 8
driver.find_element(By.XPATH, "//input[@name='address']").send_keys("1234567")
time.sleep(1)

len5 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[3]").get_attribute("data-bv-result")
assert len5 == "INVALID"

empty5 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[5]").get_attribute("data-bv-result")
assert empty5 == "VALID"

# Input city
# empty
driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Trichy")
driver.find_element(By.XPATH, "//input[@name='city']").clear()
time.sleep(1)

len6 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[4]").get_attribute("data-bv-result")
assert len6 == "INVALID"

empty6 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[6]").get_attribute("data-bv-result")
assert empty6 == "INVALID"

# less than 4
driver.find_element(By.XPATH, "//input[@name='city']").send_keys("123")
time.sleep(1)

len6 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[4]").get_attribute("data-bv-result")
assert len6 == "INVALID"

empty6 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[6]").get_attribute("data-bv-result")
assert empty6 == "VALID"

# Input State
ele = driver.find_element(By.XPATH, "//select[@name='state']")
drop = Select(ele)

drop.select_by_visible_text("Indiana")
time.sleep(1)

drop.select_by_visible_text("Please select your state")
time.sleep(2)

empty7 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[7]").get_attribute("data-bv-result")
assert empty7 == "INVALID"

# Input zip code
# empty
driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("1234")
driver.find_element(By.XPATH, "//input[@name='zip']").clear()
time.sleep(1)

empty8 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[8]").get_attribute("data-bv-result")
assert empty8 == "INVALID"

zipc = driver.find_element(By.XPATH, "//small[@data-bv-validator='zipCode']").get_attribute("data-bv-result")
assert zipc == "INVALID"

# less than 4
driver.find_element(By.XPATH, "//input[@name='zip']").send_keys("123")
time.sleep(1)

empty8 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[8]").get_attribute("data-bv-result")
assert empty8 == "VALID"

zipc = driver.find_element(By.XPATH, "//small[@data-bv-validator='zipCode']").get_attribute("data-bv-result")
assert zipc == "INVALID"

# Input web domain
# empty ---- no negative tc here

# Input hosting
# No negative tc here ---radio button

# Input description
# empty
driver.find_element(By.XPATH, "//textarea").send_keys(":) Alive is awesome is the description here... ha ha")
driver.find_element(By.XPATH, "//textarea").clear()
time.sleep(2)

len9 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[5]").get_attribute("data-bv-result")
assert len9 == "INVALID"

empty9 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[9]").get_attribute("data-bv-result")
assert empty9 == "INVALID"

# less than 10
driver.find_element(By.XPATH, "//textarea").send_keys("123456789")
driver.find_element(By.XPATH, "//textarea").clear()
time.sleep(2)

len9 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='stringLength'])[5]").get_attribute("data-bv-result")
assert len9 == "INVALID"

empty9 = driver.find_element(By.XPATH, "(//small[@data-bv-validator='notEmpty'])[9]").get_attribute("data-bv-result")
assert empty9 == "VALID"

print("demo 5 executed successfully...")

# close
driver.close()
