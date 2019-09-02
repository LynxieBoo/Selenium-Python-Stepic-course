from selenium import webdriver
import time
import os


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements_by_css_selector('.form-control')
    for element in elements:
        element.send_keys("answer")
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file_input.txt')
    send_file = browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(5)
    print_answer(browser)
finally:
    browser.quit()
