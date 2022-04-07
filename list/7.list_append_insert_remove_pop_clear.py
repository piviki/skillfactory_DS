# добавление и удаление элементов
# добавляем в конец списка
# append()
users = ['Tom', 'Bob']
users.append('Alice')
print(users)
# ['Tom', 'Bob', 'Alice']

# добавляем на вторую позицию
users.insert(1, 'Bill')
print(users)
# ['Tom', 'Bill', 'Bob', 'Alice']

# получаем индекс элемента
i = users.index('Tom')
print(i)
# 0

# удаляем по этому индексу
removed_item = users.pop(i)
print(removed_item)
# Tom
print(users)
# ['Bill', 'Bob', 'Alice']

# удаляем последний элемент
last_user = users[-1]
users.remove(last_user)
print(users)
# ['Bill', 'Bob']

# удалим все элементы
users.clear()