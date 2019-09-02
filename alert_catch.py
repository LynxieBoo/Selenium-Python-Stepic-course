from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    btn = browser.find_element_by_css_selector('.btn').click()
    time.sleep(3)
    alert = browser.switch_to.alert.accept()
    time.sleep(3)
    x = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_css_selector("button.btn").click()
    time.sleep(3)
    print_answer(browser)
finally:
    time.sleep(3)
    browser.quit()
