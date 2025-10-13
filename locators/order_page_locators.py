from selenium.webdriver.common.by import By

class OrderPageLocators:
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