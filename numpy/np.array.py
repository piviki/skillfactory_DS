# array = массив
# СОЗДАНИЕ МАССИВА ИЗ СПИСКА
import numpy as np
arr = np.array([1, 2, 3, 5, 8])
print(arr)
# [1 2 3 5 8] - одномерный массив
print(type(arr))
# <class 'numpy.ndarray'>
# Название ndarray — это сокращение от n-dimensional array, -мерный массив

# двумерный массив из списка списков
# таблица чисел или матрица
nd_arr = np.array([
               [12, 45, 78],
               [34, 56, 13],
               [12, 98, 76]
               ])
print(nd_arr)
# array([[12, 45, 78],
#        [34, 56, 13],
#        [12, 98, 76]])

# ТИПЫ ДАННЫХ В МАССИВЕ
# dtype
print(arr.dtype)
# int32
# сразу при создании массива задать тип данных 
arr = np.array([1, 2, 3], dtype = np.int8)
print(type(arr))
