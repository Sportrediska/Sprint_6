import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, '.Header_Nav__AGCXC .Button_Button__ra12g')
    ORDER_BUTTON_DOWN = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')
    ORDER_FORM_TITLE_STEP_1 = (By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Для кого самокат']")
    ORDER_FORM_TITLE_STEP_2 = (By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Про аренду']")
    ORDER_BACKSIDE_ELEMENT = (By.CLASS_NAME, 'App_App__15LM-')

    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    INPUT_METRO_OPTIONS = (By.CSS_SELECTOR, ".select-search__select .select-search__row")
    INPUT_PHONE = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".Order_NextButton__1_rCA .Button_Button__ra12g.Button_Middle__1CSJM")

    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    ARENDA_DAYS = (By.CLASS_NAME, "Dropdown-placeholder")
    ARENDA_DAYS_OPTIONS = (By.CLASS_NAME, "Dropdown-option")
    CHECKBOX_COLOR = (By.CLASS_NAME, "Checkbox_Input__14A2w")
    INPUT_COMMENT = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.CSS_SELECTOR, ".Order_Buttons__1xGrp .Button_Button__ra12g.Button_Middle__1CSJM:not(.Button_Inverted__3IF-i)")

    POP_UP_CONFIRM_ORDER = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    POP_UP_BUTTON_CONFIRM_YES = (By.CSS_SELECTOR, ".Order_Modal__YZ-d3 .Button_Button__ra12g.Button_Middle__1CSJM:not(.Button_Inverted__3IF-i)")
    POP_UP_SUCCESS_ORDER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    BUTTON_WATCH_STATUS = (By.CSS_SELECTOR, ".Order_NextButton__1_rCA .Button_Button__ra12g.Button_Middle__1CSJM")

    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    def __init__(self, driver):
        self.driver = driver

    def click_order_header(self):
        self.driver.find_element(*self.ORDER_BUTTON_HEADER).click()

    def click_order_down(self):
        self.driver.find_element(*self.ORDER_BUTTON_DOWN).click()

    def scroll_to_order_button_down(self):
        element = self.driver.find_element(*self.ORDER_BUTTON_DOWN)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_order_form(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.ORDER_FORM_TITLE_STEP_1))

    def fill_name(self, name):
        self.driver.find_element(*self.INPUT_NAME).send_keys(name)

    def fill_surname(self, surname):
        self.driver.find_element(*self.INPUT_SURNAME).send_keys(surname)

    def fill_address(self, address):
        self.driver.find_element(*self.INPUT_ADDRESS).send_keys(address)

    def click_metro(self):
        self.driver.find_element(*self.INPUT_METRO).click()

    def fill_metro(self, metro):
        self.driver.find_element(*self.INPUT_METRO).send_keys(metro)

    def click_first_metro_in_list(self):
        self.driver.find_element(*self.INPUT_METRO_OPTIONS).click()

    def fill_phone(self, phone):
        self.driver.find_element(*self.INPUT_PHONE).send_keys(phone)

    def click_button_next(self):
        self.driver.find_element(*self.BUTTON_NEXT).click()

    def wait_order_form_title_step_2(self):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.ORDER_FORM_TITLE_STEP_2))

    def fill_date(self, date):
        self.driver.find_element(*self.INPUT_DATE).send_keys(date)

    def click_order_backside_element(self):
        self.driver.find_element(*self.ORDER_BACKSIDE_ELEMENT).click()

    def click_arenda_days(self):
        self.driver.find_element(*self.ARENDA_DAYS).click()

    def select_arenda_days(self, index):
        self.driver.find_elements(*self.ARENDA_DAYS_OPTIONS)[index].click()

    def click_checkbox_color(self, index):
        self.driver.find_elements(*self.CHECKBOX_COLOR)[index].click()

    def fill_comment(self, comment):
        self.driver.find_element(*self.INPUT_COMMENT).send_keys(comment)

    def click_button_order(self):
        self.driver.find_element(*self.BUTTON_ORDER).click()

    def wait_pop_up_confirm(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.POP_UP_CONFIRM_ORDER))

    def click_pop_up_button_confirm_yes(self):
        self.driver.find_element(*self.POP_UP_BUTTON_CONFIRM_YES).click()

    def wait_pop_up_success_order(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.POP_UP_SUCCESS_ORDER))

    def click_button_watch_status(self):
        self.driver.find_element(*self.BUTTON_WATCH_STATUS).click()

    def click_logo_yandex(self):
        self.driver.find_element(*self.LOGO_YANDEX).click()

    def click_logo_samokat(self):
        self.driver.find_element(*self.LOGO_SAMOKAT).click()

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
