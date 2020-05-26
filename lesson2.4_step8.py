from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
browser.find_element_by_css_selector('#book').click()


x = browser.find_element_by_css_selector('#input_value').text
browser.find_element_by_css_selector('#answer').send_keys(str(calc(x)))
browser.find_element_by_css_selector('#solve').click()