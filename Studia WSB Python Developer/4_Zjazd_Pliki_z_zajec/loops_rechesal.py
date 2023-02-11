
tange_10 = range(10)
range_10 = [0,1,2,3,4,5,6,7,8,9]

def print_10_for_loop(x):
    for i in range(x):
        if i < 5:
            print('continue')
            continue
        if i == 7:
            print('break')
            break
        print(i)

print_10_for_loop(10)
print()

def print_10_while_loop(x):
    i = 0
    while i < x:
        i = i + 1
        if i < 5:
            print('continue')
            continue
        if i == 7:
            print('break')
            break
        print(i)

print_10_while_loop(10)
print()




#
