while True:
    x = int(input('Wprowadz Liczbe>0: '))
    if x > 1:
        break

l = 0
while (x != 1):
    if x % 2 == 0:
        x = x / 2
        l += 1
        print(x)
    else:
        x = 3 * x + 1
        l += 1
        print(x)
print('Program wykonal sie ', l, 'razy')
