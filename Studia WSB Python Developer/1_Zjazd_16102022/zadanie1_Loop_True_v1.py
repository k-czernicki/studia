# z gory ustalona liczba jaka jest 50

liczba_do_zagadniecia = 50

while True:
    liczba_podana = int(input('Zgadnij jaka to liczba: '))
    if liczba_podana == liczba_do_zagadniecia:
        print('Zgadles! To bylo: ', liczba_do_zagadniecia)
        break

    if liczba_podana > liczba_do_zagadniecia:
        print('podana przez ciebie liczba jest za duza')
    elif liczba_podana < liczba_do_zagadniecia:
        print('podana przez ciebie liczba jest za mala')
print('koniec programu')

# break sie liczy pod jakim warunkiem zostanie wykonany
