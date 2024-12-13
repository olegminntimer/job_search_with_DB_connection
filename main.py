from src.hh_api import HeadHunterAPI


def main():
    employer_ids = [
        "80", # "Альфа-Банк"
        "1740", # "Яндекс"
        # "4181",# "ВТБ"
        # "1373",# "Аэрофлот"
        # "39305",# "Газпром нефть"
        # "3388",# "Газпромбанк"
        # "15478",# "VK"
        # "4233",# "X5 Group"
        # "4219",# "Tele2"
        # "78638",# "Тинькофф"
        # "Альфа-Банк",
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
    data = hh_api.get_vacancies(employer_ids)

    print(data)


if __name__ == '__main__':
    main()
