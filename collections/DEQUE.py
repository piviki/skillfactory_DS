# DEQUE
# доступ к возможностям и стека, и очереди
from collections import deque
dq = deque()
print(dq)
deque([])

# append()
clients = deque()
clients.append('Vasya')
clients.append('Dima')
clients.append('Nobody')
clients.append('Somebody')
print(clients)
# deque(['Vasya', 'Dima', 'Nobody', 'Somebody'])
print(clients[3])
# Somebody

# pop() and popleft()
client_1 = clients.popleft()
client_2 = clients.popleft()
print(clients)
# deque(['Nobody', 'Somebody'])

clients.appendleft('VIP')
clients.pop()
print(clients)
# deque(['VIP', 'Nobody'])

# функции extend (добавить в конец дека) и extendleft (добавить в начало дека)
shop = deque([1, 2, 3, 4, 5])
shop.extend([6, 7, 8, 9])
print(shop)
# deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

shop.extendleft([10, 11, 12])
print(shop)
# deque([12, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9])

shop.appendleft([10, 11, 12])
print(shop)
# deque([[10, 11, 12], 12, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9])

shop.pop()
print(shop)
# eque([[10, 11, 12], 12, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8])
shop.popleft()
print(shop)
# deque([12, 11, 10, 1, 2, 3, 4, 5, 6, 7, 8])

# maxlen
# ОЧЕРЕДЬ С ОГРАНИЧЕННОЙ МАКСИМАЛЬНОЙ ДЛИНОЙ
limited = deque(maxlen=3)
print(limited)
# deque([], maxlen=3)

limited.extend([1, 2, 3])
print(limited)
# deque([1, 2, 3], maxlen=3)

print(limited.append(8))
# None
print(limited.append([8]))
# None

limited_list = deque([1, 2, 3, 4, 5, 6, 7, 8], maxlen=3)
print(limited_list)
# deque([6, 7, 8], maxlen=3)
# сохраняются только последние элементы, а первые исчезают из памяти

# reverse позволяет поменять порядок элементов в очереди на обратный:
dq = deque([1, 2, 3, 4])
print(dq)
dq.reverse()
print('with reverse', dq)
# deque([1, 2, 3, 4])
# with reverse deque([4, 3, 2, 1])

# rotate перенос заданных элементов из конца очереди в начало:
dq.rotate(3)
print('with rotate 3', dq)
# with rotate 3 deque([3, 2, 1, 4])

dq.rotate(-2)
print(dq)
# deque([1, 4, 3, 2])

dq.rotate(-1)
print(dq)

# Функция index 
dq_2 = deque([1,2,4,2,3,1,5,4,4,4,4,4,3])
print('first index is:', dq_2.index(4))
# 2
print('amount of number 4 is:', dq_2.count(4))
# 6

# Функция count
print(dq_2.count(4))
# 6
print(dq_2.count(25))
# 0