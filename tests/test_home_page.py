import allure
import pytest
from selenium import webdriver
from urls import Urls
from pages.home_page import HomePage
from data_for_tests import DataForTests as Data


class TestHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка на соответствие ответа вопросу в блоке "Вопросы о важном"')
    @pytest.mark.parametrize('faq', Data.faq)
    def test_faq_question_corresponds_answer(self, faq):
        home_page = HomePage(self.driver)
        home_page.open_page(Urls.BASE_URL)
        assert home_page.check_question_text(faq['index'], faq['question'])
        assert home_page.check_answer_text(faq['index'], faq['answer'])

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
