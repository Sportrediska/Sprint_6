from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def scroll_to_by_index(self, locator, index):
        element = self.driver.find_elements(*locator)[index]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_any_of_elements(self, locator):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_any_elements_located(locator))

    def get_text_by_index(self, locator, index):
        return self.driver.find_elements(*locator)[index].text

    def click_by_index(self, locator, index):
        self.driver.find_elements(*locator)[index].click()
