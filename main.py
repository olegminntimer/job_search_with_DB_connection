from config import config
from src.create_database import create_database, save_data_to_database
from src.dbmanager import DBManager
from src.hh_data import HeadHunterAPI
from src.saver import JSONSaver


def main():
    employer_ids = {
        "80": "Альфа-Банк",
        "1740": "Яндекс",
        "4181": "ВТБ",
        "1373": "Аэрофлот",
        "39305": "Газпром нефть",
        "3388": "Газпромбанк",
        "15478": "VK",
        "4233": "X5 Group",
        "4219": "Tele2",
        "78638": "Тинькофф",
    }
    print("Запрашиваем данные с сайта HeadHunter(hh.ru)...")
    hh_api = HeadHunterAPI()
    data = hh_api.get_data(employer_ids)
    # print(data)
    print("Данные получены.")

    params = config()
    print("Создаем базу данных для хранения вакансий с сайта и сохраняем данные.")
    create_database('hh_employers_vacancies', params)
    save_data_to_database(data, 'hh_employers_vacancies', params)
    print("Данные записаны в базу данных.")
    file_save = JSONSaver()
    db_data = DBManager('hh_employers_vacancies', params)
    choice = "1"
    while choice in ("12345"):
        print("""
        Возможные действия с данными с сайта HeadHunter(hh.ru):
        
    1. Список всех компаний и количество вакансий у каждой компании - "companies_and_vacancies_count.json".
    
    2. Список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию - "all_vacancies.json".
    
    3. Средняя зарплата по вакансиям - "avg_salary.json".
    
    4. Список всех вакансий, у которых зарплата выше средней по всем вакансиям - "vacancies_with_higher_salary.json".
    
    5. Список всех вакансий, в названии которых содержатся переданные в метод слова, например python - "vacancies_with_keyword.json".
    
    Выход - любая цифра не из списка или любая буква.
        """)
        choice = input("Выберите пункт: ")
        if choice == "1":
            file_save.save_to(db_data.get_companies_and_vacancies_count(), "companies_and_vacancies_count.json")
            print("Данные записаны в 'companies_and_vacancies_count.json'.")
        elif choice == "2":
            file_save.save_to(db_data.get_all_vacancies(), "all_vacancies.json")
            print("Данные записаны в 'all_vacancies.json'.")
        elif choice == "3":
            avg_salary = int(db_data.get_avg_salary()[0][0])
            file_save.save_to([avg_salary], "avg_salary.json")
            print("Данные записаны в 'avg_salary.json'.")
        elif choice == "4":
            file_save.save_to(db_data.get_vacancies_with_higher_salary(), "vacancies_with_higher_salary.json")
            print("Данные записаны в 'vacancies_with_higher_salary.json'.")
        elif choice == "5":
            keyword = input("Введите ключевое слово поиска: ")
            file_save.save_to(db_data.get_vacancies_with_keyword(keyword), "vacancies_with_keyword.json")
            print("Данные записаны в 'vacancies_with_keyword.json'.")
    print("Программа завершена.")


if __name__ == '__main__':
    main()
