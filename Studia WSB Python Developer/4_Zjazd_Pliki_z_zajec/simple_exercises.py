


# write func 'combined_sum'
# taking 3 variables returning their sum
def combined_sum(x, y, z):
    return x + y + z

print(combined_sum(1,2,3))
print(combined_sum('1','2','3'))
print()



# write combined_sum_2 taking any number of positional arguments
# return their sum do not use sum :-D
def combined_sum_2(*args):
    sum = 0
    for i in args:
        sum = sum + int(i)
    return sum

print(combined_sum_2(1,2,3,4,5))
print(combined_sum_2(1,2,3,4,5.1))
print(combined_sum_2('1','2','3','4','5'))
print()


# write decorator printing args passed to function
def print_args_kags(func):
    def wrapper(*args, **kargs):
        print(args, kargs)
        return func(*args, **kargs)
    return wrapper

@print_args_kags
def combined_sum(x, y, z):
    return x + y + z

@print_args_kags
def combined_sum_2(*args):
    sum = 0
    for i in args:
        sum = sum + int(i)
    return sum

print(combined_sum(1,2,3))
print(combined_sum_2(1,2,3,4,5))
print()

# write function printing
# ****
# ****
# ****
# ****
# taking x and printing x times x sters
def rectangle(x):
    for i in range(x):
        print('*' * x)

rectangle(15)
rectangle(5)
print()

# write function printing
# *
# **
# ***
# ****
# do not use '*' * x construction
def triangle_with_xyz(x):
    for y in range(x):
        for z in range(y+1):
            print('*', end='')
        print()

triangle_with_xyz(15)
triangle_with_xyz(5)
print()

def triangle_with_names(x):
    for height in range(1, x+1):
        for width in range(height):
            print('*', end='')
        print()

triangle_with_names(15)
triangle_with_names(5)
print()

# write function printing
#    *
#   **
#  ***
# ****
# do not use '*' * x construction
def right_triangle(x):
    for height in range(1, x+1):
        for spaces in range(x-height):
            print('_', end='')
        for stars in range(height):
            print('*', end='')
        print()

right_triangle(15)
right_triangle(5)
print()




#
