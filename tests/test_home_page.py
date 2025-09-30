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
        self.driver.get(Urls.BASE_URL)
        home_page = HomePage(self.driver)
        home_page.scroll_to_question(faq['index'])
        home_page.wait_question()
        question_text = home_page.get_faq_question_text(faq['index'])
        assert question_text == faq['question']
        home_page.click_faq_question(faq['index'])
        home_page.wait_answer()
        answer_text = home_page.get_faq_answer_text(faq['index'])
        assert answer_text == faq['answer']

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
