from selenium.webdriver.common.by import By


class SearchPage:
    MOVIE_ITEMS = (By.CSS_SELECTOR, ".search_results .element")
    FIRST_MOVIE = (By.CSS_SELECTOR, ".search_results .element a")

    def __init__(self, driver):
        self.driver = driver

    def get_results_count(self) -> int:
        return len(self.driver.find_elements(*self.MOVIE_ITEMS))

    def open_first_movie(self) -> None:
        self.driver.find_element(*self.FIRST_MOVIE).click()