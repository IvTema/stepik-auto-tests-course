from selenium import webdriver
import time

try:
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	num1 = browser.find_element_by_css_selector("#num1").text
	print(num1)
	num2 = browser.find_element_by_css_selector("#num2").text
	print(num2)
	num3 = str(int(num1)+int(num2))
	print(num3)

	from selenium.webdriver.support.ui import Select

	select = Select(browser.find_element_by_css_selector("#dropdown"))
	select.select_by_value(num3)

	browser.find_element_by_css_selector('.btn').click()

finally:
	time.sleep(10)
	browser.quit()