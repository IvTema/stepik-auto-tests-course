from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	img = browser.find_element_by_css_selector("#treasure")
	print(img)

	x = img.get_attribute('valuex')
	print(x)

	answer = browser.find_element_by_css_selector('#answer')
	answer.send_keys(calc(x))

	robotCheckbox = browser.find_element_by_css_selector("#robotCheckbox")
	robotCheckbox.click()

	robotsRule = browser.find_element_by_css_selector("#robotsRule")
	robotsRule.click()

	btn = browser.find_element_by_css_selector(".btn")
	btn.click()

finally:
	time.sleep(10)
	browser.quit()

