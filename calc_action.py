
def action_dict():
    """
    Содержит словарь с действиями возможными в калькуляторе
    """
    act_dict = {1: 'деление нацело', 2: 'остаток от деления', 3: 'деление', 4: 'сложение', 5: 'вычитание', 6: 'умножение'}
    return act_dict


def get_action(num, action, devision):
    """
    Производит действия с указанными цифрами в зависимости от выбранного действия
    """
    if action == 1:
        return num // devision
    if action == 2:
        return num % devision
    if action == 3:
        return num / devision
    if action == 4:
        return num + devision
    if action == 5:
        return num - devision
    if action == 6:
        return num * devision


def print_action():
    """
    Выводит словарь с возможными действиями ввиде строки
    """
    for key, value in action_dict().items():
        print(key, '-', value, end=' ; ')





