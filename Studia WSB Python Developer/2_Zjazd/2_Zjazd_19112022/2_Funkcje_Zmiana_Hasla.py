def zmiana_hasla(user):
    licznik = 0
    while True:
        password = input('Podaj haslo ')
        if user in hasla and password == hasla[user]:
            while True:
                licznik = 0
                new_password_1 = input('Podaj nowe haslo ')
                new_password_2 = input('Powtorz nowe haslo ')
                if new_password_1 == new_password_2:
                    hasla[user] = new_password_1
                    print('Haslo zostalo zmienione')
                    break
                else:
                    licznik += 1
                    if licznik < 3:
                        print('żle wpisane nowe haslo, jeszcze raz')
                    else:
                        print('blad')
                        break
        else:
            licznik += 1
            if licznik < 3:
                print('zle dane, wpisz haslo jeszcze raz')
            else:
                print('brak uzytkownika bądź haslo niepoprawne')
                break
        break
    return None

hasla = {'Justyna': '1234', 'Tajfun': '2345', 'superadmin': 'abc'}

x = input('Czy chcesz zmienic haslo? T/N ')
if x.lower() == 't':
    uzytkownik = input('podaj nazwe uzytkownika ')
    zmiana_hasla(uzytkownik)
print(hasla)
print('dalsza czesc programu')
