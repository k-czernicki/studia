def zakres(pierwszy=0, ostatni=100, krok=1):
    liczba = pierwszy
    while liczba < ostatni:
        yield liczba
        liczba += krok


# yield pozwala sie dostac do petli w funkcji i do kazdej wartosci iteratora jaka chcemy zwrocic
# return zwraca jedynie wynik raz na koncu

zakres1 = zakres(1, 50)
# zakres2 = zakres(1,50)

for a in zakres1:
    print(a)

for b in zakres1:
    print(b)
