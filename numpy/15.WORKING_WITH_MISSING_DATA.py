# РАБОТА С ПРОПУЩЕННЫМИ ДАННЫМИ

import numpy as np
data = np.array([4, 9, -4, 3])
# Воспользуемся встроенной в NumPy функцией sqrt
roots = np.sqrt(data)
print(roots)
# RuntimeWarning: invalid value encountered in sqrt roots = np.sqrt(data)
# [2.         3.                nan 1.73205081] 
# # nan = Not a number (не число
#  np.nan — это отдельный представитель класса float

# чтобы грамотно сравнить что-либо с None, необходимо использовать оператор is
print(None is None)
# True
print(np.nan is np.nan)
# True
print(np.nan is None)
# False

# Если попробовать посчитать сумму массива, который содержит np.nan, в итоге получится nan
print(sum(roots))
# nan

# Можно заполнить пропущенные значения, например, нулями
# с помощью функции np.isnan(<массив>) узнаем, на каких местах в массиве находятся «не числа»:
print(np.isnan(roots))
# [False False  True False]

# Можно использовать полученный массив из True и False для извлечения элементов из массива roots
print(roots[np.isnan(roots)])
# nan

# Этим элементам можно присвоить новые значения, например 0:
roots[np.isnan(roots)]=0
