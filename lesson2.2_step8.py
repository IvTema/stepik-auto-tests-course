from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = "firstname"
    value2 = "lastname"
    value3 = "email"

    input1 = browser.find_element_by_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name(value3)
    input3.send_keys("test@test.test")


    file_path = os.path.join('C:\Games\empty.txt')
    print(file_path)
    browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

    print("Тест успешно завершен. 10 сек на закрытие браузера...")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#не забываем пустую строку