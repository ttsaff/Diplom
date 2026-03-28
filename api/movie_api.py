import requests
from typing import Dict, Optional
from config.config import BASE_URL, API_KEY
import time


class MovieAPI:
    headers: Dict[str, str] = {
        "X-API-KEY": API_KEY if API_KEY else ""
    }

    @staticmethod
    def _make_request(url: str, params: Optional[Dict] = None, retries: int = 3) -> requests.Response:
        """Helper с retry и обработкой ошибок"""
        for attempt in range(retries):
            try:
                response: requests.Response = requests.get(
                    url,
                    headers=MovieAPI.headers,
                    params=params,
                    timeout=20,
                    verify=False
                )
                return response
            except (requests.exceptions.Timeout, 
                    requests.exceptions.SSLError, 
                    requests.exceptions.ConnectionError) as e:
                if attempt < retries - 1:
                    wait_time: int = 2 ** attempt
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise

    @staticmethod
    def search_movie(query: str, limit: int = 2) -> requests.Response:
        """Поиск фильма по названию"""
        return MovieAPI._make_request(
            f"{BASE_URL}movie/search",
            params={
                "page": 1,
                "limit": limit,
                "query": query
            }
        )

    @staticmethod
    def get_random_movie() -> requests.Response:
        """Получение случайного фильма (через поиск популярных)"""
        return MovieAPI._make_request(
            f"{BASE_URL}movie/search",
            params={
                "page": 1,
                "limit": 1,
                "query": "The"
            }
        )

    @staticmethod
    def get_movie_by_id(movie_id: int) -> requests.Response:
        """Получение фильма по ID"""
        return MovieAPI._make_request(
            f"{BASE_URL}movie/{movie_id}"
        )
