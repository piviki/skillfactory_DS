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