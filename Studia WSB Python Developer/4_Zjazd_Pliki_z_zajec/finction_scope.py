

outer = 'crow mask'

def country_duel():
    outer = 'spy'
    inner = 'param'
    print(outer + ' vs ' + inner)

# print(inner)  #NameError
country_duel()

def will_print():
    print = object()
    try:
        print('foo')
    except TypeError as err:
        # DO NOT SHADOW PYTHON FUNCTIONS !!!
        # but this is how to hadle this ?
        import builtins
        builtins.print('error occurred')
        builtins.print('type(err) ', type(err))
        builtins.print(err)
        pass

will_print()
print('bar')
print()

foo = 'foo'

def outer_func():
    foo_outer = 'foo_outer'
    print('outer before inner declaration')
    def inner_func():
        foo_inner = 'foo_inner'
        print('inner', foo, foo_outer, foo_inner)
    print('outer after inner declaration')
    inner_func()

outer_func()

print()

def outer_func(*outer_args, **outer_kargs):
    def inner_func():
        return 'arg passed form outer', outer_args, outer_kargs
    return inner_func()

print('>>', outer_func('foo_bar_baz', foo='bar'))
print()

def outer_func_2(*outer_args, **outer_kargs):
    def inner_func(*inner_args, **inner_kargs):
        return outer_args, outer_kargs, inner_args, inner_kargs
    return inner_func

result_func = outer_func_2('foo', foo='bar')
print('>>', result_func('bar', bar='bar'))
print()

def add_x_factory(x):
    def add_x(y):
        return x + y
    return add_x

add_2_func = add_x_factory(2)
add_5_func = add_x_factory(5)
print(add_2_func(2), add_5_func(5))
print()


def print_me(name_foo):
    print('me ' + name_foo)

def print_him(name_bar):
    print('him ' + name_bar)

def pass_and_execute(func, name):
    func(name)


pass_and_execute(print_me, 'Filip')
pass_and_execute(print_him, 'Adrian')
print()

add_2_func = lambda x: x+2
print(add_2_func(2))
add_3_func = lambda x: x+3
print(add_3_func(3))

print()
#
