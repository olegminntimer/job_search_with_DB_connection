from typing import Any
import requests

from src.utils import list_formatter


class HeadHunterAPI:
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        """Конструктор класса HeadHunter для поиска вакансий."""
        # self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def get_vacancies(self, employer_ids: list[str]) -> list[dict[str, Any]]:
        """Метод загрузки вакансий по списку работодателей."""
        i_count = 1
        for employer_id in employer_ids:
            # self.__params["text"] = employer
            # while self.__params.get("page") != 20:
            response = requests.get(f"https://api.hh.ru/vacancies?employer_id={employer_id}", headers=self.__headers,
                                    params=self.__params)
            # if response.status_code != 200:
            #     continue
            vacancies = list_formatter(response.json()["items"])
            self.vacancies.extend(vacancies)
            # self.__params["page"] += 1
            print(i_count, end=".")
            i_count += 1
        print()
        return self.vacancies
