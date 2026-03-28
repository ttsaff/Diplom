from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SearchPage:
    RESULTS = (By.CSS_SELECTOR, "a[href*='/film/']")

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы поиска"""
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 15)

    def get_results_count(self) -> int:
        """Получить количество результатов поиска"""
        elements: List[WebElement] = self.wait.until(
            EC.presence_of_all_elements_located(self.RESULTS)
        )
        return len(elements)

    def open_first_movie(self) -> None:
        """Открыть первый фильм из результатов"""
        elements: List[WebElement] = self.wait.until(
            EC.presence_of_all_elements_located(self.RESULTS)
        )
        elements[0].click()