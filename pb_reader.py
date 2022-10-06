import csv


def get_last_row_id():
    """
    Возвращает последний row_id из csv-файла
    """
    with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        list_id = []
        for row in reader:
            list_id.append(row['row_id'])

    return list_id[-1]


def get_last_id():
    """
    Возвращает последний id из csv-файла
    """
    with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        list_id = []
        for row in reader:
            list_id.append(int(row['id']))

    return sorted(list_id)[-1]



def get_allowed_id():
    """
    Возвращает список активных id в справочнике
    """
    with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
        fieldnames = ['row_id', 'id', 'surname', 'name', 'phone', 'city']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter = ";")
        with open('csv_phonebook_activity_id.csv', 'r', encoding='utf-8') as csvfile_meta:
            fieldnames_meta = ['row_id', 'changed']
            reader_meta = csv.DictReader(csvfile_meta, fieldnames=fieldnames_meta, delimiter=";")
            list_deleted = []
            for del_row in reader_meta:
                list_deleted.append(del_row['row_id'])
            list_deleted = list_deleted[1:] # исключаем первый элемент списка ('row_id')
            listn = []
            for row in reader:
                if row['row_id'] not in list_deleted:
                    listn.append(row['id'])
            list_result = list(map(int, listn[1:]))

    return list_result


# print(get_allowed_id())

# def get_all_data():
#     """
#     Возвращает все записи из справочника (не удаленные)
#     """
#     with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
#         fieldnames = ['row_id', 'id', 'surname', 'name', 'phone', 'city']
#         reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter = ";")
#         with open('csv_phonebook_activity_id.csv', 'r', encoding='utf-8') as csvfile_meta:
#             fieldnames_meta = ['row_id', 'changed']
#             reader_meta = csv.DictReader(csvfile_meta, fieldnames=fieldnames_meta, delimiter=";")
#             list_deleted = []
#             for del_row in reader_meta:
#                 list_deleted.append(del_row['row_id'])
#             list_deleted = list_deleted[1:] # исключаем первый элемент списка ('row_id')
#             for row in reader:
#                 if row['row_id'] not in list_deleted:
#                     print(row['id'], row['surname'], row['name'], row['phone'], row['city'])

# get_all_data()




# with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=";")
#     list_id = []
#     for row in reader:
#         list_id.append(int(row['id']))

# new_list = []
# print(list_id)
# new_list = sorted(list_id)
# # print(new_list)
# print(sorted(list_id)[-1])




def get_all_data():
    """
    Возвращает все записи из справочника (не удаленные) в виде списка
    """
    with open('csv_phonebook.csv', 'r', encoding='utf-8') as csvfile:
        fieldnames = ['row_id', 'id', 'surname', 'name', 'phone', 'city']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter = ";")
        with open('csv_phonebook_activity_id.csv', 'r', encoding='utf-8') as csvfile_meta:
            fieldnames_meta = ['row_id', 'changed']
            reader_meta = csv.DictReader(csvfile_meta, fieldnames=fieldnames_meta, delimiter=";")
            list_deleted = []
            for del_row in reader_meta:
                list_deleted.append(del_row['row_id'])
            list_deleted = list_deleted[1:] # исключаем первый элемент списка ('row_id')
            listn = []
            for row in reader:
                if row['row_id'] not in list_deleted:
                    listn.append([row['id'], row['surname'], row['name'], row['phone'], row['city']])

    return listn


def print_list_row(list):
    """
    Выводит полученные записи на экран
    """
    for row in list:
        print(*row)





