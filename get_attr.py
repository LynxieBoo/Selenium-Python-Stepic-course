from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
try:
    browser.get(link)

    x = browser.find_element_by_id('treasure').get_attribute('valuex')
    browser.find_element_by_id('answer').send_keys(calc(x))

    elems = ['#robotCheckbox', '#robotsRule', 'button.btn']

    for elem in elems:
        browser.find_element_by_css_selector(elem).click()

    print_answer(browser)
finally:
    browser.quit()
