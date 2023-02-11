# Przyklad kogos z grupy gdzie polaczone sa punkty A i B

gross = float(input('jakie masz zarobki'))
kids = int(input('ile masz dzieci'))


# przyklad A
def rev_a(gross, kids):
    tax = 0.2
    kids_bonus = 500
    bonus = kids * kids_bonus
    return (1 - tax) * gross + bonus


# przyklad B
def rev_b(gross, kids):
    tax = 0
    kids_bonus = 0
    bonus = 0
    if gross > 5000:
        tax = 0.2
    elif gross < 3000:
        tax = 0.1
    if kids in (2, 3):
        bonus = kids * kids_bonus
    return (1 - tax) * gross + bonus


print('twoje zarobki wyniosa', rev_a(gross, kids), 'zl')

print('twoje zarobki wyniosa', rev_b(gross, kids), 'zl')

# Przyklad prowadzacego ponizej

# Przyklad A
liczba_dzieci = int(input('Podaj liczbe dzieci: '))
zarobki_brutto = float(input('Podaj zarobki brutto: '))
zarobki_netto = 0.8 * zarobki_brutto + 500 * liczba_dzieci
print('Twoje zarobki netto to: ', zarobki_netto, ' zł')

# Przyklad B
liczba_dzieci = int(input('Podaj liczbe dzieci: '))
zarobki_brutto = float(input('Podaj zarobki brutto: '))
if zarobki_brutto < 3000:
    zarobki_netto = zarobki_brutto
elif zarobki_brutto < 5000:
    zarobki_netto = zarobki_brutto * 0.9
else:
    zarobki_netto = zarobki_brutto * 0.8
if liczba_dzieci >= 2:
    zarobki_netto += 500
if liczba_dzieci >= 3:
    zarobki_netto += 500
print('Twoje zarobki netto to: ', zarobki_netto, ' zł')
