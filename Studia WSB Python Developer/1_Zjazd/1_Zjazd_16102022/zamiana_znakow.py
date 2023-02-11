tekst = 'ala ma kota! oraz psa. koniec'

nowy_tekst = ''
for ch in tekst:
    if ch == '!':
        ch = '.'
    print(ch, end='')
    nowy_tekst += ch
print()
print('oryginal ', tekst)
print()
print('zmieniony', nowy_tekst)
print('koniec programu')

# Kod prowadzacego

tekst = 'ala ma kota! oraz psa. the end'
# tekst[0] = 'A'
znaki_nowego_tesktu = []
for ch in tekst:
    if ch == '!':
        ch = '.'
    print(ch, end='')
    znaki_nowego_tesktu.append(ch)
print()
print('orginalny teskst ', tekst)
print('znaki_nowego_tesktu = ', znaki_nowego_tesktu)
nowy_tekst = ''.join(znaki_nowego_tesktu)
print('nowy_tekst ', nowy_tekst)
print()
print('koniec programu')

# jest tez funkcja replace

tekst = "!ala ma kota!"
nowy_tekst = tekst.replace("!", ".")
print(nowy_tekst)

