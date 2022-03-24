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
sorted_ages = OrderedDict(sorted(data_list, kyes()))
print(sorted_ages)