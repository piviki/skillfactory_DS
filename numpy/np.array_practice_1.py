# Practice
import numpy as np
nd_arr = np.array([
               [12, 45, 78],
               [34, 56, 13],
               [12, 98, 76]
               ], dtype=np.int16)

# Узнайте размерность массива
print(nd_arr.ndim)
# 2

# Какова максимальная протяжённость по одной из осей массива?
print(nd_arr.shape)
# (3, 3)

# Узнайте число элементов массива.
print(nd_arr.size)
# 9

# Какой тип данных у элементов массива?
print(nd_arr.dtype)
# int16

# Узнайте вес всех элементов в массиве в байтах
print(nd_arr.itemsize*nd_arr.size)
# 18