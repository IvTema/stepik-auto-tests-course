from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

browser.find_element_by_css_selector('.btn.btn-primary').click()
browser.switch_to.alert.accept()

x = browser.find_element_by_css_selector('#input_value').text
browser.find_element_by_css_selector('.form-control').send_keys(str(calc(x)))
browser.find_element_by_css_selector('.btn.btn-primary').click()