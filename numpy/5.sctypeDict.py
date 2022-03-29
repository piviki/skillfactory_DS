# sctypeDict = словарь типов данных в NumPy 
# в этом словаре содержится более 100 ключей
import numpy as np
print(np.sctypeDict)
print(len(np.sctypeDict))

# Получить список названий уникальных типов
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')