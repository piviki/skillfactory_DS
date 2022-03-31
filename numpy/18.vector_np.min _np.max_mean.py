# Статистика
# np.min и np.max 
# позволяют находить максимальное и минимальное значение в векторе
import numpy as np
vec = np.array([2,7,18,28,18,1,8,4])
print('min=', vec.min())
# min= 1
print('max=', np.max(vec))
# max= 28

# mean()
# позволяет посчитать среднее значение
print('mean=', vec.mean())
# mean= 10.75
print('mean=', np.mean(vec))
# mean= 10.75


# np.ptp() - value range
# Возвращает диапазон значений ([max - min]) массива или указанной оси массива.
print('диапазон значений [min-max]:', vec.ptp())
# диапазон значений [min-max]: 27

# np.median()
# Найдите медиану массива
#print('median:', np.median(vec)))


# average()
print('average:', np.average(vec))
# average: 10.75

# std()
# Найдите стандартное отклонение значений в массиве
print('стандартное отклонение:', np.std(vec))
# стандартное отклонение: 8.954747344286158

# histogram()
# Вычисление гистограммы набора данных.
print('histogram:', np.histogram(vec))
# histogram: (array([2, 1, 2, 0, 0, 0, 2, 0, 0, 1], dtype=int64), 
# array([ 1. ,  3.7,  6.4,  9.1, 11.8, 14.5, 17.2, 19.9, 22.6, 25.3, 28. ]))
