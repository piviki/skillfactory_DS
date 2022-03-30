import numpy as np
mistory = np.linspace(0, 6, 12, endpoint=False)
print(mistory)
# [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5]

mistory_new = mistory.reshape((4, 3))
print(mistory_new)
# [[0.  0.5 1. ]
# [1.5 2.  2.5]
# [3.  3.5 4. ]
# [4.5 5.  5.5]]

# В переменную elem сохраните элемент из 2 строки и 2 столбца
elem = mistory_new[2, 2]
print(elem)
# 4.0

# В переменную last сохраните элемент из последней строки последнего столбца
last = mistory_new[-1,-1]
print(last)
# 5.5

# # В переменную line_4 сохраните строку 3
line_4 = mistory_new[3]
print(line_4)
# [4.5 5.  5.5]

# В переменную col_2 сохраните последний столбец
col_2 = mistory_new[:,-1]
print(col_2)
# [1.  2.5 4.  5.5]

# Из строк 1-3 (включительно) получите столбцы 1-2 (включительно)
# Результат сохраните в переменную part
part = mistory_new[1:,1:]
print(part)
# [[2.  2.5]
# [3.5 4. ]
# [5.  5.5]]

#  Сохраните в переменную rev последний столбец в обратном порядке
rev = mistory_new[::-1,-1] 
print(rev)
# [5.5 4.  2.5 1. ] # сначала reverse, а затем последний столбец

# Сохраните в переменную trans транспонированный массив
trans = mistory_new.transpose()
print(trans)
# [[0.  1.5 3.  4.5]
# [0.5 2.  3.5 5. ]
# [1.  2.5 4.  5.5]]