from typing import Any
import requests

from src.utils import list_formatter


class HeadHunterAPI:
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        """Конструктор класса HeadHunter для поиска вакансий."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.data = []

    def get_data(self, hh_employer_ids: dict) -> list[dict[str, Any]]:
        """Метод загрузки вакансий по списку работодателей."""
        for key, value in hh_employer_ids.items():
            response = requests.get(f"{self.__url}?employer_id={key}", headers=self.__headers,
                                    params=self.__params)
            vacancies = response.json()["items"]
            self.data.append({
                'employer': {"hh_employer_id": key, "name": value},
                'vacancies': list_formatter(vacancies)
            })
        return self.data
