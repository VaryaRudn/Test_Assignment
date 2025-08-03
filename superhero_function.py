import requests

def tallest_superhero(gender, bool_work):

    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    heros = response.json()

    tallest_height = 0
    tallest_hero = ''

    for hero in heros:

        heros_gender = hero["appearance"]["gender"]
        heros_work = hero["work"]["occupation"]

        heros_height_str = hero["appearance"]["height"][1]
        if 'meters' in heros_height_str:
            heros_height = float(heros_height_str.split()[0])*100
        else:
            heros_height = float(heros_height_str.split()[0])

        #bool_work = work != '-'
        bool_heros_work = heros_work != '-'

        if gender == heros_gender and bool_work == bool_heros_work:
            if heros_height > tallest_height:
                tallest_height = heros_height
                tallest_hero = hero["name"]
    return tallest_hero if tallest_hero else "Подходящих героев не найдено"





