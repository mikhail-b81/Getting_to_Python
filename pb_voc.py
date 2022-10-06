

def dict_action():
    """
    Содержит перечень доступных команд (действий со справочником)
    Возвращает по ключу:
    0 - строка заголовок словаря
    1 - словарь
    2 - ключи словаря
    """
    dict_title = 'Выбор действия:'
    dict_action = {
        1: 'Вывести меню (возможные действия)',
        2: 'Краткое описание (ReadMe)',
        3: 'Показать все записи',
        4: 'Добавить новую запись',
        5: 'Изменить существующую запись',
        6: 'Удалить запись',
        7: 'Поиск (с возможностью экспорт данных в csv)',
        8: 'Экспорт данных в csv (всего справочника)',
        9: 'Импорт данных',
        0: 'Выход из программы'
        }
    list_action = list(dict_action.keys())
    return [dict_title, dict_action, list_action]


def dict_rows():
    """
    Содержит заголовки строк доступных для выбора из справочника
    Возвращает по ключу:
    0 - строка заголовок словаря
    1 - словарь
    2 - ключи словаря
    """
    rows_title = 'Список доступных полей:'
    dict_rows = {
        1: 'surname',
        2: 'name',
        3: 'phone',
        4: 'city',
        }
    list_rows = list(dict_rows.keys())
    return [rows_title, dict_rows, list_rows]


def print_dict_rotation(dictionary, type_rotation):
    """
    Выводит словарь на экран в виде списка (горизонтального или вертикального)
    входные параметры:
    dictionary - словарь
    type_rotation - тип отображения словаря (1 - по вертикали, 2 - по горизонтали)
    """
    if type_rotation == 1:
        for key, value in dictionary.items():
            print(key, '-', value, end='\n')
    elif type_rotation == 2:
        for key, value in dictionary.items():
            print(key, '-', value, end=' ; ')
    else:
        print('Error: Указан неправильный входной параметр - type_rotation')
