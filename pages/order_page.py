from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators as OPL
from pages.base_page import BasePage


class OrderPage(BasePage):

    def click_order_header(self):
        self.driver.find_element(*OPL.ORDER_BUTTON_HEADER).click()

    def click_order_down(self):
        self.driver.find_element(*OPL.ORDER_BUTTON_DOWN).click()

    def scroll_to_order_button_down(self):
        element = self.driver.find_element(*OPL.ORDER_BUTTON_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_order_form(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OPL.ORDER_FORM_TITLE_STEP_1))

    def fill_name(self, name):
        self.driver.find_element(*OPL.INPUT_NAME).send_keys(name)

    def fill_surname(self, surname):
        self.driver.find_element(*OPL.INPUT_SURNAME).send_keys(surname)

    def fill_address(self, address):
        self.driver.find_element(*OPL.INPUT_ADDRESS).send_keys(address)

    def click_metro(self):
        self.driver.find_element(*OPL.INPUT_METRO).click()

    def fill_metro(self, metro):
        self.driver.find_element(*OPL.INPUT_METRO).send_keys(metro)

    def click_first_metro_in_list(self):
        self.driver.find_element(*OPL.INPUT_METRO_OPTIONS).click()

    def fill_phone(self, phone):
        self.driver.find_element(*OPL.INPUT_PHONE).send_keys(phone)

    def click_button_next(self):
        self.driver.find_element(*OPL.BUTTON_NEXT).click()

    def wait_order_form_title_step_2(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OPL.ORDER_FORM_TITLE_STEP_2))

    def fill_date(self, date):
        self.driver.find_element(*OPL.INPUT_DATE).send_keys(date)

    def click_order_backside_element(self):
        self.driver.find_element(*OPL.ORDER_BACKSIDE_ELEMENT).click()

    def click_arenda_days(self):
        self.driver.find_element(*OPL.ARENDA_DAYS).click()

    def select_arenda_days(self, index):
        self.driver.find_elements(*OPL.ARENDA_DAYS_OPTIONS)[index].click()

    def click_checkbox_color(self, index):
        self.driver.find_elements(*OPL.CHECKBOX_COLOR)[index].click()

    def fill_comment(self, comment):
        self.driver.find_element(*OPL.INPUT_COMMENT).send_keys(comment)

    def click_button_order(self):
        self.driver.find_element(*OPL.BUTTON_ORDER).click()

    def wait_pop_up_confirm(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OPL.POP_UP_CONFIRM_ORDER))

    def click_pop_up_button_confirm_yes(self):
        self.driver.find_element(*OPL.POP_UP_BUTTON_CONFIRM_YES).click()

    def wait_pop_up_success_order(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OPL.POP_UP_SUCCESS_ORDER))

    def click_button_watch_status(self):
        self.driver.find_element(*OPL.BUTTON_WATCH_STATUS).click()



    def fill_order_form(self, name, surname, address, metro, phone, date, days_index, color_index, comment):
        self.wait_order_form()
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.click_metro()
        self.fill_metro(metro)
        self.click_first_metro_in_list()
        self.fill_phone(phone)
        self.click_button_next()
        self.wait_order_form_title_step_2()
        self.fill_date(date)
        self.click_order_backside_element()
        self.click_arenda_days()
        self.select_arenda_days(days_index)
        self.click_checkbox_color(color_index)
        self.fill_comment(comment)
