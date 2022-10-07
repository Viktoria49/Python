# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n 
# и выведите на экран их сумму.
# Пример:


n = int(input("Введите число: "))
if n <= 0:
    print ("Введено недопустимое значение, повторите попытку")
else:
    lis = list()
    sum = 0
    for i in range(1, n+1):
        f = round((1 + 1/i) ** i)
        lis.append(f)
        sum = sum + f
    print(f"n = {n}: {lis} -> {sum}")