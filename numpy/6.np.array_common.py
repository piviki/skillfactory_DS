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
print(arr.dtype)
# int8

# Если добавить float в массив int, пропадёт десятичная часть
arr[2] = 125.5
print(arr)
#[  1   2 125]

# Строку, которую можно преобразовать в число, можно сразу положить в массив.
arr[1] = '12'
print(arr)
# [  1  12 125]

# Поменять тип данных во всём массиве  = np.int32 или np.float128
arr = np.float16(arr)
print(arr)
# [  1.  12. 125.]

# СВОЙСТВА NUMPY-МАССИВОВ
# размерность массива можно с помощью .ndim
print(arr.ndim)
# 1
print(nd_arr.ndim)
# 2

# Узнать общее число элементов в массиве можно с помощью .size
print(arr.size)
# 1
print(nd_arr.size)
# 9

# Форма или структура массива хранится в атрибуте .shape
print(arr.shape)
# (3,)
print(nd_arr.shape)
# (3, 3)

# узнать, сколько «весит» каждый элемент массива в байтах позволяет .itemsize
print(arr.itemsize)
# 2 в виде int16 (16 бит => 2 байта)

print(nd_arr.itemsize)
# 4 в виде int32 (32 бит => 4 байта)
