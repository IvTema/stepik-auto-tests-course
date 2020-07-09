import pytest
from selenium import webdriver

samples = [
    ("236895","a" ),
    ("b" "236896"),
    ("c", "236897"),
    ("d", "236898"),
    ("e", "236899"),
    ("f" "236903"),
    ("g", "236904"),
    ("h", "236905")
]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num, code', samples)
def test_correct_sign(browser, num, code):
        link = "https://stepik.org/lesson/{}/step/1".format(code)
        print("Номер ссылки %s" % num)
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")