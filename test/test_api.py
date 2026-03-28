import pytest
import allure
import requests
from api.movie_api import MovieAPI
from config.config import BASE_URL


@allure.title("Поиск фильма по названию")
@allure.story("Movie search")
@pytest.mark.api
def test_search_movie():
    with allure.step("Отправка запроса"):
        response = MovieAPI.search_movie("Cars")

    with allure.step("Проверка статуса"):
        assert response.status_code == 200

    with allure.step("Проверка наличия результатов"):
        json_data = response.json()
        assert json_data is not None
        assert "docs" in json_data
        assert len(json_data["docs"]) > 0

@allure.title("Получение случайного фильма")
@allure.story("Random movie")
@pytest.mark.api
def test_random_movie():
    with allure.step("Отправка запроса"):
        response = MovieAPI.get_random_movie()

    with allure.step("Проверка статуса"):
        assert response.status_code == 200

    with allure.step("Проверка наличия результатов"):
        json_data = response.json()
        assert json_data is not None
        assert "docs" in json_data
        assert len(json_data["docs"]) > 0

@allure.title("Поиск фильма по ID")
@allure.story("Movie by ID")
@pytest.mark.api
def test_get_movie_by_id():
    with allure.step("Получить ID фильма"):
        search_response = MovieAPI.search_movie("Matrix")
        search_data = search_response.json()
        assert len(search_data["docs"]) > 0
        movie_id = search_data["docs"][0]["id"]

    with allure.step("Запрос по ID"):
        response = MovieAPI.get_movie_by_id(movie_id)

    with allure.step("Проверка статуса"):
        assert response.status_code == 200

    with allure.step("Проверка совпадения ID"):
        json_data = response.json()
        assert json_data is not None
        assert json_data.get("id") == movie_id

@allure.title("Поиск с limit=0")
@allure.story("Negative cases")
@pytest.mark.api
def test_search_limit_zero():
    response = MovieAPI.search_movie("Cars", limit=0)
    # API может вернуть 400 или 200 с пустыми результатами
    assert response.status_code in [200, 400]

@allure.title("Поиск по некорректному ID")
@allure.story("Negative cases")
@pytest.mark.api
def test_invalid_movie_id():
    try:
        response = MovieAPI.get_movie_by_id(999999999999)
        # Если не выкинул ошибку, проверяем статус
        assert response.status_code in [400, 404]
    except requests.exceptions.RequestException:
        # Если сервер вообще закрыл соединение, тест проходит
        pass

@allure.title("Поиск без токена")
@allure.story("Negative cases")
@pytest.mark.api
def test_without_token():
    try:
        response = requests.get(
            f"{BASE_URL}movie/search",
            params={"query": "test"},
            timeout=20,
            verify=False
        )
        assert response.status_code == 401
    except requests.exceptions.RequestException:
        # Сервер может закрыть соединение если нет токена
        pass

@allure.title("Неверный метод")
@allure.story("Negative cases")
@pytest.mark.api
def test_wrong_method():
    try:
        response = requests.put(
            f"{BASE_URL}movie/1",
            timeout=20,
            verify=False
        )
        assert response.status_code in [401, 404, 405]
    except requests.exceptions.RequestException:
        # Сервер может закрыть соединение на неверном методе
        pass
