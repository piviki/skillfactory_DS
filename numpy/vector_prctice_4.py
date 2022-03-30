# Задача на Длину вектора
# параллельны друг другу, называются сонаправленными
# сумма длин сонаправленных векторов должна быть равной длине суммы двух векторов
# С помощью этого критерия найдите пару сонаправленных векторов
import numpy as np
a = np.array([23, 34, 27])
b = np.array([-54, 1,  46])
c = np.array([46, 68, 54])
# 1) find vectors len
len_a = np.linalg.norm(a)
len_b = np.linalg.norm(b)
len_c = np.linalg.norm(c)
print(len_a, len_b, len_c)
# 49.13247398615299 70.94363960215179 98.26494797230598
len_a_b = np.linalg.norm(a+b)
len_b_c = np.linalg.norm(b+c)
len_a_c = np.linalg.norm(a+c)
print(len_a_b, len_b_c, len_a_c)
# 86.68909966079934 121.75795661885921 147.39742195845895
print(len_a_b == len_a+len_b)
# False
print(len_b_c == len_b+len_c)
# False
print(len_a_c == len_a+len_c)
# True
# a and c сонаправленные векторы

# Задача на расстояние векторов