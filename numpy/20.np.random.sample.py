# sample()
# функция, генерирующая массивы случайных чисел от 0 до 1, 
# которая принимает в качестве аргумента именно кортеж без распаковки
import numpy as np
shape = (2, 3)
print(np.random.sample(shape))
# [[0.42585981 0.67437237 0.26057282]
# [0.35495304 0.48319046 0.6820975 ]]