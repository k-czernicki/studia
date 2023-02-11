def pole_trojkata(podstawa, wysokosc):
    # pole = podstawa * wysokosc / 2
    return podstawa * wysokosc / 2


def pole_trojkata_2():
    a = float(input('podaj dlugosc podstawy'))
    h = float(input('podaj wysokosc'))
    print('pole trojkata to: ', a * h / 2)
    return a * h / 2


def czysc():
    print('czysc ram')
    print('czysc cache')
    return None


a = 5
b = 6
slowo = 'Tajfun'

print(pole_trojkata(a, len(slowo)))
czysc()
