# Practice
# Получите сумму чисел, сохранённых в переменных a и b
import numpy as np
a = 6
b = 7
print(np.int64(a)+np.int64(b))
# 13

# Напишите функцию get_chess, которая принимает на вход длину стороны квадрата a и возвращает двумерный массив формы (a, a), заполненный 0 и 1 в шахматном порядке. В левом верхнем углу всегда должен быть ноль
# Remenber: для получения каждого второго элемента используется срез [::2]
def get_chess(a):
    arr = np.zerros((a,a))
    arr[1::2,::2]=1
    arr[::2,1::1]=1
    