from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators as HPL


class HomePage(BasePage):

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

    def check_click_logo_samokat_sends_to(self, url):
        self.click_element(HPL.LOGO_SAMOKAT)
        return self.wait_of_url_to_be(url)

    def check_click_logo_yandex_sends_to(self, url):
        self.click_element(HPL.LOGO_YANDEX)
        self.go_to_last_tab()
        self.wait_until_url_contains(url)
        current_url = self.get_current_url()
        return url in current_url
