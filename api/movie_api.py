import requests
from config.config import BASE_URL, API_KEY


class MovieAPI:
    headers = {
    "X-API-KEY": API_KEY if API_KEY else ""
    }

    @staticmethod
    def search_movie(query: str, limit: int = 2):
        return requests.get(
            f"{BASE_URL}movie/search",
            headers=MovieAPI.headers,
            params={"page": 1, "limit": limit, "query": query}
        )

    @staticmethod
    def get_random_movie():
        return requests.get(
            f"{BASE_URL}movie/random",
            headers=MovieAPI.headers,
            params={
                "notNullFields": "name",
                "type": "movie",
                "status": "completed"
            }
        )

    @staticmethod
    def get_movie_by_id(movie_id: int):
        return requests.get(
            f"{BASE_URL}movie/{movie_id}",
            headers=MovieAPI.headers
        )
