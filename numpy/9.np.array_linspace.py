# для работы с дробными параметрами
# linspace () от англ. linear space — линейное пространство
# возвращает одномерный массив из чисел
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
import numpy as np
# Создадим массив из десяти чисел между 1 и 2
arr = np.linspace(1, 2, 10)
print(arr)
# [1.         1.11111111 1.22222222 1.33333333 1.44444444 1.55555556, 1.66666667 1.77777778 1.88888889 2.        ]

# Создадим массив из десяти чисел между 1 и 2, не включая 2
arr_1 = np.linspace(1,2,10, endpoint=False)
print(arr_1)
# [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9]

# Узнаем, какой шаг был использован для создания массива из десяти чисел между 1 и 2, где 2 включалось и не включалось
arr_step = np.linspace(1, 2, 10, endpoint=True, retstep=True)
print(arr_step)
# 0.1111111111111111
arr_step_2 = np.linspace(1, 2, 10, endpoint=False, retstep=True)
print(arr_step_2)
# 0.1