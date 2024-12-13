from src.hh_api import HeadHunterAPI


def main():
    employers = [
        "80", # "Альфа-Банк"
        "1740", # "Яндекс"
        "4181",# "ВТБ"
        "1373",# "Аэрофлот"
        "39305",# "Газпром нефть"
        "3388",# "Газпромбанк"
        "15478",# "VK"
        "999442",# "X5 Group"
        "4219",# "Tele2"
        "2324020",# "Тинькофф"
    ]
    hh_api = HeadHunterAPI()
    employers_list = hh_api.get_employers()
    print(employers_list)
    # for employer in employers_list:
    #     if employer["open_vacancies"] > 0:
    #         print(employer["name"]+" "+str(employer["open_vacancies"]))


if __name__ == '__main__':
    main()
