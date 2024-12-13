from src.hh_api import HeadHunterAPI


def main():
    employers = [
        # "80", # "Альфа-Банк"
        # "1740", # "Яндекс"
        # "4181",# "ВТБ"
        # "1373",# "Аэрофлот"
        # "39305",# "Газпром нефть"
        # "3388",# "Газпромбанк"
        # "15478",# "VK"
        # "4233",# "X5 Group"
        # "4219",# "Tele2"
        # "78638",# "Тинькофф"
        "Альфа-Банк",
        # "Яндекс",
        # "ВТБ",
        # "Аэрофлот",
        # "Газпром нефть",
        # "Газпромбанк",
        # "VK",
        # "X5 Group",
        # "Tele2",
        # "Тинькофф",
    ]
    hh_api = HeadHunterAPI()
    vacancies_list = []
    i_count = 1
    for employer in employers:
        # vacancies_list.extend(hh_api.get_vacancies(employer))
        print(i_count, end="-")
        i_count += 1
    print()
    print(vacancies_list)
    # for employer in employers_list:
    #     if employer["open_vacancies"] > 0:
    #         print(employer["name"]+" "+str(employer["open_vacancies"]))


if __name__ == '__main__':
    main()
