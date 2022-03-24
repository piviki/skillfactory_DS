# counter in use
from collections import Counter
cars_list_moscow = ['blue', 'red', 'white', 'red', 'green', 'orange', 'purple', 'white', 'white']
cars_list_spb = ['white', 'white', 'blue', 'red', 'funny', 'purple']
# print(cars_list_moscow)
moscow_counter = Counter(cars_list_moscow)
spb_counter = Counter(cars_list_spb)
print('Moscow', moscow_counter)
print('SPb', spb_counter)
# Moscow Counter({'white': 3, 'red': 2, 'blue': 1, 'green': 1, 'orange': 1, 'purple': 1})
# SPb Counter({'white': 2, 'blue': 1, 'red': 1, 'funny': 1, 'purple': 1})

# another way
c = Counter()
b = Counter()
for car in cars_list_moscow:
    c[car] +=1
for car_num in cars_list_spb:
    b[car_num] +=1
print('Moscow', c)
print('SPb', b)
# Moscow Counter({'white': 3, 'red': 2, 'blue': 1, 'green': 1, 'orange': 1, 'purple': 1})
# SPb Counter({'white': 2, 'blue': 1, 'red': 1, 'funny': 1, 'purple': 1})

# elemets()
print('Moscow:', *moscow_counter.elements())
# Moscow: blue red red white white white green orange purple
print('SPb:', *spb_counter)
# SPb: white blue red funny purple

