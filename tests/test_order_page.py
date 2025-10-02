import allure
import pytest
from selenium import webdriver
from urls import Urls
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data_for_tests import DataForTests as Data


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка открытия формы заказа по кнопке "Заказать" в header')
    def test_header_button_opens_order_form(self):
        order_page = OrderPage(self.driver)
        order_page.open_page(Urls.BASE_URL)
        current_url = order_page.get_url_after_click_header_button()
        assert current_url == Urls.ORDER_URL
        assert order_page.wait_order_form()

    @allure.title('Проверка открытия формы заказа по кнопке "Заказать" в блоке "Как это работает"')
    def test_down_button_opens_order_form(self):
        order_page = OrderPage(self.driver)
        order_page.open_page(Urls.BASE_URL)
        current_url = order_page.get_url_after_click_down_button()
        assert current_url == Urls.ORDER_URL
        assert order_page.wait_order_form()

    @allure.title('Проверка оформления заказа самоката')
    @pytest.mark.parametrize('samokats', Data.samokats)
    def test_make_order_adds_new_samokat(self, samokats):
        order_page = OrderPage(self.driver)
        order_page.open_page(Urls.ORDER_URL)
        order_page.make_order(
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
        assert order_page.check_success_order()

        order_page.click_button_watch_status()

        home_page = HomePage(self.driver)
        assert home_page.check_click_logo_samokat_sends_to(Urls.BASE_URL)
        assert home_page.check_click_logo_yandex_sends_to('dzen.ru')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
