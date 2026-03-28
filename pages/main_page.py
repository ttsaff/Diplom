from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='kp_query']")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация главной страницы"""
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 15)

    def open(self, url: str) -> None:
        """Открыть страницу по URL"""
        self.driver.get(url)

    def search(self, query: str) -> None:
        """Выполнить поиск фильма"""
        search_input = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(query)
        search_input.submit()
