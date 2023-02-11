i = 1
silnia = 1

while True:
    x = int(input('Wpisz liczbe:'))
    if x > 0:
        break
    else:
        print('zla liczba, jeszcze raz')

while (i <= x):
    silnia = silnia * i
    i += 1
print(silnia)