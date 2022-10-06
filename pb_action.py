import csv
import datetime
import pb_reader as r


def get_row_id(id):
    """
    Возвращает row_id для активных строк.
    Входной параметр: id активной строки, для которой нужно найти ее row_id
    """
    with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
        fieldnames = ['row_id', 'id', 'surname', 'name', 'phone', 'city']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=";")
        with open('csv_phonebook_activity_id.csv', 'r', encoding='utf-8') as csvfile_meta:
            fieldnames_meta = ['row_id', 'changed']
            reader_meta = csv.DictReader(csvfile_meta, fieldnames=fieldnames_meta, delimiter=";")
            list_deleted = []
            for del_row in reader_meta:
                list_deleted.append(del_row['row_id'])
            list_deleted = list_deleted[1:]  # исключаем первый элемент списка ('row_id')
            for row in reader:
                if row['id'] == str(id) and row['row_id'] not in list_deleted:
                    return (row['row_id'])


def delete_row(delete_id):
    """
    Помечаем строку на удаление
    Запись row_id удаленной строки в файл csv_phonebook_activity_id.csv
    """
    # delete_id = input('Введите id строки которую надо удалить: ')
    deleted_row_id = get_row_id(delete_id)
    # print(deleted_row_id)
    with open('csv_phonebook_activity_id.csv', 'a', encoding='utf-8', newline='') as csvfile:
        # fieldnames = ['id', 'surname', 'name', 'phone', 'city']
        csv_writer = csv.writer(csvfile, delimiter=';')
        csv_writer.writerow([deleted_row_id, datetime.datetime.now(), 'deleted'])


def update_row(update_id, position, value):
    """
    Обновление данных в строке
    Добавляет новую версию строки (с новым row_id)
    Помечает старую версию строки как удаленную
    Запись row_id удаленной строки в файл csv_phonebook_activity_id.csv
    """
    with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
        fieldnames = ['row_id', 'id', 'surname', 'name', 'phone', 'city']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter = ";")
        for row in reader:
            if row['id'] == str(update_id):
                surname = row['surname']
                name = row['name']
                phone = row['phone']
                city = row['city']
                if position == 1:
                    surname = value
                elif position == 2:
                    name = value
                elif position == 3:
                    phone = value
                elif position == 4:
                    city = value
                with open('csv_phonebook.csv', 'a', encoding='utf-8', newline='') as csvfile_a:
                    csv_writer = csv.writer(csvfile_a, delimiter=';')
                    csv_writer.writerow([int(r.get_last_row_id())+1, update_id, surname, name, phone, city])
                break

    with open('csv_phonebook_activity_id.csv', 'a', encoding='utf-8', newline='') as csvfile_up:
        csv_writer = csv.writer(csvfile_up, delimiter=';')
        csv_writer.writerow([get_row_id(update_id), datetime.datetime.now(), 'update'])


def added_row():
        """
        Запись новых данных в справочник (csv_phonebook.csv)
        """
        row_id = int(r.get_last_row_id())
        id = int(r.get_last_id())
        surname = input('Введите фамилию (поле surname): ')
        name = input('Введите имя (поле name): ')
        phone = input('Введите телефон (поле phone): ')
        city = input('Введите город (поле city): ')
        with open('csv_phonebook.csv', 'a', encoding='utf-8', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=';')
            csv_writer.writerow([row_id+1, id+1, surname, name, phone, city])


# def search_value(position, value):
#     """
#     Поиск данных по условию
#     position - поле по которому будем искать
#     value - значение которое нужно найти
#     """
#     with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
#         fieldnames = ['row_id', 'id', 'surname', 'name', 'phone', 'city']
#         reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=";")
#         with open('csv_phonebook_activity_id.csv', 'r', encoding='utf-8') as csvfile_meta:
#             fieldnames_meta = ['row_id', 'changed']
#             reader_meta = csv.DictReader(csvfile_meta, fieldnames=fieldnames_meta, delimiter=";")
#             list_deleted = []
#             for del_row in reader_meta:
#                 list_deleted.append(del_row['row_id'])
#             list_deleted = list_deleted[1:]  # исключаем первый элемент списка ('row_id')
#             count_row = 0
#             for row in reader:
#                 if row['row_id'] not in list_deleted:
#                     if int(position) == 1 and row['surname'] == value:
#                         print(row['id'], row['surname'], row['name'], row['phone'], row['city'])
#                         count_row += 1
#                     elif int(position) == 2 and row['name'] == value:
#                         print(row['id'], row['surname'], row['name'], row['phone'], row['city'])
#                         count_row += 1
#                     elif int(position) == 3 and row['phone'] == value:
#                         print(row['id'], row['surname'], row['name'], row['phone'], row['city'])
#                         count_row += 1
#                     elif int(position) == 4 and row['city'] == value:
#                         print(row['id'], row['surname'], row['name'], row['phone'], row['city'])
#                         count_row += 1
#             if count_row == 0:
#                 print('Записей удавлетворяющих условию поиска не найдено')
#             else:
#                 print(f'Найдено {count_row} записей')


