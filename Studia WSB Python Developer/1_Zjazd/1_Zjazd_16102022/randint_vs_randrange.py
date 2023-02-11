import random

# losowanie liczby z zakresu i zwraca tez gorny zakres
for i in range(5):
    print('randint: ', random.randint(1, 5))
print()

# losowanie liczby z zakresu i nie zwraca gornego zakresu
# mozna dodac step czyli np 2 i bedzie dawac liczby co 2 np 1, 3, 5
# print('randrange', random.randrange(1, 5, 2))
for i in range(5):
    print('randrange', random.randrange(1, 5))
