kolory_napojow = {'kawa': 'biala', 'herbata' : 'zielona', 'cola' : 'czarna'}

print(kolory_napojow.keys())   #zwraca klucze w slowniku
print(kolory_napojow.values())   #zwraca wartosci w slowniku
print(kolory_napojow.items())    #zwraca klucz i wartosc
print('KLucz' in kolory_napojow)   #zwraca prawde jesli klucz wystepuje w slowniku
print('kawa' in kolory_napojow)

print(kolory_napojow['kawa'])
kolory_napojow['kefir'] = 'bialy'
print(kolory_napojow.items())
kolory_napojow['kefir'] = 'zieLony'
print(kolory_napojow.items())