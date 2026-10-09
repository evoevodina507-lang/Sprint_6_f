from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # --- Поиск и действия с элементами ---

    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        element.click()

    def click_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    # --- Обёртки над driver ---

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def get_window_handles(self):
        return self.driver.window_handles

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    # --- Ожидания ---

    def wait_for_condition(self, condition):
        return self.wait.until(condition)

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_url_contains(self, substring):
        return self.wait.until(
            lambda driver: substring in driver.current_url
        )

    def wait_for_new_window(self):
        return self.wait.until(
            lambda driver: len(driver.window_handles) > 1
        )