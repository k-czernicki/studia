

def print_start_end(func):
    def wrapper():
        print('+++ start +++')
        func()
        print('+++  end  +++')
    return wrapper

def print_foo():
    print('foo-bar-baz')

print_foo = print_start_end(print_foo)  # decoration
print('+++calling+++')
print_foo()
print()

@print_start_end
def print_baz():
    print('baz-bar-foo')

print('+++calling+++')
print_baz()
print()

def print_start_end_2(func):
    def wrapper(*args, **kargs):
        print('+++ start +++')
        result = func(*args, **kargs)
        print('+++  end  +++')
        return result
    return wrapper

@print_start_end_2
def print_buzz(a, b, name='bazz'):
    return name, a + b

@print_start_end_2
def print_wooo(key, val):
    return key, val

print('+++calling+++')
print(print_buzz(11, 22))
print(print_wooo('foo', val='bar'))
print()



print()

#
