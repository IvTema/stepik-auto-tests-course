import unittest
from selenium import webdriver
import time

class TestSystem(unittest.TestCase):
    def test_1st(self):
        def link_f(link):
            browser = webdriver.Chrome()
            browser.get(link)
            name = browser.find_element_by_css_selector('.first_block>.first_class>.first')
            name.send_keys('Walter')
            lastname = browser.find_element_by_css_selector('.first_block>.second_class>.second')
            lastname.send_keys('White')
            mail = browser.find_element_by_css_selector('.first_block>.third_class>.third')
            mail.send_keys('SayMyName@drugs.net')

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector("button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!',
                             "button_click_error")
        link_f("http://suninjuly.github.io/registration1.html")
        link_f("http://suninjuly.github.io/registration2.html")

if __name__ == "__main__":
    unittest.main()