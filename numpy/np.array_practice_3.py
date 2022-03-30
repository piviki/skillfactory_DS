import numpy as np
mystery = np.array([12279.0, -26024.0, 28745.0, np.nan, 31244.0, -2365.0, -6974.0, -9212.0, np.nan, -17722.0, 16132.0, 25933.0, np.nan, -16431.0, 29810.0])
# Получите булевый массив с информацией о np.nan в массиве mystery
# True - значение пропущено, False - значение не пропущено
nans_index = np.isnan(mystery)
print(nans_index)
# [False False False  True False False False False  True False False False True False False]

# В переменную n_nan сохраните число пропущенных значений
n_nan = sum(nans_index)
print(n_nan)
# 3

# Заполните пропущенные значения в массиве mystery нулями
mystery[nans_index] = 0
#mystery[np.isnan(mystery)]=0
print(mystery)
# [ 12279. -26024.  28745.      0.  31244.  -2365.  -6974.  -9212.      0. -17722.  16132.  25933.      0. -16431.  29810.]

# Поменяйте тип данных в массиве mystery на int32
mystery = np.int32(mystery)
print(mystery.dtype)
# int32

# Отсортируйте значения в массиве по возрастанию и сохраните
# результат в переменную array
array = np.sort(mystery)
print(array)
# [-26024 -17722 -16431  -9212  -6974  -2365      0      0      0  12279 16132  25933  28745  29810  31244]

# Сохраните в массив table двухмерный массив, полученный из массива array
# В нём должно быть 5 строк и 3 столбца. Причём порядок заполнения должен быть
table = array.reshape((5,3), order='F')
print(table)
# [[-26024  -2365  16132]
# [-17722      0  25933]
# [-16431      0  28745]
# [ -9212      0  29810]
# [ -6974  12279  31244]]

#  Сохраните в переменную col столбец 2
col = table[:,1]
print(col)
# [-2365     0     0     0 12279]