# def search_value_n(position, value):
#     """
#     Поиск данных по условию
#     position - поле по которому будем искать
#     value - значение которое нужно найти
#     """
#     with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
#         fieldnames = ['row_id', 'id', 'surname', 'name', 'phone', 'city']
#         reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=";")
#         with open('csv_phonebook_activity_id.csv', 'r', encoding='utf-8') as csvfile_meta:
#             fieldnames_meta = ['row_id', 'changed']
#             reader_meta = csv.DictReader(csvfile_meta, fieldnames=fieldnames_meta, delimiter=";")
#             list_deleted = []
#             listn = []
#             for del_row in reader_meta:
#                 list_deleted.append(del_row['row_id'])
#             list_deleted = list_deleted[1:]  # исключаем первый элемент списка ('row_id')
#             count_row = 0
#             for row in reader:
#                 if row['row_id'] not in list_deleted:
#                     if int(position) == 1 and row['surname'] == value:
#                         listn.append([row['id'], row['surname'], row['name'], row['phone'], row['city']])
#                         count_row += 1
#                     elif int(position) == 2 and row['name'] == value:
#                         listn.append([row['id'], row['surname'], row['name'], row['phone'], row['city']])
#                         count_row += 1
#                     elif int(position) == 3 and row['phone'] == value:
#                         listn.append([row['id'], row['surname'], row['name'], row['phone'], row['city']])
#                         count_row += 1
#                     elif int(position) == 4 and row['city'] == value:
#                         listn.append([row['id'], row['surname'], row['name'], row['phone'], row['city']])
#                         count_row += 1
#             if count_row == 0:
#                 info_str = 'Записей удавлетворяющих условию поиска не найдено'
#             else:
#                 info_str = f'Найдено {count_row} записей'
#
#     return [listn, info_str]


def search_value(list, position, value):
    """
    Поиск данных по условию
    position - поле по которому будем искать
    value - значение которое нужно найти
    """
    listn = [['id', 'surname', 'name', 'phone', 'city']]
    count_row = 0
    for row in list:
        if int(position) == 1 and row[1] == value:
            listn.append(row)
            count_row += 1
        if int(position) == 2 and row[2] == value:
            listn.append(row)
            count_row += 1
        if int(position) == 3 and row[3] == value:
            listn.append(row)
            count_row += 1
        if int(position) == 4 and row[4] == value:
            listn.append(row)
            count_row += 1

    if count_row == 0:
        info_str = 'Записей удавлетворяющих условию поиска не найдено'
    else:
        info_str = f'Найдено {count_row} записей'

    return [listn, info_str]


# def search_value_nnn(list, position, value):
#     """
#     Поиск данных по условию
#     position - поле по которому будем искать
#     value - значение которое нужно найти
#     """
#     listn = []
#     count_row = 0
#     for q in list:
#         for row in q:
#             if int(position) == 1 and row[1] == value:
#                 listn.append(row)
#                 count_row += 1
#             if int(position) == 2 and row[2] == value:
#                 listn.append(row)
#                 count_row += 1
#             if int(position) == 3 and row[3] == value:
#                 listn.append(row)
#                 count_row += 1
#             if int(position) == 4 and row[4] == value:
#                 listn.append(row)
#                 count_row += 1
#
#     if count_row == 0:
#         info_str = 'Записей удавлетворяющих условию поиска не найдено'
#     else:
#         info_str = f'Найдено {count_row} записей'
#
#     return [listn, info_str]
