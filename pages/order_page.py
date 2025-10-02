import allure

from locators.order_page_locators import OrderPageLocators as OPL
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Получить URL после клика по кнопке в хедере')
    def get_url_after_click_header_button(self):
        self.click_element(OPL.ORDER_BUTTON_HEADER)
        return self.get_current_url()

    @allure.step('Получить URL после клика по нижней кнопке')
    def get_url_after_click_down_button(self):
        self.scroll_to_element(OPL.ORDER_BUTTON_DOWN)
        self.click_element(OPL.ORDER_BUTTON_DOWN)
        return self.get_current_url()

    @allure.step('Кликнуть кнопку "Посмотреть статус"')
    def click_button_watch_status(self):
        self.click_element(OPL.BUTTON_WATCH_STATUS)

    @allure.step('Ожидать форму заказа')
    def wait_order_form(self):
        return self.wait_of_element(OPL.ORDER_FORM_TITLE_STEP_1)

    @allure.step('Оформить заказ: {name} {surname}')
    def make_order(self, name, surname, address, metro, phone, date, days_index, color_index, comment):
        # fill form step 1
        self.wait_of_element(OPL.ORDER_FORM_TITLE_STEP_1)
        self.send_keys(OPL.INPUT_NAME, name)
        self.send_keys(OPL.INPUT_SURNAME, surname)
        self.send_keys(OPL.INPUT_ADDRESS, address)
        self.click_element(OPL.INPUT_METRO)
        self.send_keys(OPL.INPUT_METRO, metro)
        self.click_element(OPL.INPUT_METRO_OPTIONS)
        self.send_keys(OPL.INPUT_PHONE, phone)
        self.click_element(OPL.BUTTON_NEXT)
        # fill form step 2
        self.wait_of_element(OPL.ORDER_FORM_TITLE_STEP_2)
        self.send_keys(OPL.INPUT_DATE, date)
        self.click_element(OPL.ORDER_BACKSIDE_ELEMENT)
        self.click_element(OPL.ARENDA_DAYS)
        self.click_by_index(OPL.ARENDA_DAYS_OPTIONS, days_index)
        self.click_by_index(OPL.CHECKBOX_COLOR, color_index)
        self.send_keys(OPL.INPUT_COMMENT, comment)
        self.click_element(OPL.BUTTON_ORDER)
        # confirm order
        self.wait_of_element(OPL.POP_UP_CONFIRM_ORDER)
        self.click_element(OPL.POP_UP_BUTTON_CONFIRM_YES)

    @allure.step('Проверить успешное оформление заказа')
    def check_success_order(self):
        return self.wait_of_element(OPL.POP_UP_SUCCESS_ORDER)
