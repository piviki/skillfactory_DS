# СОРТИРОВКА ОДНОМЕРНЫХ МАССИВОВ

# Способ 1. Функция np.sort(<массив>) возвращает новый отсортированный массив:
import numpy as np
arr = np.array([23,12,45,12,23,4,15,3])
arr_new = np.sort(arr)
print(arr_new)
# [ 3  4 12 12 15 23 23 45]
print(arr_new.dtype)

# Способ 2. Функция <массив>.sort() сортирует исходный массив и возвращает None:
print(arr.sort())
# None
print(arr)
# [ 3  4 12 12 15 23 23 45]