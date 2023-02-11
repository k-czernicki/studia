# Znajdź sumę oczek, która jest najbardziej prawdopodobna przy:
# Rzucie 2 kostkami
# Rzucie 3 kostkami
# do rozwiazania z 2 kostkami dodajemy wartosc do listy sukcesy sum i dodajemy wynik nr 3
# Rzucie 11 kostkami

import random

sukcesy_wyrzuconych_sum = [0] * 13

for nr_powtorzenia in range(1000):
    wynik_kostki_1 = random.randint(1, 6)
    wynik_kostki_2 = random.randint(1, 6)

    wyrzucona_suma = wynik_kostki_1 + wynik_kostki_2
    sukcesy_wyrzuconych_sum[wyrzucona_suma] += 1

maksymalny_indeks = 0
maksymalna_wartos = 0
for i in range(len(sukcesy_wyrzuconych_sum)):
    if sukcesy_wyrzuconych_sum[i] > maksymalna_wartos:
        maksymalna_wartos = sukcesy_wyrzuconych_sum[i]
        maksymalny_indeks = i

print('sukcesy_wyrzuconych_sum = ', sukcesy_wyrzuconych_sum)
print('Najbardziej prawdopodobna suma to: ', maksymalny_indeks, 'wyrzucono ja ', maksymalna_wartos)
