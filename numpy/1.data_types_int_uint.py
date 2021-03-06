# data types
# 8 bit
print('8 bit min = -2**8/2:', -2**8/2)
print('8 bit max = 2**8/2-1:', 2**8/2-1)
# 8 bit min = -2**8/2: -128.0
# 8 bit max = 2**8/2-1: 127.0

# 16 bit
print('16 bit min = -2**16/2:', -2**16/2)
print('16 bit max = 2**16/2-1:', 2**16/2-1)
# 16 bit min = -2**16/2: -32768.0
# 16 bit max = 2**16/2-1: 32767.0

# 32 bit
print('32 bit min = -2**32/2:', -2**32/2)
print('32 bit max = 2**32/2-1:', 2**32/2-1)
# 32 bit min = -2**32/2: -2147483648.0
# 32 bit max = 2**32/2-1: 2147483647.0

# 64 bit
print('64 bit min = -2**64/2:', -2**64/2)
print('64 bit max = 2**64/2-1:', 2**64/2-1)
# 64 bit min = -2**64/2: -9.223372036854776e+18
# 64 bit max = 2**64/2-1: 9.223372036854776e+18

# int8, int16, int32 & int64
# сколько битов памяти должно быть выделено для хранения переменной

# Преобразуем обычное целое число в NumPy-тип, например в int8
import numpy as np
a = np.int8(25)
print(a)
# 25
print(type(a))
# <class 'numpy.int8'>

# узнать границы int, можно воспользоваться функцией np.iinfo (int info):
print(np.iinfo(np.int8))
# min = -128, max = 127
print(np.iinfo(a))
# min = -128, max = 127

# uint (unsigned int — беззнаковое целое
b = np.uint8(124)
print(b)
#124
print(type(b))
# <class 'numpy.uint8'>
print(np.iinfo(b))
# min = 0, max = 255

# преобразовать переменные 
a = np.int32(2147483610)
b = np.int32(2147483605)
print(a, b)
# 2147483610 2147483605
print(np.int64(a) + np.int64(b))
# 4294967215
