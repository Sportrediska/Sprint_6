from selenium.webdriver.common.by import By

class HomePageLocators:
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[id^='accordion__heading-']")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "[id^='accordion__panel-']")
    
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")