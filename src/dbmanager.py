class DBManager:
    """Подключение к базе данных и анализ вакансий с hh.ru."""

    def __init__(self, dbname: str, params: dict):
        """Конструктор класса DBManager."""
        self.dbname = dbname
        self.params = params

    def get_companies_and_vacancies_count():
        """Получаем список всех компаний и количество вакансий у каждой компании."""
        pass

    def get_all_vacancies():
        """Получаем список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        pass

    def get_avg_salary():
        """Получаем среднюю зарплату по вакансиям."""
        pass

    def get_vacancies_with_higher_salary():
        """Получаем список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword():
        """Получаем список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        pass
