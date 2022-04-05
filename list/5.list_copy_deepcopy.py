# copying a list
bikes =  ['trek', 'redline', 'giant']
bikes_copy = bikes[:]
print(bikes_copy)
# ['trek', 'redline', 'giant']

# deepcopy()
import copy
users1 = ['Tom', 'Bob', 'Alice']
users2 = copy.deepcopy(users1)
users2.append('Sam')
print(users1)
# ['Tom', 'Bob', 'Alice']
print(users2)
# ['Tom', 'Bob', 'Alice', 'Sam']