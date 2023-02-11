def is_pass_strong(password):
    special_characters = '"!@#$%^&*()-+?_=,<>/"1234567890'
    if len(password) >= 10:
        print('haslo ma', len(password), 'znakow')
        if any(i in special_characters for i in password):
            print('znaleziono znak specjalny')
            if password != password.lower() and password != password.upper():
                print('duze i male litery sa ok')
                return True
            else:
                print('brak duzych albo malych znakow')
                return False
        else:
            print('nie znaleziono znaku specjalnego')
            return False
    else:
        print('haslo za krotkie ')
        return False


def zmiana_hasla(user):
    licznik = 0
    while True:
        password = input('Podaj haslo ')
        if user in hasla and password == hasla[user]:
            while True:
                licznik = 0
                new_password_1 = input('Podaj nowe haslo ')
                new_password_2 = input('Powtorz nowe haslo ')
                if new_password_1 == new_password_2 and is_pass_strong(new_password_1):
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
