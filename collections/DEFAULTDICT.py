# DEFAULTDICT
# for dict creation
students = [('Ivan', 1), ('Peter', 2), ('Ann', 3)]
groups = dict()
for student, group in students:
    if group not in groups:
        groups[group] = list() # обязательно создаем list
        groups[group].append(student)
print(groups)
  # {1: ['Ivan'], 2: ['Peter'], 3: ['Ann']}  

# with defaultdict
from collections import defaultdict
student_groups = defaultdict(list) # обязательно создаем list
for student, group in students:
    student_groups[group].append(student)
print(student_groups)
# defaultdict(<class 'list'>, {1: ['Ivan'], 2: ['Peter'], 3: ['Ann']})

print(student_groups[2])
# ['Peter']
print(student_groups.keys())
# dict_keys([1, 2, 3])
print(student_groups[4] == 'Fedor')
# False
