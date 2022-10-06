import csv
import datetime
import pb_reader as r


def get_export_data(exp_data):
    """
    Экспорт данных в csv-файл
    Название файла: csv_phonebook + время создания файла
    """
    title = 'csv_phonebook_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S") + '.csv'

    with open(title, 'w', encoding='utf-8', newline='') as csvfile_exp:
        csv_writer = csv.writer(csvfile_exp, delimiter=';')
        for row in exp_data:
            csv_writer.writerow(row)

    return title


def get_import_data(imp_title):
    """
    Импорт данных из csv-файл
    В файле должна быть шапка - surname, name, phone, city
    Разделитель - ;
    """
    with open(imp_title, 'r', encoding='utf-8') as csvfile:
        fieldnames = ['surname', 'name', 'phone', 'city']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter=";")
        list_imp = []
        for row in reader:
            list_imp.append([row['surname'], row['name'], row['phone'], row['city']])

        with open('csv_phonebook.csv', 'a', encoding='utf-8', newline='') as csvfile_a:
            csv_writer = csv.writer(csvfile_a, delimiter=';')
            row_id = int(r.get_last_row_id())
            id = int(r.get_last_id())
            for row in list_imp[1:]:
                row_id += 1
                id += 1
                csv_writer.writerow([row_id, id, row[0], row[1], row[2], row[3]])

    return list_imp

