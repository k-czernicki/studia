lista = [1, 5, 3, 24, 15, 6, 8, 12, 31]
# // - to dzielenie
# % - pozostalosc inaczej reszta

for i in range(len(lista)):
    if lista[i] % 2 == 0 or i > 10:
        print('wykonanie petli nr ', i, ' wartosc listy = ', lista[i])

# if lista[i] % 2 == 0 or lista[i] > 10:
# to tez rozwiazanie zamiast linii 6, wtedy wyswietla wiecej danych
