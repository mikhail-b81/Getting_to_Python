import sys
import calc_action as ca
import calc_put_log as cpl

def check_zero_division(action, devision):
    """
    Проверка деления на ноль
    Запись об ошибке заносится в журнал событий (функция write_log_error из модуля calc_put_log)
    В результате ошибки программа прерывается
    """
    if devision == 0 and action in (1, 2, 3):
        error_type = 'Error: Деление на ноль!'
        cpl.write_log_error(error_type)
        print(error_type)
        sys.exit()


def check_num(num):
    """
    Проверка что ввели число, допускается запись числа через символ '.'
    Например ввод числа: .2 соответствует 0.2 или 2. соответствует 2.0
    Запись об ошибке заносится в журнал событий (функция write_log_error из модуля calc_put_log)
    В результате ошибки программа прерывается
    """
    nums = ['0','1','2','3','4','5','6','7','8','9','.']
    for i in num:
        if i not in nums or num == '.':
            error_type = 'Error: Не число!'
            cpl.write_log_error(error_type)
            print(error_type)
            sys.exit()


def check_action(action):
    """
    Проверка что выбранное действие есть в калькуляторе
    Запись об ошибке заносится в журнал событий (функция write_log_error из модуля calc_put_log)
    В результате ошибки программа прерывается
    """
    if int(action) not in list(ca.action_dict().keys()):
        error_type = 'Error: В калькуляторе нет такого действия!'
        cpl.write_log_error(error_type)
        print(error_type)
        sys.exit()


