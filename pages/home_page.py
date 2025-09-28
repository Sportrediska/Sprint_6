from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[id^='accordion__heading-']")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "[id^='accordion__panel-']")

    def __init__(self, driver):
        self.driver = driver

    def get_faq_question_text(self, index):
        return self.driver.find_elements(*self.FAQ_QUESTIONS)[index].text

    def get_faq_answer_text(self, index):
        return self.driver.find_elements(*self.FAQ_ANSWERS)[index].text

    def scroll_to_question(self, index):
        element = self.driver.find_elements(*self.FAQ_QUESTIONS)[index]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_faq_question(self, index):
        self.driver.find_elements(*self.FAQ_QUESTIONS)[index].click()

    def wait_question(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_any_elements_located(self.FAQ_QUESTIONS))

    def wait_answer(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_any_elements_located(self.FAQ_ANSWERS))
