def list_formatter(vacancies: list) -> list:
    """Функция изменяет формат полученного списка с сайта в упрощенный список."""
    vacancies_formatted = []
    for vacancy in vacancies:
        if vacancy["salary"]:
            if not (vacancy["salary"]["from"]):
                vacancy["salary"]["from"] = 0
            if not (vacancy["salary"]["to"]):
                vacancy["salary"]["to"] = 0
        else:
            vacancy["salary"] = 0
        vacancies_formatted.append(
            {
                "vacancy": vacancy["name"],
                "salary": vacancy["salary"],
                "url": vacancy["alternate_url"],
                "employer": vacancy["employer"]["name"],
            }
        )
    return vacancies_formatted