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

# counts summation
print('summation', moscow_counter+spb_counter)
# Counter({'white': 5, 'red': 3, 'blue': 2, 'purple': 2, 'green': 1, 'orange': 1, 'funny': 1})

# counts subtract
print('subtract', moscow_counter.subtract(spb_counter))


# elemets()
print('Moscow:', *moscow_counter.elements())
# Moscow: blue red red white white white green orange purple
print('SPb:', *spb_counter.elements())
# SPb: white white blue red funny purple

# to create a list use list() function
print('Moscow', list(moscow_counter))
# Moscow ['blue', 'red', 'white', 'green', 'orange', 'purple']

# dict
print(dict(spb_counter))
# {'white': 2, 'blue': 1, 'red': 1, 'funny': 1, 'purple': 1}

# most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:
print('most common', moscow_counter.most_common())
# most common [('red', 1), ('white', 1), ('green', 1), ('orange', 1), ('blue', 0), ('purple', 0), ('funny', -1)]

# # можно передать значение, которое задаёт желаемое число первых наиболее частых элементов, например, 2
print('two most common', moscow_counter.most_common(2))
# two most common [('red', 1), ('white', 1)]

# len(list())) список уникальных номеров
clients_List = [953421196, 953421161, 953421142, 953421186, 953421181, 953421144,
                953421196, 953421161, 953421142, 953421186, 953421181, 953421144,
                953421196, 953421161, 953421142, 953421186, 953421181, 953421144]
c = Counter(clients_List)
print(len(list(c)))
# 6
print('clients_List', c)
# clients_List Counter({953421196: 3, 953421161: 3, 953421142: 3, 953421186: 3, 953421181: 3, 953421144: 3})
print('client 953421144 is', c[953421144])
# client 953421144 3
print('most commom:', c.most_common())
# most commom: [(953421196, 3), (953421161, 3), (953421142, 3), (953421186, 3), (953421181, 3), (953421144, 3)]
print('most commom 2:', c.most_common(2))
#  most commom: [(953421196, 3), (953421161, 3)]