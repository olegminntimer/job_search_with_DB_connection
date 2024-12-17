from typing import Any

import psycopg2


class DBManager:
    """Подключение к базе данных и анализ вакансий с hh.ru."""

    def __init__(self, dbname: str, params: dict):
        """Конструктор класса DBManager."""
        self.dbname = dbname
        self.params = params

    def get_to_database(self, query: str) -> list[tuple, Any]:
        """Выполняет запрос query к базе данных."""
        conn = psycopg2.connect(dbname=self.dbname, **self.params)
        with conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return  result


    def get_companies_and_vacancies_count(self):
        """Получаем список всех компаний и количество вакансий у каждой компании."""
        query = """
                SELECT employers.name, COUNT(vacancies.employer_id)
                FROM employers
                JOIN vacancies USING (employer_id)
                GROUP BY employer_id
                """
        return self.get_to_database(query)

    def get_all_vacancies(self):
        """Получаем список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        query = """
                SELECT employers.name, vacancies.name, vacancies.salary, vacancies.url
                FROM employers
                JOIN vacancies USING (employer_id)
                """
        return self.get_to_database(query)

    def get_avg_salary(self):
        """Получаем среднюю зарплату по вакансиям."""
        query = """
                SELECT AVG(vacancies.salary) FROM vacancies
                """
        return self.get_to_database(query)

    def get_vacancies_with_higher_salary(self):
        """Получаем список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        query = """
                SELECT * FROM vacancies WHERE vacancies.salary > (SELECT AVG(vacancies.salary) FROM vacancies)
                """
        return self.get_to_database(query)

    def get_vacancies_with_keyword(self, key_word: str):
        """Получаем список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        При поиске отбрасывается первая буква."""
        key_word = f"%{key_word[1:]}%"
        conn = psycopg2.connect(dbname=self.dbname, **self.params)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT employers.name, vacancies.name, vacancies.salary, vacancies.url 
                FROM employers
                JOIN vacancies USING (employer_id) 
                WHERE vacancies.name LIKE (%s)
                """,
                (key_word,))
            result = cur.fetchall()
        conn.commit()
        conn.close()
        return result
