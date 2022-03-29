# ЗАПОЛНЕНИЕ НОВЫХ МАССИВОВ
import numpy as np
# Можно заранее подготовить массив заданной размерности, заполненный нулями, а потом загружать в него реальные данные по мере необходимости
# np.zeros
zerros_1d = np.zeros(5)
print(zerros_1d)
# [0. 0. 0. 0. 0.]

# Создадим трёхмерный массив с формой 2x4x3 и типом float32
zerros_3d = np.zeros((2,3,4), dtype = np.int32)
print(zerros_3d) # две матрицы, 3 строки, 4 стобца
# [[[0 0 0 0]
# [0 0 0 0]
# [0 0 0 0]]

# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]
print(zerros_3d.shape)
# (2, 3, 4)
print(zerros_1d.dtype)
# float64
print(zerros_3d.dtype)
# int32
print(zerros_3d.shape)
# (2, 3, 4)

