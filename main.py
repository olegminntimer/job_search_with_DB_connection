from config import config
from src.create_database import create_database, save_data_to_database
from src.dbmanager import DBManager
from src.hh_data import HeadHunterAPI


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

    hh_api = HeadHunterAPI()
    data = hh_api.get_data(employer_ids)
    # print(data)

    params = config()
    create_database('hh_employers_vacancies', params)
    save_data_to_database(data, 'hh_employers_vacancies', params)
    db_data = DBManager('hh_employers_vacancies', params)
    # print(db_data.get_companies_and_vacancies_count())
    # print(db_data.get_all_vacancies())
    # print(db_data.get_avg_salary())
    # print(db_data.get_vacancies_with_higher_salary())
    print(db_data.get_vacancies_with_keyword('разработ'))


if __name__ == '__main__':
    main()
