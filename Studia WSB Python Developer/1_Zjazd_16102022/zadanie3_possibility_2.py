import random

sukces_przy_rzucie_1_koscia = 0
sukces_przy_rzucie_3_kosciami = 0

for nr_powtorzenia_testu in range(1000):
    pierwsza_kostka = random.randint(1, 6)
    kostki = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    if pierwsza_kostka >= 4:
        sukces_przy_rzucie_1_koscia += 1
        # print('sukces przy rzucie 1 kostka')

    if 6 in kostki:
        sukces_przy_rzucie_3_kosciami += 1
        # print('sukces przy rzucaniu wieloma kostkami')

if sukces_przy_rzucie_1_koscia > sukces_przy_rzucie_3_kosciami:
    print('jest wiecej sukcesow przy rzucie 1 koscia')
elif sukces_przy_rzucie_1_koscia == sukces_przy_rzucie_3_kosciami:
    print('prawdopodobienstwo jest takie same')
else:
    print('jest wiecej sukcesow przy rzucie 3 koscia')
    # jak else to nie musi byc ten caly warunek sukces_przy_rzucie_1_koscia < sukces_przy_rzucie_3_kosciami

print('sukces_przy_rzucie_1_koscia =', sukces_przy_rzucie_1_koscia)
print('sukces_przy_rzucie_3_kosciami =', sukces_przy_rzucie_3_kosciami)
