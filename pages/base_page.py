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

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_any_of_elements(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_any_elements_located(locator))

    def wait_of_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    def wait_of_url_to_be(self, url):
        return WebDriverWait(self.driver, 3).until(EC.url_to_be(url))

    def wait_until_url_contains(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_contains(url))

    def get_text_by_index(self, locator, index):
        return self.driver.find_elements(*locator)[index].text

    def click_by_index(self, locator, index):
        self.driver.find_elements(*locator)[index].click()

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def get_current_url(self):
        return self.driver.current_url

    def go_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
