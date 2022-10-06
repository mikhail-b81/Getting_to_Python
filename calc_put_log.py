import calc_action as ca
import datetime

def write_log(num, action, devision):
    """
    Запись успешного действия в журнал событий.
    """
    with open('calc_log.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{str(datetime.datetime.now())}')
        file.write(f'\nбыли выбраны следующие позиции: первое число: {num}, второе число: {devision}, операция: {action} ({ca.action_dict()[action]})')
        file.write(f'\nрезультат: {ca.get_action(num, action, devision)}')
        file.write('\n-------------------------------')


def write_log_error(error_type):
    """
    Запись успешного действия в журнал событий.
    """
    with open('calc_log.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{str(datetime.datetime.now())}')
        file.write(f'\nДействие вызвало ошибку')
        file.write(f'\n{error_type}')
        file.write('\n-------------------------------')


