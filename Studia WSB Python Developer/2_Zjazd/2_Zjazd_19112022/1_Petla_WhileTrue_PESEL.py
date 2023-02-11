suma = 0

while True:
    pesel = int(input('Podaj PESEL '))
    if str(pesel) == 'abc':
        print('SPERUSER')
        break
    elif len(str(pesel)) == 4:
        pesel_str = str(pesel)
        suma = int(pesel_str[0]) + int(pesel_str[1]) + int(pesel_str[2]) + int(pesel_str[3])

        print(suma)
        if suma % 3 == 0 or suma % 4 == 0:
            print('PESEL poprawny')
            break
        else:
            print('Suma kontrolna się nie zgadza')
    else:
        print('PESEL powinien mieć 4 cyfry, jeszcze raz')

print('Dalsza czesc programu')
