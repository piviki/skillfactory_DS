# bool_
# записывать их необходимо именно с нижним подчёркиванием
import numpy as np
a = True
print(type(a))
a = np.bool(a)
print(type(a))
a = np.bool_(a)
print(type(a))
# <class 'bool'>
# <class 'numpy.bool_'>

# comparing
print(np.bool(True) == np.bool_(True))
# True
print(type(np.bool(True)) == type(np.bool_(True)))
# False