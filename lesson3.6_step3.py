import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def answer():
    return math.log(int(time.time()))

samples = [
    ("a", "236895"),
    ("b", "236896"),
    ("c", "236897"),
    ("d", "236898"),
    ("e", "236899"),
    ("f", "236903"),
    ("g", "236904"),
    ("h", "236905")
]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num, code', samples)
def test_correct_sign(browser, num, code):
        link = "https://stepik.org/lesson/{}/step/1".format(code)
        print("Номер ссылки %s" % num)
        browser.get(link)
        text_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
        #сначала хотел явное ожидание, сейчас это функционально бессмысленно, но переписывать не стал
        text_field.send_keys(str(math.log(int(time.time()))))
        browser.find_element_by_css_selector(".submit-submission").click()
        assert browser.find_element_by_css_selector('.smart-hints__hint').text == "Correct!", "Не надпись Correct!"