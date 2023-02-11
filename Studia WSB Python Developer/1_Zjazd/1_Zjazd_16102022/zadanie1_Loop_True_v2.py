# zgadnij liczbe ale liczba jest losowa za azdym razem z przedzialu 1-100

import random
liczba_do_zgadniecia = random.randint(1, 100)

while True:
    liczba_podana = int(input('Zgadnij jaka to liczba: '))
    if liczba_podana == liczba_do_zgadniecia:
        print('Zgadles! To bylo: ', liczba_do_zgadniecia)
        break

    if liczba_podana > liczba_do_zgadniecia:
        print('podana przez ciebie liczba jest za duza')
    elif liczba_podana < liczba_do_zgadniecia:
        print('podana przez ciebie liczba jest za mala')
print('koniec programu')