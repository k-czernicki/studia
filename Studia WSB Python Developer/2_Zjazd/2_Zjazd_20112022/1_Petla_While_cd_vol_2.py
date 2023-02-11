def can_be_int(x):
    try:
        y = int(x)
        return True
    except ValueError:
        return False


def can_be_float(x):
    try:
        y = float(x)
        return True
    except ValueError:
        return False


while True:
    x = input('Wprowadz liczbe > 1: ')
    if can_be_int(x) and int(x) > 1:
        x = int(x)
        break

l = 0
while (x != 1 and l < 50):
    if x % 2 == 0:
        x = int(x / 2)
        l += 1
        print(x)
    else:
        x = 3 * x + 1
        l += 1
        print(x)
print('Program wykonal sie ', l, 'razy')
