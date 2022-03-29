# удобной функцией для создания одномерных массивов является arange
# arange([start,] stop, [step,], dtype=None)
import numpy as np
# Создадим массив из пяти чисел от 0 до 4:
print(np.arange(5))
# [0 1 2 3 4]

# Создадим массив от 2.5 до 5
print(np.arange(2.5, 5))
# [2.5 3.5 4.5]

# Создадим массив от 2.5 до 5 с шагом 0.5
print(np.arange(2.5, 5, 0.5))
# [2.5 3.  3.5 4.  4.5]

# Создадим массив от 2.5 до 5 с шагом 0.5 и с типом float16
print(np.arange(2.5, 5, 0.5, dtype = np.float16))
# [2.5 3.  3.5 4.  4.5]
print(np.arange(1.4, 7, 3, dtype = np.float32))
# [1.4 4.4]