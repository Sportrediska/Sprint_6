import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from pages.order_page import OrderPage
from selenium.webdriver.support import expected_conditions as EC


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
        assert order_page.wait_pop_up_success_order()

        home_page = HomePage(self.driver)
        order_page.click_button_watch_status()
        home_page.click_logo_samokat()
        assert WebDriverWait(self.driver, 3).until(EC.url_to_be(self.BASE_URL))

        home_page.click_logo_yandex()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains('dzen.ru'))
        current_url = self.driver.current_url
        assert 'dzen.ru' in current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
