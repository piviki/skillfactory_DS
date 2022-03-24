# Counter ()
# for counting

# Creating empty Counter
from collections import Counter
c = Counter()
c['red'] +=1
print('Adding red car to Counter', c)
# Adding red car to Counter Counter({'red': 1})

# Creating a list of cars
from collections import Counter
cars = ['red', 'red', 'black', 'white', 'green', 'yellow', 'white']
c = Counter()
for car in cars:
    c[car] +=1
print('Making dict for the car list', c)
# Making dict for the car list Counter({'red': 2, 'white': 2, 'black': 1, 'green': 1, 'yellow': 1})

# use Counter() only
c = Counter(cars)
print(c)
# Counter({'red': 2, 'white': 2, 'black': 1, 'green': 1, 'yellow': 1})
