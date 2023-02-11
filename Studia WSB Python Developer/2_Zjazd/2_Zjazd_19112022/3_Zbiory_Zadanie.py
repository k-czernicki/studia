# załóżmy, że pesel ma 4 cyfry
# stwórzmy zbiór NFZ – ludzie, w bazie pacjentów NFZ
# stwórzmy zbiór chorzy_rok – ludzie chorzy w ostatnim roku
# stwórzmy zbiór chorzy_miesiac – ludzie chorzy w ostatnim miesiącu
# stwórzmy zbiór krzyki – wszystkich ludzi mieszkających na krzykach
# stwórzmy zbiór centrum – wszystkich ludzi mieszkających

NFZ = {1234, 3476, 4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243, 6435, 1298, 6732, 7688, 7648, 2345, 2356}
chorzy_rok = set([1234, 3476, 4544, 3423, 3254, 8769, 5436])
chorzy_miesiac = {1234, 3476, 3098, 4544, 3423}
krzyki = {4544, 3423, 3254, 8769, 5436, 2345, 6532, 1243}
centrum = {7648, 2345, 2356, 3987, 1234, 3476, 3254}
zbior_pusty = set()

# sprawdźmy, ile osób, które chorowały w ostatnim roku na krzykach
print('Chorzy w ostatnim roku na krzykach ',chorzy_rok.intersection(krzyki))
print('ilość: ',len(chorzy_rok.intersection(krzyki)))

# sprawdźmy ile osób z Krzyków chorowało w ostatnim roku
print('\nChorzy w ostatnim roku na krzykach ',krzyki.intersection(chorzy_rok))
print('Ilość ',len(krzyki.intersection(chorzy_rok)))

# sprawdźmy, ile osób chorowało w ostatnim miesiącu w centrum
print('\nChorzy w ostatnim miesiącu w centrum ',centrum.intersection(chorzy_miesiac))
print('Ilość ',len(centrum.intersection(chorzy_miesiac)))

# sprawdźmy, ile mieszka w sumie w centrum i na krzykach
print ('\nMIeszkańcy centrum i Krzyków ',centrum.union(krzyki))
print ('Ilość ',len(centrum.union(krzyki)))

# sprawdźmy poprawność danych:
print ('\nPoprawność danych')
# każdy, kto chorował w ostatnim miesiącu, jednocześnie chorował w ostatnim roku
if len(chorzy_miesiac.difference(chorzy_rok)) == 0:
    print ('ok')
else:
    print('problem: ',chorzy_miesiac.difference(chorzy_rok))

# nikt nie powinien mieszkać jendocześnie w centrum i na krzykach – jeśli tak, trzeba usunąć
print ('Osoby mieszkjaące jednocześnie w centrum i na krzykach ',krzyki.intersection(centrum))
print ('Ilość: ',len(krzyki.intersection(centrum)))
if len(krzyki.intersection(centrum)) != 0:
    x = input('Usuwam. Usunąć ludzi z Krzyków (K), czy z Centrum (C) ?   ')
    duplikaty = krzyki.intersection(centrum)
    if x == 'K':
        for i in krzyki.intersection(centrum):
            krzyki.remove(i)
    elif x == 'C':
        for i in duplikaty:
            centrum.remove(i)
        # centrum = centrum.difference(krzyki.intersection(centrum))
print ('Usunięte, sprawdzam: Liczba osób mieszkających jednocześnie w centrum i na krzykach ',len(krzyki.intersection(centrum)))
if len(krzyki.intersection(centrum)) == 0:
    print ('ok')
else:
    print ('Ups, nie udało się usunać')