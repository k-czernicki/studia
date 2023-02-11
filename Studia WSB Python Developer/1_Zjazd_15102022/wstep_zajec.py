print('Pierwszy program')

a = 5
b = 7
napis = 'Python'
print(a)
print(a + b)
print('suma a i b wynosi ', a + b, ' a ty lubisz jezyk', napis)

imie = input('Podaj imie ')
print('Witaj', imie)

a = 5  # int - liczba calkowita
b = 5.5  # float - liczba zmiennoprzecinkowa
c = 'mama'  # string - napis
d = ['mama', 'kot', 5, 5.5]  # list - lista elementow

print('Zmienna a jest typu ', type(a))  # wypisanie typu zmiennej 'a'
print('Zmienna b jest typu ', type(b))
print('Zmienna c jest typu ', type(c))
print('Zmienna d jest typu ', type(d))

print('Pierwszy element listy to ', d[0])

print(d[2])  # pokazanie n-tego elementu listy d ale liczy od 0

print(d[1][2])  # wyciaganie litery z napisu

print(len(d[1]))  # pokazanie jaka jest dlugosc tekstu

wiek = int(input('ile masz lat'))
# dodanie int przed lub innego typu klasy konwetruje nam ta dana na okreslona klase.
# A w tym wypadku nie przejdzie jak wpiszemy text
# poczekanie na wartosc
print(type(wiek))

# command + /  to robienie komentarza w wielu liniach

if wiek > 18:  # sprawdzenie warunku
    # jesli rowne to == a nie =
    print('jestes pelnoletni')
    print('Gratulacje')
elif wiek == 18:  # sprawdzenie drugiego warunku
    print('masz dostep ale uwazaj na tresci')
else:  # akcja, gdy warunki nie zostaly spelnione
    print('koniec programu, nie masz dostepu')
print('dalsze instrukcje?')
# jak print jest poza to wykona zawsze. jak wpiszemy ponizej 18 to na luzie da tylko koniec programu

# and - dodwanie kolejnego warunku
# or - jak nie ten warunek to inny

plec = input('wpisz plec K/M')

if plec == 'K' or plec == 'k':
    print('Szanowna Pani')
elif plec == 'M' or plec == 'm':
    print('Szanowny Panie')
else:
    print('zly wybor')
