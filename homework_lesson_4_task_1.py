
# 1
# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# *Сохранить словарь в файл users_hobby.txt.
#
# Фрагмент файла с данными о пользователях (users.txt): Иванов Иван Иванович Петров Петр Петрович
# Фрагмент файла с данными о хобби (hobby.txt): скалолазание, охота горные лыжи

# Читаем файл
def readfile(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        flist = f.readlines()
    return flist

# Определяем количество записей в файле
def lenfile(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        flist = f.readlines()
        count = len(flist)
    return count

# Определяем наименьшее количество записей (если в файлах разное количество записей)
def count_row(file_name_1, file_name_2):
    if file_name_1 > file_name_2:
        return file_name_2
    elif file_name_1 < file_name_2:
        return file_name_1
    elif file_name_1 == file_name_2:
        return file_name_1


n = count_row(lenfile('users.txt'), lenfile('hobby.txt'))
listuser = readfile('users.txt')
listhobby = readfile('hobby.txt')
newdict = {}
for i in range(n):
    newdict[listuser[i].replace('\n', '')] = listhobby[i]

with open('users_hobby.txt', 'w', encoding='utf-8') as file:
    for key, value in newdict.items():
        file.write(f'{key}: {value}')

