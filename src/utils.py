def list_formatter(vacancies: list) -> list:
    """Функция изменяет формат полученного списка с сайта в упрощенный список."""
    vacancies_formatted = []
    for vacancy in vacancies:
        vacancy_salary = 0
        if vacancy["salary"]:
            if vacancy["salary"]["from"]:
                vacancy_salary = vacancy["salary"]["from"]
            else:
                if vacancy["salary"]["to"]:
                    vacancy_salary = vacancy["salary"]["to"]
        vacancies_formatted.append(
            {
                "name": vacancy["name"],
                "salary": vacancy_salary,
                "url": vacancy["alternate_url"],
                # "employer_id": vacancy["employer"]["id"],
            }
        )
    return vacancies_formatted
