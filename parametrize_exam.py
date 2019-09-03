import pytest
from selenium import webdriver
import time
import math


def get_answer():
    return math.log(int(time.time()))

"""
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    print("\nquit browser..")
    browser.quit()
"""

num_tests = [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]


@pytest.mark.parametrize('num_test', num_tests)
def test_guest_should_see_login_link(browser, num_test):
    link = f"https://stepik.org/lesson/{num_test}/step/1"
    browser.get(link)
    # .smart-hints__hint - это где correct
    # .textarea - это куда вставлять
    # .submit-submission - это на что нажимать
    browser.find_element_by_css_selector(".textarea").send_keys(str(get_answer()))
    browser.find_element_by_css_selector(".submit-submission").click()
    is_correct = browser.find_element_by_css_selector(".smart-hints__hint").text
    if is_correct != "Correct!":
        print(is_correct)

# pytest -s -v filename.py
