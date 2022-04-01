# random.choice()
# получить случайный набор объектов из массива
# choice(a, size=None, replace=True)
# a — массив или число для генерации arange(a);
# size — желаемая форма массива (число для получения одномерного массива, кортеж — для многомерного; если параметр не задан, возвращается один объект);
# replace — параметр, задающий, могут ли элементы повторяться (по умолчанию могут)
import numpy as np
# Выберем случайным образом из списка двоих человек, которые должны будут выступить с отчётом на этой неделе
workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
choice = np.random.choice(workers, size=2, replace=False)
print(choice)
# ['Ivan' 'Maria']
choice2 = np.random.choice(workers)
print(choice2)
# Kate # возвращается один объект по умолчанию

# получим случайную последовательность, которая образуется в результате десяти подбрасываний игральной кости
coin_choice = np.random.choice([1,2,3,4,5,6], size=10)
print(coin_choice)
# [4 4 5 1 5 1 5 1 5 2] 
# ошибка не возникает за счёт того, что объекты могут повторяться