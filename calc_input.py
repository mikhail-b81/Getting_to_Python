import calc_checker as cc

def get_num():
    """
    Запрашивает у пользователя число.
    Проверяет введенные символы что бы они были числом (с помощью функции check_num() из модуля calc_checker)
    """
    number = input('введите число: ')
    cc.check_num(number)
    return float(number)



