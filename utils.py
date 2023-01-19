import json
from datetime import datetime


def get_schedule():
    """Чтение JSON файла и возвращение списка со словарями, в котором хранится информация об уроке"""
    with open("data/data2.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_schedule_by_day(weekday):
    """
    Возвращает список с уроками, которые проходят в день недели выбранном пользователем

            Параметры:
                    weekday (str): название дня недели

            Возвращаемое значение:
                    schedule_list (list): список со словарями уроков

            Исключение:
                    ValueError: при вводе weekday не строчного типа данных (str), возвращается пустой список (list)

    """
    schedule_list = []
    schedule_data = get_schedule()
    if weekday == 'понедельник':
        weekday = 'пн'
    elif weekday == 'вторник':
        weekday = 'вт'
    elif weekday == 'среда':
        weekday = 'ср'
    elif weekday == 'четверг':
        weekday = 'чт'
    elif weekday == 'пятница':
        weekday = 'пт'
    elif weekday == 'суббота':
        weekday = 'сб'
    elif weekday == 'воскресенье':
        weekday = 'вс'

    try:
        for lesson in schedule_data:
            if lesson["day_week"] == weekday:
                schedule_list.append(lesson)
        return schedule_list
    except ValueError:
        return []


def get_schedule_by_word(query):
    """
        Возвращает список с уроками, в названии которых используется введенное пользователем слово или совпадает с ним

                Параметры:
                        query (str): слово из названия дисциплины, которое ввел пользователь

                Возвращаемое значение:
                        schedule_list (list): список со словарями уроков

                Исключение:
                        ValueError: при вводе query не строчного типа данных (str), возвращается пустой список (list)

    """
    try:
        schedule_list = []
        data = get_schedule()
        for lesson in data:
            if query.lower() in lesson["discipline"].lower():
                schedule_list.append(lesson)
        return schedule_list
    except ValueError:
        return []


def get_schedule_for_tomorrow():
    """
        Возвращает список с уроками на завтра в настоящем времени

                Параметры:
                        не передаются

                Возвращаемое значение:
                        schedule_list (list): список со словарями уроков

                Исключение:
                        ValueError: при использовании ключа "day_week" не строчного типа данных (str) в data2.json,
                        возвращается пустой список (list)

    """
    now = datetime.now()
    tomorrow_weekday = datetime.weekday(now) + 1
    tomorrow_day = ''
    schedule_list = []
    week = {
        0: 'пн',
        1: 'вт',
        2: 'ср',
        3: 'чт',
        4: 'пт',
        5: 'сб',
        6: 'вс'
    }
    data = get_schedule()

    for k, v in week.items():
        if tomorrow_weekday == k:
            tomorrow_day = v

    try:
        for day in data:
            if day["day_week"] == tomorrow_day:
                schedule_list.append(day)
        return schedule_list
    except ValueError:
        return []


def get_schedule_for_today():
    """
        Возвращает список с уроками на сегодня в настоящем времени

                Параметры:
                        не передаются

                Возвращаемое значение:
                        schedule_list (list): список со словарями уроков

                Исключение:
                        ValueError: при использовании ключа "day_week" не строчного типа данных (str) в data2.json,
                        возвращается пустой список (list)

    """
    now = datetime.now()
    today_weekday = datetime.weekday(now)
    today_day = ''
    schedule_list = []
    week = {
        0: 'пн',
        1: 'вт',
        2: 'ср',
        3: 'чт',
        4: 'пт',
        5: 'сб',
        6: 'вс'
    }
    data = get_schedule()

    for k, v in week.items():
        if today_weekday == k:
            today_day = v

    try:
        for day in data:
            if day["day_week"] == today_day:
                schedule_list.append(day)
        return schedule_list
    except ValueError:
        return []
