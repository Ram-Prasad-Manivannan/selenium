from selenium import webdriver
from selenium.webdriver.common.by import By

print('Enter the gmailid and password')
gmailId, passWord = map(str, input().split())
try:
	driver = webdriver.Chrome()
	driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
	'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
	'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
	driver.implicitly_wait(15)

	loginBox = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
	loginBox.send_keys(gmailId)

	nextButton = driver.find_element(By.XPATH, '//*[@id ="identifierNext"]')
	nextButton[0].click()

	passWordBox = driver.find_element(By.XPATH,
		'//*[@id ="password"]/div[1]/div / div[1]/input')
	passWordBox.send_keys(passWord)

	nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
	nextButton[0].click()

	print('Login Successful...!!')
except:
	print('Login Failed')
