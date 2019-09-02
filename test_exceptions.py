from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
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
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id('book').click()
    x = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(x)
    browser.find_element_by_css_selector("[type='submit']").click()

    print_answer(browser)
finally:
    browser.quit()
