# range()
# создать последовательный список чисел
## range(end) - from 0 to end
## range(start, end) - from start to end(end is not included)
### range(start, end, step) - from start to end with step
numbers = list(range(10))
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# взятия среза/ slicing a list
print(numbers[:2]) # [0, 1]
print(numbers[2:4]) # [2, 3]
print(numbers[:4:2]) # [0, 2]
num = numbers
print(num[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(num.reverse())