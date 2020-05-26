from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#input_value").text
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(calc(num1))

    robotCheckbox = browser.find_element_by_css_selector("#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotCheckbox.click()

    robotsRule = browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
	time.sleep(10)
	browser.quit()