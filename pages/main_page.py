from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_INPUT = (By.NAME, "kp_query")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str) -> None:
        self.driver.get(url)

    def search(self, query: str) -> None:
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(query)
        self.driver.find_element(*self.SEARCH_BUTTON).click()