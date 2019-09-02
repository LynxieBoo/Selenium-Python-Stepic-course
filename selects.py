from selenium import webdriver
from selenium.webdriver.support.ui import Select


def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()


link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    two_el = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(two_el))

    elems = ['button.btn']
    for elem in elems:
        browser.find_element_by_css_selector(elem).click()

    print_answer(browser)
finally:
    browser.quit()
