import calc_input as ci
import calc_action as ca
import calc_put_log as cpl
import calc_checker as cc

# калькулятор
print('Введите число с которым надо сделать действие')
num = ci.get_num()

print('выберите действие:')
print(ca.print_action())

action = int(ci.get_num())
cc.check_action(action)


if action in (1, 2, 3):
    print('введите делитель: ')
    devision = ci.get_num()
    print(devision)
else:
    print('введите второе число: ')
    devision = ci.get_num()
    print(devision)
print('-'*30)

cc.check_zero_division(action, devision)

print("Результат: ", ca.get_action(num, action, devision))

cpl.write_log(num, action, devision)