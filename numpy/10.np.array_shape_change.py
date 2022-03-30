# ИЗМЕНЕНИЕ ФОРМЫ МАССИВА
# атрибут shape

import numpy as np
arr = np.arange(8)
print(arr)
# [0 1 2 3 4 5 6 7]

# Поменять форму массива arr можно с помощью присвоения атрибуту shape кортежа с желаемой формой:
arr.shape = (2, 4)
print(arr)
# [[0 1 2 3] 
# [4 5 6 7]]

print(arr.dtype)
print(arr.size)
print(arr.ndim)