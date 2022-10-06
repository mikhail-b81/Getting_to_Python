import pb_reader as r
import pb_action as a
import pb_voc as v
import pb_exporter as e

print('-'*27)
print('-- Телефонный справочник --')
print('-'*27)
print(v.dict_action()[0])
v.print_dict_rotation(v.dict_action()[1], 1)


action = -1
while action != 0:
    action = int(input('\nВыберите действие: '))
    if action not in v.dict_action()[2]:
        print('Error: Нет такого действия!')
    elif action == 1:
        print('-' * 50)
        print(v.dict_action()[0])
        v.print_dict_rotation(v.dict_action()[1], 1)
    elif action == 2:
        with open("readme.txt", 'r', encoding='utf-8') as file:
            print(file.read())
    elif action == 3:
        print('-'*50)
        r.print_list_row(r.get_all_data())
    elif action == 4:
        print('-'*50)
        a.added_row()
    elif action == 5:
        print('-'*50)
        update_id = int(input('Укажите id записи которую хотите изменить: '))
        if update_id in r.get_allowed_id():
            v.print_dict_rotation(v.dict_rows()[1], 2)
            position = int(input('\nВыбирете поле которое надо изменить: '))
            value = input('Введите новое значение для выбранного поля: ')
            a.update_row(update_id, position, value)
        else:
            print('Error: Записи с указанным id нет в справочнике!')
    elif action == 6:
        print('-'*50)
        delete_id = int(input('Укажите id записи которую хотите удалить: '))
        if delete_id in r.get_allowed_id():
            a.delete_row(delete_id)
        else:
            print('Error: Записи с указанным id нет в справочнике!')
    elif action == 7:
        print('-'*50)
        v.print_dict_rotation(v.dict_rows()[1], 2)
        position = int(input('\nВыбирете поле по которому будет поиск: '))
        value = input('Введите искомое значение: ')
        search_data = a.search_value(r.get_all_data(), position, value)
        r.print_list_row(search_data[0])
        print(search_data[1])
        if input('Сохранить результат поиска в csv? (Y-да): ') in ['Y', 'y']:
            print('-' * 50)
            print('Данные сохранены в файле:', e.get_export_data(search_data[0]))
    elif action == 8:
        print('-'*50)
        print('Данные сохранены в файле:', e.get_export_data(r.get_all_data()))
    elif action == 9:
        print('-'*50)
        print('Пример названия импортируемого файла: import_file.csv')
        imp_title = input('Введите имя импортирунмого файла: ')
        print('В справочник были добавлены следующие записи:')
        r.print_list_row(e.get_import_data(imp_title))



