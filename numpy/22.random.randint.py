# random.randint()
# Для генерации целых чисел 
# randint(low, high=None, size=None, dtype=int)
# Функцию randint нельзя запустить совсем без параметров, необходимо указать хотя бы одно число
import numpy as np
# Сгенерируем таблицу 2x3 от 0 до 3 включительно
print(np.random.randint(4, size=(2,3)))
# [[0 1 1]
# [1 2 0]]

# Чтобы задать и нижнюю, и верхнюю границы самостоятельно, передадим два числа
print(np.random.randint(6,12, size=(3,3)))
# [[9 7 9]
# [9 9 8]
# [8 7 8]]

