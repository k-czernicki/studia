

class Car:  # class definition
    def go(self):
        print('go go go')

# Car.go()  # err
car = Car()  # class INSATANCE
print(car)
car.go()
print()

car_1 = Car()
car_2 = Car()
car_3 = Car()
car_1.go()
car_2.go()
car_3.go()
print()

class Car:  # class definition
    INFO = 'at lease 4 wheels'

    def set_name(self, name):
        print(self)
        self.name = name

    @classmethod
    def print_info(cls):
        print(cls)
        print(cls.INFO)

print(dir(Car))
print()

car = Car()
print(dir(car))
print()

# print(car.name)  # err
car.set_name('kia')
print(dir(car))
print()

print(car.name)
print()

print(Car.INFO)
print(car.INFO)
print()

Car.print_info()
print()

car_name = getattr(car, 'name')
print(car_name)
print()

name_setter = getattr(car, 'set_name')
print(name_setter)
print()

class Car:
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        self.name = name

car = Car('foobar')
print(car.name)
car.set_name('kia')
print(car.name)
print()

class Car:
    def go(self):
        print('go go go')

    def __call__(self):
        print('= call =')
        self.go()

def car_go():
    print('go go go')

car = Car()
car()
car.go()
car_go()
print()

class Human:
    def __init__(self, age):
        self.age = age
    def __eq__(self, other):
        print(self, other)
        return self.age == other.age

john = Human(22)
print('john', john)
tom = Human(33)
print('tom', tom)
print(tom == john)
print(Human(23) == Human(23))
print()

class Human:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'== {self.name} =='
    def __repr__(self):
        return f'-- {self.name} --'

tom = Human('Tom')
print('print:', tom)
print('str  :', str(tom))
print('repr :', repr(tom))
# __grtattr__
# __getattribute__
# __setitem__  # instance[item] = x
# __getitem__  # instance[item]
# __len__      # len(x)
# __new__      # constructor
# __add__      # a + b
# __sub__      # a - b
print()

class Human:
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

tom = Human('Tom')
print(tom.get_name())
tom.set_name('TOM')
print(tom.get_name())
print()


class Car:
    def __init__(self, name):
        print('--init--')
        self.name = name

    def set_name(self, name):
        print('--setter--')
        self._name = name

    def get_name(self):
        print('--getter--')
        return self._name

    name = property(get_name, set_name)

kia = Car('kia')
print(kia.name)
kia.name = 'KIA'
print(kia.name)
print()

class Car:
    def __init__(self, name):
        print('--init--')
        self.name = name
    @property
    def name(self):
        print('--getter--')
        return self._name
    @name.setter
    def name(self, name):
        print('--setter--')
        self._name = name

kia_2 = Car('kia')
print(kia_2.name)
kia_2.name = 'KIA'
print(kia_2.name)
print()

class Vehicle:
    def go(self):
        print('go go go')

class Car(Vehicle):
    def stop(self):
        print('stop')
    # def go(self):
    #     print('go 1 go 1 go 1')

class Kia(Car): pass

kia = Kia()
kia.go()
kia.stop()
print()


class Human:
    def __init__(self, name):
        self.name = name

class Father(Human):
    def strenght(self):
        print('i an strong')

class Mother(Human):
    def __init__(self, name):
        self.name = 'mrs ' + name
    def beauty(self):
        print('i am a beauty')

class Son(Father, Mother):
    def beast(self):
        print(self.name)
        self.strenght()
        self.beauty()

#       Human
#       /   \
# Father     Mother
#       \   /
#        Son

pudzian = Son('mariusz')
pudzian.beast()
print(Son.__mro__)
print()

class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        # self.name = 'super=' + name
        super().__init__('SUPER=' + name)
        # Human.__init__(self, 'super-' + name)

tom = Man('Tom')
print(tom.name)
print()

class PenBody:
    def __init__(self, material):
        self.material = material

class PenCardridge:
    def __init__(self, ink_color):
        self.ink_color = ink_color

class PenClip:
    def __init__(self, material):
        self.material = material

class Pen:
    def __init__(self, material, clip_material, ink_color):
        self.body = PenBody(material)
        self.cardridge = PenCardridge(ink_color)
        self.clip = PenClip(clip_material)

bic_pen = Pen('plastic', 'gum', 'blue')
elegant_pen = Pen('aluminium', 'tytanium', 'black')
print(bic_pen.body.material,
      bic_pen.cardridge.ink_color,
      bic_pen.clip.material)
print(elegant_pen.body.material,
      elegant_pen.cardridge.ink_color,
      elegant_pen.clip.material)
print()

import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def eat(self):
        pass

# animal = Animal()  # not allowed

class Human(Animal):
    def eat(self):
        print('eating')

tom = Human()
tom.eat()
print()

#
