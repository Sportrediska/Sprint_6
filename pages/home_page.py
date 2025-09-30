from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators as HPL


class HomePage(BasePage):

    def get_faq_question_text(self, index):
        return self.driver.find_elements(*HPL.FAQ_QUESTIONS)[index].text

    def get_faq_answer_text(self, index):
        return self.driver.find_elements(*HPL.FAQ_ANSWERS)[index].text

    def scroll_to_question(self, index):
        element = self.driver.find_elements(*HPL.FAQ_QUESTIONS)[index]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_faq_question(self, index):
        self.driver.find_elements(*HPL.FAQ_QUESTIONS)[index].click()

    def wait_question(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_any_elements_located(HPL.FAQ_QUESTIONS))

    def wait_answer(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_any_elements_located(HPL.FAQ_ANSWERS))

    def click_logo_yandex(self):
        self.driver.find_element(*HPL.LOGO_YANDEX).click()

    def click_logo_samokat(self):
        self.driver.find_element(*HPL.LOGO_SAMOKAT).click()