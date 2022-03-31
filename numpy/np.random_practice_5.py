# np.random_Practice
import numpy as np
# Задайте seed равным 2021
np.random.seed(2021)
# В simple сохраните случайное число в диапазоне от 0 до 1
simple = np.random.rand()
print(simple)
# 0.6059782788074047

# Сгенерируйте 120 чисел в диапазоне от -150 до 2021, сохраните их
# в переменную randoms
randoms = np.random.uniform(-150,2021, size=120)
print(randoms)

# Получите массив из случайных целых чисел от 1 до 100 (включительно)
# из 3 строк и 2 столбцов. Сохраните результат в table
table = np.random.randint(1,101, size=(3,2))
print(table)
# [[46 93]
# [35 41]
# [17 45]]

# # В переменную even сохраните чётные числа от 2 до 16 (включительно)
even = np.arange(2,17,2)
print(even)
# [ 2  4  6  8 10 12 14 16]

#Перемешайте числа в even так, чтобы массив even изменился
np.random.shuffle(even)
print(even)
# [ 6 10  2  8 14 16  4 12]

# Получите из even 3 числа без повторений. Сохраните их в переменную select
select = np.random.choice(even, replace=False, size=3)
print(select)
# [ 4  6 10]

# Получите переменную triplet, которая должна содержать перемешанные
# значения из массива select (сам select измениться не должен)
triplet = np.random.permutation(select)
print(triplet)
# [ 6 10  4]