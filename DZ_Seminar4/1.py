# Вычислить число c заданной точностью d
#  Пример:
#
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

import math
from math import pi
d = input('Введите число d с заданной точностью: \n').count('0')
print(f'Число π с заданной точностью {d} = {round(pi,d)}')
