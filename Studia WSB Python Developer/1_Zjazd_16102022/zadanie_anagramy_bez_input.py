slowo = 'kajak'

print('dlugosc podanego slowa to ', len(slowo))

for i in range(len(slowo)):

    # print('na pozycji ', i, 'znajduje sie litera ', slowo[i], 'a po przeciwnej ', slowo[len(slowo) - 1 - i])

    # if slowo[i] == slowo[len(slowo) - 1 - i]:
    #     print('slowo wyglada na anagram')
    # else:
    #     print('slowo nie wyglada na anagram')

    if slowo[i] != slowo[len(slowo) - 1 - i]:
        print('to na pewno nie anagram')
        break
# ewentualnie zamiast else: if i == len(slowo) - 1:
else:
    print('to slowo:', slowo, 'jest anagramem')
