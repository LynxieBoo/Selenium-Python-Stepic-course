from selenium import webdriver
import unittest


class TestRegistration(unittest.TestCase):
    def reg_form(self, link):
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)
        browser.get(link)

        # имя
        browser.find_element_by_css_selector(".first[required]").send_keys('My name')
        # фамилия
        browser.find_element_by_css_selector(".second[required]").send_keys('My last name')
        # почта
        browser.find_element_by_css_selector(".third[required]").send_keys('test@test.io')

        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        welcome_text = browser.find_element_by_tag_name("h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        return welcome_text

    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.reg_form(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Not registered")

    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.reg_form(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Not registered")


if __name__ == "__main__":
    unittest.main()
