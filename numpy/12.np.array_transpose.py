# функция transpose()
# Эта операция меняет строки и столбцы массива местами
# транспонирование

import numpy as np
arr = np.arange(8)
arr.shape = (2, 4)
print(arr)
# [[0 1 2 3]
#  [4 5 6 7]]

arr_trans = arr.transpose()
print(arr_trans)
# [[0 4]
# [1 5]
# [2 6]
# [3 7]]

# При транспонировании одномерного массива его форма не меняется:
arr = np.arange(3)
print(arr.shape)
# (3,)
arr_trans = arr.transpose()
print(arr_trans.shape)
# (3,)

