
def print_name():
    print('Filip')

print_name()

print()

def return_name():
    return 'Filip'

print(return_name())

print()

def greet(name):
    print('hello ' + name)

greet('Filip')

print()

def return_multiple():
    return [1, 2, 3], 4  # ([1,2,3], 4)

print(return_multiple())
print()

def party():
    print('before')
    return
    print('after')

print(party())
print()
print(party)
print()
o = object()
print(o)
print()

def name_nick(name, nick, other):
    print(name + ' ' + nick + ' ' + other)

name_nick('Filip', 'coding', 'now')
print()


def add_nums(
    x=111,
    y=333,
    z=666
):
    print(x + y + z)

add_nums(1,2)
add_nums(1,2,3)
add_nums()
print()

def print_args(*args):
    print(args)

print_args(1,2,3,4,5)
print_args([1,2], 3, 4, 2, 4, 5, 5)
print()

def positional_and_wildcard(x, y, *rest, z='hello'):
    print(x, y, rest, z)

positional_and_wildcard([1,2], 3, 4, 2, 4, 5, 5, z=12)
positional_and_wildcard([1,2], 3, 4, 2, 4, 5, 5,)
print()

def interesting(x, y, z):
    print(x, y, z)

interesting(1, 2, 3)
interesting(1, 2, z=3)
interesting(1, y=2, z=3)
interesting(x=1, y=2, z=3)
interesting(y=1, z=2, x=3)
interesting(z=1, y=2, x=3)
print()

def kword(*, x=11, y=22, z=33):
    print(x, y, z)

kword(x=11, y=22, z=33)
kword(z=11, y=22, x=33)
kword(z=11, x=33)
kword(z=11)
print()

def return_name():
    return 'Filip'

def wild_kargs(**kargs):
    print(kargs)

wild_kargs(z=3, d=5, asd='asd')
wild_kargs(z=3, d=5, asd='asd', an=return_name())
print()

def alltogether(*args, **kargs):
    print(args, kargs)

alltogether(1, 2, 3, x=11, y=22, z=33)
alltogether(2, 3, z=223, w=34)
alltogether(x=2, ccjdjdjdj=1231)
print()

def alltogether_2(a, b, c=12, *args, foo, bar='python', **kargs):
    print(a, b, c, args, foo, bar, kargs)

alltogether_2(1, 2, 1122, 3, 4, foo=2, x=666, y=777)
alltogether_2(1, 2, 3, 4, foo=2, x=666, y=777)
alltogether_2(1, 2, 3, 4, x=666, y=777, foo='foo')
alltogether_2(1, 2, 3, x=666, y=777, foo='foo')
# tip use *a *arg *args **k **ka **karg **kargs **kwarg **kwayargs
print()
