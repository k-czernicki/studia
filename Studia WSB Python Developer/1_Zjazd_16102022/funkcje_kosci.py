import random

def rzuc_kostka():
    return random.randint(1, 6)

def sytuacja1_czy_jest_sukces():
    # nie wiadomo ile wypadło, wiadomo że jest to conajmniej 4
    wynik_rzutu = rzuc_kostka()
    if wynik_rzutu >= 4:
        return True
    else:
        return False
    
for i in range(10):
    print('wynik sytuacji1 ', sytuacja1_czy_jest_sukces())