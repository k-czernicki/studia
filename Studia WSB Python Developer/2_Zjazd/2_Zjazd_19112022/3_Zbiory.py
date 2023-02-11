zbior1 = {1, 2, 3, 4, 5, 6, 7, 8, 'tata', 'pies'}
zbior2 = {7, 8, 9, 0, 'mama', 'pies'}

print(zbior1.union(zbior2))
print(zbior1.intersection(zbior2))
print(zbior1.difference(zbior2))
print(zbior2.difference(zbior1))

x = list(zbior1.intersection(zbior2))
print(x)
