link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_presence(browser):
    browser.get(link)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) > 0, "NO ADD_TO_BASKET BUTTON"