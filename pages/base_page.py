import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу: {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Скроллить к элементу с индексом {index}')
    def scroll_to_by_index(self, locator, index):
        element = self.driver.find_elements(*locator)[index]
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скроллить к элементу')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидать появления любого из элементов')
    def wait_any_of_elements(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_any_elements_located(locator))

    @allure.step('Ожидать появления элемента')
    def wait_of_element(self, locator):
        return WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидать URL: {url}')
    def wait_of_url_to_be(self, url):
        return WebDriverWait(self.driver, 3).until(EC.url_to_be(url))

    @allure.step('Ожидать что URL содержит: {url}')
    def wait_until_url_contains(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_contains(url))

    @allure.step('Получить текст элемента с индексом {index}')
    def get_text_by_index(self, locator, index):
        return self.driver.find_elements(*locator)[index].text

    @allure.step('Кликнуть по элементу с индексом {index}')
    def click_by_index(self, locator, index):
        self.driver.find_elements(*locator)[index].click()

    @allure.step('Кликнуть по элементу')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввести текст: {value}')
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перейти на последнюю вкладку')
    def go_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
