# 5. Реализуйте алгоритм перемешивания списка.

import random
n = int(input("Введите число: "))
list1 = list(range(0, n))
print(list1)
list2 = list()
for i in range(0, n):
    rand_idx = random.randrange(len(list1))
    list2.append(list1[rand_idx])
    list1.remove(list2[i])
print(list2)
