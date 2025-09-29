import time

import pytest
from selenium import webdriver

from pages.order_page import OrderPage


class TestOrderPage:
    driver = None
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
    samokats = [
        {
            'name': 'Истребитель',
            'surname': 'Хорибл',
            'address': 'Пушкина',
            'metro': 'Чистые пруды',
            'phone': '+79998877655',
            'date': '03.09.2005',
            'days_index': 1,
            'color_index': 0,
            'comment': 'сломался'
        },
        {
            'name': 'Орешник',
            'surname': 'Позитивный',
            'address': 'Колотушкина',
            'metro': 'Спортивная',
            'phone': '+79998877777',
            'date': '11.09.2023',
            'days_index': 0,
            'color_index': 1,
            'comment': 'Работает'
        }
    ]

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_header_button_opens_order_form(self):
        self.driver.get(self.BASE_URL)
        order_page = OrderPage(self.driver)
        order_page.click_order_header()
        current_url = self.driver.current_url
        expected_url = self.BASE_URL + 'order'
        assert current_url == expected_url
        assert order_page.wait_order_form()

    def test_down_button_opens_order_form(self):
        self.driver.get(self.BASE_URL)
        order_page = OrderPage(self.driver)
        order_page.scroll_to_order_button_down()
        order_page.click_order_down()
        current_url = self.driver.current_url
        expected_url = self.BASE_URL + 'order'
        assert current_url == expected_url
        assert order_page.wait_order_form()

    @pytest.mark.parametrize('samokats', samokats)
    def test_make_order_adds_new_samokat(self, samokats):
        self.driver.get(self.BASE_URL + 'order')
        order_page = OrderPage(self.driver)
        order_page.fill_order_form(
            samokats['name'],
            samokats['surname'],
            samokats['address'],
            samokats['metro'],
            samokats['phone'],
            samokats['date'],
            samokats['days_index'],
            samokats['color_index'],
            samokats['comment']
        )
        order_page.click_button_order()
        order_page.wait_pop_up_confirm()
        order_page.click_pop_up_button_confirm_yes()
        # todo Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
        # todo Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
        # todo Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
