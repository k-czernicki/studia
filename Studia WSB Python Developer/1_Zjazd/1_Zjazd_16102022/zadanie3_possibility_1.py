import random

lista_kostek = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
print(lista_kostek)

if 1 in lista_kostek:
    print('jedna z kostek wyrzucika 1')
else:
    print('zadna z kostek nie wyrzucila 1')