# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = float(input('N: '))
while int(num) != num:
    num *= 10

result = 0
while num:
    result += num % 10
    num //= 10
print(result)