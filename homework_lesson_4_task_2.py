
# 2
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.


num = int(input('Задайте натуральное число: '))

print(num)

mlist = []
divider = 2                         # Первый делитель = 2
while num > 1:
    if num % divider == 0:
        mlist.append(divider)
        num //= divider
    else:
        divider += 1                # Если число перестало делится на делитель то переходим к следующему делителю

print(mlist)