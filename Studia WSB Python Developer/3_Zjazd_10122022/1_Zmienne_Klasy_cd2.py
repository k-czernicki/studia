x = None
print(x is None)

####################################

koniec = object()

def abc():
    node = None
    if node is koniec:
        return

print(abc)

# ponizej rozne metody na przyrownanie do siebie obiektow / zmiennych
# a == b
# a.__eq__(b)