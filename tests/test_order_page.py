import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from pages.home_page import HomePage
from pages.order_page import OrderPage
from selenium.webdriver.support import expected_conditions as EC
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
        order_page.click_order_header()
        current_url = self.driver.current_url
        expected_url = Urls.ORDER_URL
        assert current_url == expected_url
        assert order_page.wait_order_form()

    @allure.title('Проверка открытия формы заказа по кнопке "Заказать" в блоке "Как это работает"')
    def test_down_button_opens_order_form(self):
        order_page = OrderPage(self.driver)
        order_page.open_page(Urls.BASE_URL)
        order_page.scroll_to_order_button_down()
        order_page.click_order_down()
        current_url = self.driver.current_url
        expected_url = Urls.ORDER_URL
        assert current_url == expected_url
        assert order_page.wait_order_form()

    @allure.title('Проверка оформления заказа самоката')
    @pytest.mark.parametrize('samokats', Data.samokats)
    def test_make_order_adds_new_samokat(self, samokats):
        order_page = OrderPage(self.driver)
        order_page.open_page(Urls.ORDER_URL)
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
        assert WebDriverWait(self.driver, 3).until(EC.url_to_be(Urls.BASE_URL))

        home_page.click_logo_yandex()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(EC.url_contains('dzen.ru'))
        current_url = self.driver.current_url
        assert 'dzen.ru' in current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
