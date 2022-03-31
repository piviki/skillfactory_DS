# np.random.seed()
# np.random.seed(<np.uint32>). 
# Число в скобках должно быть в пределах от 0 до 2**32 - 1 (=4294967295)
# необходимо получать одинаковые воспроизводимые последовательности случайных чисел
# на предмет ошибок
import numpy as np
np.random.seed(23)
print(np.random.randint(10, size=(3,4)))
# [[3 6 8 9]
# [6 8 7 9]
# [3 6 1 2]]
# при разных запусках, увидите тот же самый набор чисел!

np.random.seed(100)
print(np.random.randint(10, size=3))
# [8 8 3]
print(np.random.randint(10, size=3))
# [7 7 0]
print(np.random.randint(10, size=3))
# [4 2 5]
