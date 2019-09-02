from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 150);")
    x = calc(browser.find_element_by_id('input_value').text)
    answer_field = browser.find_element_by_id('answer').send_keys(x)

    elems = ['#robotCheckbox', '#robotsRule', 'button.btn']
    for elem in elems:
        browser.find_element_by_css_selector(elem).click()

    print_answer(browser)
finally:
    browser.quit()
