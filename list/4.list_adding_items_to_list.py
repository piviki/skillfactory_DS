# adding items to a list
#append()
bikes = []
bikes.append('trek')
bikes.append('redline')
bikes.append('giant')
print(bikes)
# ['trek', 'redline', 'giant']

squares = list()
for x in range(1,11):
    squares.append(x**2)
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# or = list comprehensions 
squares = [x**2 for x in range(1,11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]