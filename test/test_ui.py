import pytest
import allure
from pages.main_page import MainPage
from pages.search_page import SearchPage
from config.config import UI_URL


@allure.title("Поиск фильма")
@allure.story("Search")
@pytest.mark.ui
def test_search_movie(driver):
    main = MainPage(driver)

    with allure.step("Открываем сайт"):
        main.open(UI_URL)

    with allure.step("Ищем фильм"):
        main.search("Интерстеллар")

    search = SearchPage(driver)

    with allure.step("Проверяем результаты"):
        assert search.get_results_count() > 0


@allure.title("Открытие карточки фильма")
@allure.story("Movie page")
@pytest.mark.ui
def test_open_movie_card(driver):
    main = MainPage(driver)
    main.open(UI_URL)
    main.search("Интерстеллар")

    search = SearchPage(driver)

    with allure.step("Открываем первый фильм"):
        search.open_first_movie()

    with allure.step("Проверяем что открылась страница"):
        assert "film" in driver.current_url


@allure.title("Проверка title страницы")
@allure.story("UI")
@pytest.mark.ui
def test_title(driver):
    main = MainPage(driver)

    with allure.step("Открываем сайт"):
        main.open(UI_URL)

    assert "Кинопоиск" in driver.title


@allure.title("Проверка URL после поиска")
@allure.story("Search")
@pytest.mark.ui
def test_search_url(driver):
    main = MainPage(driver)
    main.open(UI_URL)
    main.search("Матрица")

    assert "search" in driver.current_url


@allure.title("Проверка перехода по фильму")
@allure.story("Navigation")
@pytest.mark.ui
def test_navigation(driver):
    main = MainPage(driver)
    main.open(UI_URL)
    main.search("Гарри Поттер")

    search = SearchPage(driver)
    search.open_first_movie()

    assert "film" in driver.current_url
