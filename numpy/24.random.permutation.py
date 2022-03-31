# random.permutation()
# получить новый перемешанный массив, а исходный оставить без изменений
# принимает на вход один аргумент — или массив целиком, или одно число

import numpy as np
playlist = ["The Beatles", "Pink Floyd", "ACDC", "Deep Purple"]
mixed_playlist = np.random.permutation(playlist)
print('mixed_playlist', mixed_playlist)
print('original playlist', playlist)
# mixed_playlist ['Deep Purple' 'The Beatles' 'Pink Floyd' 'ACDC']
# original playlist ['The Beatles', 'Pink Floyd', 'ACDC', 'Deep Purple']
# передали в качестве аргумента список, а не массив, и ошибки не возникло
# список playlist при этом остался без изменений

print(np.random.permutation(10))
# [0 4 9 3 7 5 8 2 1 6]
# С помощью permutation можно избежать действия с arange()