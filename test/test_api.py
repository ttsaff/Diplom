import pytest
import allure
from api.movie_api import MovieAPI


@allure.title("Поиск фильма по названию")
@allure.story("Movie search")
@pytest.mark.api
def test_search_movie():
    with allure.step("Отправка запроса"):
        response = MovieAPI.search_movie("Cars")

    with allure.step("Проверка статуса"):
        assert response.status_code == 200

    with allure.step("Проверка наличия результатов"):
        assert len(response.json()["docs"]) > 0


@allure.title("Получение случайного фильма")
@allure.story("Random movie")
@pytest.mark.api
def test_random_movie():
    with allure.step("Отправка запроса"):
        response = MovieAPI.get_random_movie()

    with allure.step("Проверка статуса"):
        assert response.status_code == 200

    with allure.step("Проверка ID"):
        assert "id" in response.json()


@allure.title("Поиск фильма по ID")
@allure.story("Movie by ID")
@pytest.mark.api
def test_get_movie_by_id():
    movie = MovieAPI.get_random_movie().json()
    movie_id = movie["id"]

    with allure.step("Запрос по ID"):
        response = MovieAPI.get_movie_by_id(movie_id)

    with allure.step("Проверка статуса"):
        assert response.status_code == 200

    with allure.step("Проверка совпадения ID"):
        assert response.json()["id"] == movie_id


@allure.title("Поиск с limit=0")
@allure.story("Negative cases")
@pytest.mark.api
def test_search_limit_zero():
    response = MovieAPI.search_movie("Cars", limit=0)
    assert response.status_code == 400


@allure.title("Поиск по некорректному ID")
@allure.story("Negative cases")
@pytest.mark.api
def test_invalid_movie_id():
    response = MovieAPI.get_movie_by_id(999999999999)
    assert response.status_code == 400


@allure.title("Поиск без токена")
@allure.story("Negative cases")
@pytest.mark.api
def test_without_token():
    import requests

    response = requests.get(
        "https://api.poiskkino.dev/v1.4/movie/1"
    )

    assert response.status_code == 401


@allure.title("Неверный метод")
@allure.story("Negative cases")
@pytest.mark.api
def test_wrong_method():
    import requests

    response = requests.put(
        "https://api.poiskkino.dev/v1.4/movie/1"
    )

    assert response.status_code in (401, 404)
