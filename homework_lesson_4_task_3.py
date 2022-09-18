# 3
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


numlist = [1,2,2,3,4,1,5,3,6,7,8,8]

# var_1 from set
# print(numlist)
# print(list(set(numlist)))

# var_2 from loop
uniclist = []
for i in numlist:
    if i not in uniclist:
        uniclist.append(i)

print(numlist)
print(uniclist)