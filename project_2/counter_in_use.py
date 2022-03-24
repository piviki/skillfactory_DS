# Counter use

# Creat counters
from collections import Counter

moscow_list = ['red', 'white', 'white', 'green', 'black', 'purple']
spb_list = ['white', 'green','yellow', 'purple', 'white', 'green']
moscow_count = Counter(moscow_list)
spb_counter = Counter(spb_list)
print('Moscow counter', moscow_count)
print('Spb counter', spb_counter)