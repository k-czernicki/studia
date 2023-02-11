list = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']
username = input('Podaj nazwe uzytkownika: ')

czy_znaleziono = False
for i in range(len(list)):
    # lub moze byc
    # for u in "lista":
    # if u == "zmienna":
    if username == list[i]:
        print('znaleziono uzytkownika ', username, ' na pozycji', i, ' w liscie')
        czy_znaleziono = True

if czy_znaleziono == False:
    print('Nie ma takiego uzytkownika')
if czy_znaleziono == True:
    print('znaleziono dopasowanie')

# wytlumaczenie roznych sposobow przez prowadzacego

# uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']
# uzytkownik = 'marek'

# # wersja prosta:
# for i in range(len(uzytkownicy)):
#     if uzytkownik == uzytkownicy[i]:
#         print('Znalezino uzytkownika ', uzytkownik, ' na pozycji ', i, ' w liscie')
# # wersja skrótowa bez indeksu
# for u in uzytkownicy:
#     if uzytkownik == u:
#         print('znaleziono ', u)
# # wersja skrótowa z indeksem
# for i, u in enumerate(uzytkownicy):
#     if uzytkownik == u:
#         print('Znalezino uzytkownika ', uzytkownik, ' na pozycji ', i, ' w liscie')
