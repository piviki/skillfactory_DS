# to keep in order
data_list = [('Cate', 17), ('OLga', 20), ('Peter', 18)]
ages = dict(data_list)
print(ages)
# {'Cate': 17, 'OLga': 20, 'Peter': 18}

from collections import OrderedDict
ages_2 = OrderedDict(data_list)
print(ages_2)
# OrderedDict([('Cate', 17), ('OLga', 20), ('Peter', 18)])

# sorted()
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
sorted_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
print(sorted_ages)
# OrderedDict([('Ivan', 19), ('Maria', 20), ('Andrey', 23), ('Mark', 25)])

sorted_ages_2 = OrderedDict(sorted(data_list, key=lambda x: x[1]))
print(sorted_ages_2)
# OrderedDict([('Cate', 17), ('Peter', 18), ('OLga', 20)])

sorted_ages_3 = sorted(data_list, key=lambda x: x[1])
print(sorted_ages_3)
# [('Cate', 17), ('Peter', 18), ('OLga', 20)]

sorted_ages_4 = sorted(data_list)
print(sorted_ages_4) # no sorting - need lambda
# [('Cate', 17), ('OLga', 20), ('Peter', 18)] 