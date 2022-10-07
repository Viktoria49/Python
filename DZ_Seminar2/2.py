# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(input):

    f = 1
    for i in range(2, input + 1):
        f *= i
    return f

print([
    factorial(i) for i in range(1, int(input('N:')) + 1)
])
