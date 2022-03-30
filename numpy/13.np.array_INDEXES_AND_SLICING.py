# ИНДЕКСЫ И СРЕЗЫ В МАССИВАХ

# Создадим массив из шести чисел:
import numpy as np
arr = np.linspace(1, 2, 6)
print(arr)
# [1.  1.2 1.4 1.6 1.8 2. ]

# Обратиться к его элементу по индексу можно так же, как и к списку:
print(arr[2])
# 1.4

# для срезов работает и для одномерных массивов:
print(arr[1:3])
# [1.2 1.4]

# напечатать массив в обратном порядке можно с помощью привычной конструкции [::-1]:
print(arr[::-1])
# [2.  1.8 1.6 1.4 1.2 1. ]
print(arr.dtype)
# float64

# Создадим двумерный массив из 12 элементов из одномерного:
nd_arr = np.linspace(0, 6, 12, endpoint=False).reshape(3, 4)
print(nd_arr)
# [[0.  0.5 1.  1.5]
# [2.  2.5 3.  3.5]
# [4.  4.5 5.  5.5]]

# получить число из второй строки и третьего столбца массива
print(nd_arr[1][2])
# 3.0
print(nd_arr[1,2])
# 3.0

# получим все элементы из колонки 3 для первых двух строк:
print(nd_arr[:2,2])
# [1. 3.] получили одномерный массив в виде строки

# Можно применять срезы сразу и к строкам, и к столбцам
print(nd_arr[1:, 2:4])
# [[3.  3.5]
# [5.  5.5]]

# Чтобы получить все значения из какой-то оси, можно оставить на её месте двоеточие
print(nd_arr[:, 2:4])
# [[1.  1.5]
# [3.  3.5]
# [5.  5.5]]

# Чтобы получить самую последнюю ось, двоеточие писать необязательно
print(nd_arr[:2])
# [[0.  0.5 1.  1.5]
# [2.  2.5 3.  3.5]]

arr_2_new = np.arange(12)
arr_2_new.shape = (3, 4)
print(arr_2_new)
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

print(arr_2_new[2, 3])
# 11
print(arr_2_new[::-1])
# [[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]
print(arr_2_new[:2,2]) # получим все элементы из колонки 3 для первых двух строк:
# [2 6]
print(arr_2_new[1:, 2:4])
# [[ 6  7] срезы сразу и к строкам, и к столбцам
# [10 11]]
print(arr_2_new[1:, 2:]) # 1: номер строки, 2: два последних числа 
# [[ 6  7]
# [10 11]]

print(arr_2_new[:, 2: ])
# [[ 2  3] получить все значения из какой-то оси
#  [ 6  7]
# [10 11]]

print(arr_2_new[:2])
# [[0 1 2 3] получить самую последнюю ось
# [4 5 6 7]]