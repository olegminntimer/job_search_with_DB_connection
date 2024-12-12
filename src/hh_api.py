import requests
import os


class HeadHunterAPI:
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        """Конструктор класса HeadHunter"""
        # self.__url = "https://api.hh.ru"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.employers = []

    def get_employers(self, keyword: str = "") -> list:
        """Метод загрузки списка работодателей с открытыми вакансиями в количестве больше 0."""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get("https://api.hh.ru/employers", headers=self.__headers, params=self.__params)
            # if response.status_code != 200:
            #     continue
            employers = response.json()["items"]
            self.employers.extend(employers)
            self.__params["page"] += 1
        return self.employers

    # def get_vacancies(self, keyword: str = "") -> list:
    #     """Метод загрузки вакансий с НН"""
    #     self.__params["text"] = keyword
    #     while self.__params.get("page") != 20:
    #         response = requests.get(self.__url, headers=self.__headers, params=self.__params)
    #         # if response.status_code != 200:
    #         #     continue
    #         vacancies = response.json()["items"]
    #         self.vacancies.extend(vacancies)
    #         self.__params["page"] += 1
    #     return self.vacancies


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    employers_list = hh_api.get_employers()
    # print(employers_list)
    for employer in employers_list:
        if employer["open_vacancies"] > 0:
            print(employer["name"]+" "+str(employer["open_vacancies"]))
