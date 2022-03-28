# str
import numpy as np
a = 'Hello world'
print(type(a))

a = np.str(a)
print(type(a))
# <class 'str'>
a = np.str_(a)
print(type(a))
# <class 'numpy.str_'>