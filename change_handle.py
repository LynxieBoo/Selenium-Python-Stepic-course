from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


browser = webdriver.Chrome()
browser.implicitly_wait(3)
try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    btn = browser.find_element_by_css_selector('.trollface').click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    redirect = browser.switch_to.window(new_window)
    x = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_css_selector("button.btn").click()
    print_answer(browser)
finally:
    browser.quit()
