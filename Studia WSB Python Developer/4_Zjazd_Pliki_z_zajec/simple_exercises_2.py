#
# write function 'adder' taking x
# returning lambda function taking y returning x+y
#
# write class 'Adder' taking x in __init__
# having call method taking y returning x+y
#
# witch method is best for witch situations discuss
#
def adder(x):
    return lambda y: x+y

class Adder:
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x + y

add_1 = adder(1)
ADD_1 = Adder(1)
print(add_1(1), ADD_1(2))
print()


# write abstract class LivingSomething
#    that has abstract method make_noise
import abc

class LivingSomething(abc.ABC):
    @abc.abstractmethod
    def make_noise(self):
        pass

# create Dog, Bacteria and Human classes inheriting
# from LivingSomething implementing abstract make_noise

class Dog(LivingSomething):
    def make_noise(self):
        print('woof')

class Bacteria(LivingSomething):
    def make_noise(self):
        print('zzzzzzz')

class Human(LivingSomething):
    def make_noise(self):
        print('scream')

# create Car class storing any number of LivingSomething-s
# instaces in passangers instance variable

# write call looping through all passangers calling make_noise
# on each on them

class Car:
    def __init__(self, *livig_somethings):
        print(livig_somethings)
        self.passangers = livig_somethings
    def __call__(self):
        for passanger in self.passangers:
            passanger.make_noise()

dog = Dog()
old_car = Car(dog, Human(), Human(), Bacteria())
old_car()
print()


# write animal class with make_noise and eat method

class Animal:
    def make_noise(self):
        print('adhkajfkashjk')
    def eat(self):
        print('eating adskfas')

# write Dog class that stores name and age in __init__
# has method eat_and_sleep printing
#     'dog {name} eats then sleeps'
# write property for dogs name

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_and_sleep(self):
        print(f'dog {self.name} eats and sleaps')
        Animal.eat(self)
        self.eat()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

dog = Dog('burak', 2)
dog.eat_and_sleep()


# store 2 words in variables
# write function 'combine' returning one word that combines them both
w1 = 'foozx'
w2 = 'barx'
w3 = 'xyz'

def combine(*words):
    big_word = ''
    for word in words:
        big_word = big_word + word
    return big_word


# write function factory counter taking single character and string
# returning count  of single character appearing in string

def couter_factory(character):
    # def counter(word):
    #     # count = 0
    #     # for c in word:
    #     #     if c == character:
    #     #         count = count + 1
    #     # return count
    #     return word.count(character)
    # return counter
    return lambda word: word.count(character)

# write function taking function and its imput
# that returns result of passed function called with input

def runner(fun, *args, **kargs):
    res = fun(*args, **kargs)
    return res

res = runner(couter_factory('x'), combine(w1, w2, w3))
print(res)  #2
print(list(runner(range, 1, 10)))
#
