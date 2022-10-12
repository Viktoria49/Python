# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.20


import random
n = int(input('Введите количество элементов списка: '))
list = []
for i in range(n):
    list.append(round(random.uniform(0, 10), 2))

min = list[0]-int(list[0])
max = list[0]-int(list[0])
for item in list:
    if item-int(item) <= min:
        min = item-int(item)
    if item-int(item) >= max:
        max = item-int(item)
res = round(max-min, 2)
print(f'В списке {list}, макс и мин дробная часть {max} и {min}, их разница {res}')
