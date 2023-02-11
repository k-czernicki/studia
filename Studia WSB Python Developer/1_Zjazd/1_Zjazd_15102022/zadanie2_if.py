liczba_metrow_kw = float(input('podaj liczbe metrow kw mieszkania: '))
wysokosc_mieszkania = float(input('podaj wysokosc mieszkania w metrach: '))

typ_mieszkania = input('Podaj z czego jest twoje mieszkanie (cegla/plyta): ')

mieszkanie = liczba_metrow_kw * wysokosc_mieszkania
if typ_mieszkania == 'cegla':
    print('Twoj koszt ogrzewania to ', f'{mieszkanie * 0.3:.2f}', 'zl dziennie')
elif typ_mieszkania == 'plyta':
    print('Twoj koszt ogrzewania to ', f'{mieszkanie * 0.5:.2f}', 'zl dziennie')
else:
    print('nie rozpoznano typu mieszkania ', typ_mieszkania)

# zaokraglenie do 2 msc po przecinku to : f'{cos:.2f}'
# prawy i refactor i robi to np takie cos jak 'mieszkanie' czyli generuje zmienna 2 innych zmiennych
