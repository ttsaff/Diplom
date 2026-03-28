from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    RESULTS = (By.CSS_SELECTOR, "a[href*='/film/']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def get_results_count(self) -> int:
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.RESULTS)
        )
        return len(elements)

    def open_first_movie(self) -> None:
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.RESULTS)
        )
        elements[0].click()
