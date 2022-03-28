# ТИПЫ ДАННЫХ С ПЛАВАЮЩЕЙ ТОЧКОЙ
# float16, float32, float64, float128 (no for float8)
# узнать границы float = np.finfo(np.float16)
import numpy as np
print(np.finfo(np.float16))
print(np.finfo(np.float32))
print(np.finfo(np.float64))

# Resolution (от англ. «разрешение»)
# Для float16 это 0.001
# Третий знак числа float16 идёт уже с шагом 0.005
print(np.float16(4.12))
# 4.12
print(np.float16(4.13))
# 4.13
print(np.float16(4.123))
# 4.12
print(np.float16(4.124))
# 4.125
print(np.float16(4.125))
# 4.125


