from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    # имя
    input_name = browser.find_element_by_css_selector(".first[required]")
    input_name.send_keys('My name')
    # фамилия
    input_lastname = browser.find_element_by_css_selector(".second[required]")
    input_lastname.send_keys('My last name')
    # почта
    input_email = browser.find_element_by_css_selector(".third[required]")
    input_email.send_keys('test@test.io')

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
