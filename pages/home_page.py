from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators as HPL


class HomePage(BasePage):

    def click_logo_yandex(self):
        self.driver.find_element(*HPL.LOGO_YANDEX).click()

    def click_logo_samokat(self):
        self.driver.find_element(*HPL.LOGO_SAMOKAT).click()

    def check_question_text(self, index, question):
        self.scroll_to_by_index(HPL.FAQ_QUESTIONS, index)
        self.wait_any_of_elements(HPL.FAQ_QUESTIONS)
        question_text = self.get_text_by_index(HPL.FAQ_QUESTIONS, index)
        return question_text == question

    def check_answer_text(self, index, answer):
        self.click_by_index(HPL.FAQ_QUESTIONS, index)
        self.wait_any_of_elements(HPL.FAQ_ANSWERS)
        answer_text = self.get_text_by_index(HPL.FAQ_ANSWERS, index)
        return answer_text == answer
